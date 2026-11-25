#!/usr/bin/env node
import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { copyFile, lstat, mkdir, mkdtemp, open, readFile, rename, rm, rmdir, unlink } from 'node:fs/promises';
import { homedir } from 'node:os';
import { basename, dirname, extname, isAbsolute, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { parseArgs } from 'node:util';

const assets = fileURLToPath(new URL('../assets/diagrams/', import.meta.url));
const peleVersion = '1.9.0';
const cacheHome = process.env.XDG_CACHE_HOME || '';
const cacheRoot = join(isAbsolute(cacheHome) ? cacheHome : join(homedir(), '.cache'), 'to-pages');
const cache = join(cacheRoot, `pele-${peleVersion}`);
const renderOptions = { limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 };
const themeOrigin = {
  project: 'pstack-claude',
  version: '0.9.155',
  source: 'https://github.com/michael-denyer/pstack-claude/blob/103a68d9a9aa23759d00ad95b01cb78cb8f57772/plugins/pstack/skills/statechart/references/render.md',
  sourceSha256: '8cca446eb0c8f87f2ef7b97c4b149f59aacdc153134b4217c4bcde09b10ac3c4',
  license: 'MIT',
};

const usage = 'Usage: node diagram.mjs setup|doctor\n'
  + '       node diagram.mjs render INPUT.mmd --out OUTPUT_DIRECTORY [--title TITLE]';

function sha256(value) {
  return createHash('sha256').update(value).digest('hex');
}

async function pathExists(path) {
  try {
    await lstat(path);
    return true;
  } catch (error) {
    if (error.code === 'ENOENT') return false;
    throw error;
  }
}

async function loadPele() {
  const packageDir = join(cache, 'node_modules', 'pele');
  let manifest;
  try {
    manifest = JSON.parse(await readFile(join(packageDir, 'package.json'), 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') throw new Error(`Pele ${peleVersion} is missing from ${cache}. Run setup.`);
    throw new Error(`Cannot read the Pele package in ${cache}: ${error.message}`);
  }
  if (manifest.version !== peleVersion) {
    throw new Error(`Found Pele ${manifest.version} in ${cache}; expected ${peleVersion}.`);
  }
  try {
    const { render } = await import(pathToFileURL(join(packageDir, 'dist', 'pele.js')));
    if (typeof render !== 'function') throw new Error('missing render() export');
    return { render, version: manifest.version };
  } catch (error) {
    throw new Error(`Cannot load Pele ${manifest.version} from ${cache}: ${error.message}`);
  }
}

function themedSvg(svg, css) {
  const openingTag = /^<svg\b[^>]*>/.exec(svg)?.[0];
  if (!openingTag || !svg.endsWith('</svg>')) throw new Error('Pele did not return a complete SVG.');
  // An image reference would leave the standalone SVG dependent on another file or site.
  if (/<image\b/i.test(svg)) {
    throw new Error('The SVG contains an image reference. Use a diagram whose SVG is self-contained.');
  }
  return openingTag + '<style>\n' + css + '</style>' + svg.slice(openingTag.length);
}

async function doctor() {
  const { render, version } = await loadPele();
  const css = await readFile(join(assets, 'statechart.css'), 'utf8');
  themedSvg(render('stateDiagram-v2\n[*] --> Ready', renderOptions).svg, css);
  console.log(`Ready: Node ${process.versions.node}, Pele ${version} (${cache})`);
}

async function setup() {
  if (await pathExists(cache)) {
    try {
      await doctor();
    } catch (error) {
      throw new Error(`${error.message}\nMove the existing cache directory aside and run setup again: ${cache}`);
    }
    return;
  }

  await mkdir(cacheRoot, { recursive: true });
  const staging = await mkdtemp(join(cacheRoot, 'pele-install-'));
  try {
    await Promise.all(['package.json', 'package-lock.json'].map((file) =>
      copyFile(join(assets, file), join(staging, file))));
    const result = spawnSync('npm', [
      'ci', '--prefix', staging, '--cache', join(cacheRoot, 'npm'),
      '--ignore-scripts', '--no-audit', '--no-fund', '--no-global', '--no-update-notifier',
    ], { stdio: 'inherit' });
    if (result.error?.code === 'ENOENT') throw new Error('npm is required for setup. Install npm and run setup again.');
    if (result.error) throw result.error;
    if (result.status !== 0) throw new Error('npm ci failed. See the npm output above and retry setup.');

    try {
      await rename(staging, cache);
    } catch (error) {
      // A concurrent setup may already have installed the same locked package.
      if (error.code !== 'EEXIST' && error.code !== 'ENOTEMPTY') throw error;
    }
    await doctor();
  } finally {
    await rm(staging, { recursive: true, force: true });
  }
}

function escapeHtml(text) {
  return text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
}

async function writeOutput(output, files) {
  await mkdir(dirname(output), { recursive: true });
  try {
    await mkdir(output);
  } catch (error) {
    if (error.code === 'EEXIST') throw new Error(`Output already exists: ${output}. Choose a new directory.`);
    throw error;
  }
  const created = [];
  try {
    for (const [name, content] of files) {
      const path = join(output, name);
      const handle = await open(path, 'wx');
      created.push(path);
      try {
        await handle.writeFile(content);
      } finally {
        await handle.close();
      }
    }
  } catch (error) {
    await Promise.allSettled(created.map((path) => unlink(path)));
    await rmdir(output).catch(() => {});
    throw error;
  }
}

async function renderDiagram(input, output, title) {
  const extension = extname(input);
  if (extension.toLowerCase() !== '.mmd') throw new Error('Input must be a .mmd file.');
  if (await pathExists(output)) throw new Error(`Output already exists: ${output}. Choose a new directory.`);
  const { render, version } = await loadPele();
  const [original, css, licenseText, template] = await Promise.all([
    readFile(input),
    readFile(join(assets, 'statechart.css'), 'utf8'),
    readFile(join(assets, 'LICENSE.pstack'), 'utf8'),
    readFile(join(assets, 'viewer.html'), 'utf8'),
  ]);
  let source;
  try {
    source = new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(original);
  } catch {
    throw new Error(`Input is not valid UTF-8: ${input}`);
  }

  let svg;
  try {
    svg = themedSvg(render(source, renderOptions).svg, css);
  } catch (error) {
    throw new Error(`Could not render ${input}${error.code ? ` (${error.code})` : ''}: ${error.message}\n\nMermaid source:\n${source}`);
  }

  const stem = basename(input, extension);
  const sourceName = basename(input);
  const svgName = `${stem}.svg`;
  const replacements = {
    TITLE: escapeHtml(title ?? stem),
    SOURCE: escapeHtml(source),
    SOURCE_URL: `./${encodeURIComponent(sourceName)}`,
    SVG_URL: `./${encodeURIComponent(svgName)}`,
  };
  const viewer = template.replace(/\{\{([A-Z_]+)\}\}/g, (_, key) => replacements[key]);
  const provenance = {
    renderer: 'pele',
    version,
    options: renderOptions,
    theme: { ...themeOrigin, sha256: sha256(css), licenseText },
    input: { name: sourceName, sha256: sha256(original) },
    svg: { name: svgName, sha256: sha256(svg) },
  };
  await writeOutput(output, [
    [sourceName, original],
    [svgName, svg],
    ['render.json', JSON.stringify(provenance, null, 2) + '\n'],
    ['index.html', viewer],
  ]);
  console.log(`Rendered ${join(output, 'index.html')}`);
}

async function main() {
  if (Number(process.versions.node.split('.')[0]) < 20) {
    throw new Error('Use Node.js 20 or later to run diagram.mjs. Node.js 22 is supported.');
  }
  const [command, ...args] = process.argv.slice(2);
  if (command === '--help' && args.length === 0) {
    console.log(usage);
  } else if (command === 'setup' && args.length === 0) {
    await setup();
  } else if (command === 'doctor' && args.length === 0) {
    await doctor();
  } else if (command === 'render') {
    const { values, positionals } = parseArgs({
      args,
      options: { out: { type: 'string' }, title: { type: 'string' } },
      allowPositionals: true,
    });
    if (positionals.length !== 1 || !values.out) throw new Error(usage);
    await renderDiagram(resolve(positionals[0]), resolve(values.out), values.title);
  } else {
    throw new Error(usage);
  }
}

try {
  await main();
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
