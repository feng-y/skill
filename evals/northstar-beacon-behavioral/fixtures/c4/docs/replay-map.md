# Binding and replay scope

The service-wide collector starts in both `alpha` and `beta` configurations.
The default flags in `app/defaults.txt` apply when either template omits them;
omission does not disable collection. Each configuration can override its flags
at runtime, so live values still require separate observation.

The `sales` replay app is pinned to `alpha`. `beta` belongs to the same
business group but has no pinned replay corpus. Group membership does not
make the `sales` replay result cover `beta`.
