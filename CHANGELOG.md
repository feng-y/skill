# Semantic Changelog

## 2026-09-14 — Prototype → Beacon

PR: #96

`prototype` top-level Skill identity has been replaced by `beacon`.

Northstar, Architecture Evolution, Verify, and Unknowns First now invoke `$beacon` directly. The old `skills/prototype` and `evals/prototype` surfaces were removed after caller migration.

Prototype remains only as an implementation technique inside Beacon, not as a Skill identity or runtime route.

## 2026-09-11 — Capability ownership recentering

PRs: #93 and #94 established the current split across Northstar, concrete shaping, Architecture Evolution, Verify, and Unknowns First. The concrete-shaping Skill was then named `prototype`; the 2026-09-14 migration supersedes that name with Beacon.
