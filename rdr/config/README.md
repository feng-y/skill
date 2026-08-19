Both files use the same schema: `enabled` plus a token list.

Recommended deployment paths:

```text
/etc/rdr/access.json             # host-local
/data/bucket/rdr/access.json     # shared/global mounted bucket file
```

Policy composition:

```text
enabled = local.enabled AND global.enabled
tokens  = local.tokens UNION global.tokens
```

Real token files are deployment secrets and must not be committed. `access.example.json` is schema only.

The authoritative operational guide is [`../DEPLOYMENT.md`](../DEPLOYMENT.md).
