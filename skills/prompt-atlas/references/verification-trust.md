# When PASS may be lying

Read only when there is a concrete risk that **the implementation is wrong while the current verification still reports PASS**. Without that risk, return to normal verification in `execution-compile.md` and add nothing else.

First state how failure could escape detection. Typical cases are simple: the check never observes the real target; the implementer can modify or bypass the judge; a fixed sample can be overfit; failures do not propagate; or the decisive claim exists only as self-report.

Then add the smallest check that can disprove that risk. For example, trigger one controlled failure to prove the alarm really fires, use a sample the implementer could not tailor to, or have someone not involved in the implementation re-obtain Evidence in the authoritative environment. Any extra check must come from the same public Goal; it must not introduce a hidden new requirement.

No approach may manufacture green by using skip/todo, weakening assertions, deleting live tests, mocking away the target, changing thresholds, swallowing failures, or editing the acceptance check. If the needed counter-evidence cannot be obtained, report the evidence gap accurately rather than downgrading it to PASS.
