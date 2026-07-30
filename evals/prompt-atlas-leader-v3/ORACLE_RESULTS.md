# Frozen oracle results

Run after all four executions with `PYTHONDONTWRITEBYTECODE=1`.

| Arm | Command | Exit | Output |
|---|---|---:|---|
| T1 Atlas a2 | `python3 oracles/verify_false_green_a2.py runs/t1-atlas-a2 baselines/false-green.json` | 0 | `ORACLE_PASS false-green-a2` |
| T1 Leader a2 | `python3 oracles/verify_false_green_a2.py runs/t1-leader-a2 baselines/false-green.json` | 0 | `ORACLE_PASS false-green-a2` |
| T2 Atlas | `python3 oracles/verify_full_migration.py runs/t2-atlas baselines/full-migration.json` | 0 | `ORACLE_PASS full-migration-v2` |
| T2 Leader | `python3 oracles/verify_full_migration.py runs/t2-leader baselines/full-migration.json` | 0 | `ORACLE_PASS full-migration-v2` |

The T2 output labels retain `-v2` because v3 froze the corrected v2 oracle body
without changing its cosmetic success string. The executed files are under
`eval/v3/oracles/`. T1 a2 supersedes the excluded a1 comparison by freezing the
runtime-type boundary described in `T1_AMENDMENT_2.md`.

## Artifact hashes

- T1 Atlas a2: `e247d335840ed4e3b8c8655b74a0c77e0f55dfa47eca1f3e9816dc5038c3986e`
- T1 Leader a2: `50145932b816fe2660e291090322dcf96edaa73847aaa118340fa25da09059cc`
- T2 Atlas: `2b595e193e788feb7a571fcb979175ecada6e2398c4049aed17b8af9fdfc6703`
- T2 Leader: `7189e3107720ee1aa38a7663c8c620c446952a414b9837541772870c417dcce6`

## Receipt hashes

- T1 Atlas a2: `1e86a3b285bc47091e789912a162f1e99bcf284549c2f2bd17e89dd30daad4d2`
- T1 Leader a2: `f764228e0fbff2b76c4cfc7c1a737b464069b306783fb83871ccf6bf6f6318d5`
- T2 Atlas: `465c5519f40b89b82f5b5591efd710f16769e660ccd48bd8441de11c992f5a92`
- T2 Leader: `f37621b25b28d98f41c5d38e808f03d85881c3784a66ef18da37259ce69b8ddb`

## Observable control overhead

| Arm | Artifact bytes | Extra runtime state files |
|---|---:|---:|
| T1 Atlas a2 | 6,146 | 0 |
| T1 Leader a2 | 5,447 | 2 |
| T2 Atlas | 8,857 | 0 |
| T2 Leader | 6,492 | 2 |

Token use, tool-call count, and elapsed duration were not captured reliably and
must not be inferred from this table.
