import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
import { createHash } from 'node:crypto';
import { access, mkdir, mkdtemp, readdir, readFile, rm, writeFile } from 'node:fs/promises';
import { homedir, tmpdir } from 'node:os';
import { isAbsolute, join } from 'node:path';
import { test } from 'node:test';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { promisify } from 'node:util';

const run = promisify(execFile);
const cli = fileURLToPath(new URL('./diagram.mjs', import.meta.url));
const assets = new URL('../assets/diagrams/', import.meta.url);
const options = { limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 };
const flow = 'flowchart LR\r\nA["读取 #1"] -->|"完成"| B["记录"]\r\n';

function command(args, env = process.env) {
  return run(process.execPath, [cli, ...args], { env });
}

async function workspace(t) {
  const directory = await mkdtemp(join(tmpdir(), 'to-pages-diagram-test-'));
  t.after(() => rm(directory, { recursive: true, force: true }));
  return directory;
}

test('doctor checks the installed renderer and an empty cache reports setup', async (t) => {
  const { stdout } = await command(['doctor']);
  assert.match(stdout, /Ready: Node [\d.]+, Pele 1\.9\.0/);

  const cache = await workspace(t);
  const env = { ...process.env, XDG_CACHE_HOME: cache };
  await assert.rejects(command(['doctor'], env), (error) => {
    assert.equal(error.code, 1);
    return /Pele 1\.9\.0 is missing[\s\S]*Run setup/.test(error.stderr);
  });
  assert.deepEqual(await readdir(cache), []);
});

test('matches Pele SVG plus upstream CSS and preserves the portable source bundle', async (t) => {
  const directory = await workspace(t);
  const name = '步骤 #1.mmd';
  const input = join(directory, name);
  const output = join(directory, 'prepared');
  const title = 'Progress <script>alert(1)</script>';
  const statechart = [
    'stateDiagram-v2',
    '[*] --> Ready',
    'Ready --> Check : start',
    'Check --> Fail : drop',
    'Check --> Retry : wait',
    'Retry --> Loop : retry',
    'classDef breaks fill:#fdd,stroke:#d33,color:#900',
    'classDef mayBreak fill:#fed,stroke:#d83,color:#930',
    'class Ready teal',
    'class Check bugPath',
    'class Fail breaks',
    'class Retry mayBreak',
    'class Loop repeats',
  ].join('\r\n') + '\r\n';
  await writeFile(input, statechart);
  await command(['render', input, '--out', output, '--title', title]);
  assert.deepEqual((await readdir(output)).sort(), ['index.html', 'render.json', name, '步骤 #1.svg'].sort());
  assert.deepEqual(await readFile(join(output, name)), await readFile(input));

  const css = await readFile(new URL('statechart.css', assets), 'utf8');
  const hash = (value) => createHash('sha256').update(value).digest('hex');
  assert.equal(hash(css), '86148f1c5f7acb64d97932edc05543920774ba44c452b8f082b2afc883598b41');
  const cacheHome = process.env.XDG_CACHE_HOME || '';
  const peleEntry = join(isAbsolute(cacheHome) ? cacheHome : join(homedir(), '.cache'),
    'to-pages', 'pele-1.9.0', 'node_modules', 'pele', 'dist', 'pele.js');
  const { render } = await import(pathToFileURL(peleEntry));
  const rawSvg = render(statechart, options).svg;
  const svg = await readFile(join(output, '步骤 #1.svg'), 'utf8');
  assert.equal(svg, rawSvg.replace(/^<svg\b[^>]*>/, (tag) => tag + `<style>\n${css}</style>`));

  const meta = JSON.parse(await readFile(join(output, 'render.json'), 'utf8'));
  assert.equal(meta.version, '1.9.0');
  assert.deepEqual(meta.options, options);
  assert.equal(meta.theme.sha256, hash(css));
  assert.equal(meta.input.sha256, hash(statechart));
  assert.equal(meta.svg.sha256, hash(svg));
  assert.match(meta.theme.licenseText, /MIT License/);

  const html = await readFile(join(output, 'index.html'), 'utf8');
  assert.match(html, /<title>Progress &lt;script&gt;alert\(1\)&lt;\/script&gt;<\/title>/);
  assert.match(html, /<img[^>]+src="\.\/%E6%AD%A5%E9%AA%A4%20%231\.svg"/);
  assert.match(html, /href="\.\/%E6%AD%A5%E9%AA%A4%20%231\.mmd"/);
  assert.doesNotMatch(html, /<svg\b|<script>alert\(1\)/);

  const repeat = join(directory, 'prepared-again');
  await command(['render', input, '--out', repeat, '--title', title]);
  for (const file of await readdir(output)) {
    assert.deepEqual(await readFile(join(repeat, file)), await readFile(join(output, file)));
  }
});

test('renders flowchart and sequence sources with no network helpers', async (t) => {
  const directory = await workspace(t);
  const fixtures = [
    ['flow', 'flowchart', flow + '%% ' + 'x'.repeat(52_000) + '\n'],
    ['sequence', 'sequence', 'sequenceDiagram\nAlice->>Server: Submit request\nServer-->>Alice: Confirm\n'],
  ];
  for (const [name, type, source] of fixtures) {
    const input = join(directory, `${name}.mmd`);
    const output = join(directory, name);
    await writeFile(input, source);
    await command(['render', input, '--out', output], { ...process.env, PATH: '' });
    assert.match(await readFile(join(output, `${name}.svg`), 'utf8'), new RegExp(`class="pele pele-${type}"`));
  }
});

test('syntax and external-image failures show the source and leave no output', async (t) => {
  const directory = await workspace(t);
  const input = join(directory, 'invalid.mmd');
  const output = join(directory, 'prepared');
  const fixtures = [
    ['stateDiagram-v2\n[*] -->\n', /syntax/],
    ['flowchart LR\nA@{ img: "https://example.com/icon.png" }\n', /image reference/],
  ];
  for (const [source, message] of fixtures) {
    await writeFile(input, source);
    await assert.rejects(command(['render', input, '--out', output]), (error) => {
      assert.equal(error.code, 1);
      assert.match(error.stderr, message);
      assert.ok(error.stderr.includes(source));
      return true;
    });
    await assert.rejects(access(output), { code: 'ENOENT' });
    assert.equal(await readFile(input, 'utf8'), source);
  }
});

test('refuses to replace existing output and allows only one concurrent writer', async (t) => {
  const directory = await workspace(t);
  const input = join(directory, 'flow.mmd');
  const existing = join(directory, 'existing');
  await writeFile(input, flow);
  await mkdir(existing);
  await writeFile(join(existing, 'index.html'), 'original');
  await assert.rejects(command(['render', input, '--out', existing]), /Output already exists/);
  assert.deepEqual(await readdir(existing), ['index.html']);
  assert.equal(await readFile(join(existing, 'index.html'), 'utf8'), 'original');

  const output = join(directory, 'prepared');
  const args = ['render', input, '--out', output];
  const results = await Promise.allSettled([command(args), command(args)]);
  const failures = results.filter((result) => result.status === 'rejected');
  assert.equal(failures.length, 1);
  assert.match(failures[0].reason.stderr, /Output already exists/);
  assert.deepEqual((await readdir(output)).sort(), ['flow.mmd', 'flow.svg', 'index.html', 'render.json']);
});
