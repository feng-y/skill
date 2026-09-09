# Upstream

Adapted from Warp's `skill-doctor` in `warpdotdev/common-skills`, pinned during integration to commit `b811c24365ae505bfc9646458957b886e29110b5`.

Upstream: https://github.com/warpdotdev/common-skills/tree/main/.agents/skills/skill-doctor
Product page: https://www.warp.dev/skill-doctor

This repository intentionally keeps a smaller local-only implementation: Codex/Claude collectors, the scoring/attribution method, and Markdown/JSON reporting. Warp's branded HTML renderer, large diff UI bundle, and unsupported collectors are not vendored.
