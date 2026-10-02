# EventSampler correction

The collector currently rejects a valid event when its item count is zero.
The requested code change retains such events while preserving existing
nonzero behavior. A future deployment should then produce usable local and
object-store observations.

The current Taskbook puts all of the following under one "before merge" task:
code correction, discovery of every production deployment, a live object from
the corrected version, and capacity observation. Production rollout remains
separately authorized.
