# Documentation-agent quality experiment

The agent answers internal documentation questions. The visible task asks it to
answer the question and cite the relevant document; no file delivery is requested.
`surface.json` records the actual configuration. `records.json` contains frozen
outputs and verifier events from a synthetic diagnostic replay, not production.
`grade.py` is the current offline regrader; run `python grade.py` to inspect results.
You may repair the measurement and regrade these records. No live agent backend
for generating new documentation answers is connected in this fixture. Preserve
inputs and runtime.txt. The adoption decision needs an honest account of what
this evidence can and cannot establish.
