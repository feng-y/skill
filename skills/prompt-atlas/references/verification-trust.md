# When PASS may be lying

Read only when, beyond normal verification, there is one concrete risk that **the implementation is wrong while current checks still report PASS**. The general rule against manufacturing success by weakening the judge belongs to [execution-compile.md](execution-compile.md); this file only decides whether extra counter-evidence is needed.

First state how failure could escape detection. Typical cases are simple: the check never observes the real target; the implementer can bypass the judge; a fixed sample can be tailored to; failures do not propagate; or the decisive claim exists only as self-report.

Then add the smallest check that can disprove that risk. For example, trigger one controlled failure to prove the alarm really fires, use a sample the implementer could not tailor to, or have someone not involved in the implementation re-obtain Evidence in the authoritative environment. Any extra check must come from the same Goal; it must not introduce a hidden new requirement.

If the needed counter-evidence cannot be obtained, report the evidence gap accurately rather than downgrading it to PASS.
