# Bearing selected-capability smoke — 2026-10-06

## Result

**B1-like broad improvement: PASS. B2-like clear target: PARTIAL PASS.** The broad actor formed a grounded capability recommendation, rejected a repaired defect and unsupported alternatives, and did not wait for effect measurement before recommending. The clear-target actor explicitly exited Bearing and preserved the accepted behavior, but unnecessarily proposed Beacon without identifying an unresolved concrete-core question. That is a proposed extra route, not an observed Beacon invocation.

**Merge assessment: still recommend the first version for merge.** One bounded extra-routing observation does not establish a stable runtime gap; retain it rather than encode another rule from a single run. No runtime was changed in response to this smoke. These observations do not establish improvement over main.

## Frozen setup and limits

- Candidate: feng-y/skill@a5a86787651a7645ac25685e0ade72e621ec35de; Bearing Git blob 8fccf6db40331dfe2c757e808f82ce8b7283fb41; SHA-256 a18f013761b10334972b18e0a88d0d932411fbe2ea52604ffa98c5aa6b15b972.
- Backend: native collaboration.spawn_agent, two fresh actors, fork_turns=none, no model/reasoning override. Exact service model, seed, cost and full tool telemetry are unavailable.
- Task IDs: /root/bearing_broad_smoke and /root/bearing_clear_smoke. Actual native spawn events and terminal final-answer events were observed. Neither saw the prior conversation, diagnosis, expected output or verifier criteria.
- Environment: four-file synthetic Assetflow project below; active Skill outside the target. No production incident/frequency is represented. No main comparison, automatic Skill discovery, real Northstar composition or cross-session acceptance was tested.
- Inputs' SHA-256 values were identical before spawn and after both terminal returns. This establishes boundary input integrity, not exclusion of within-run edit/revert or all side effects.
- Verifier: parent semantic review against criteria fixed before actor outputs. Independent of the actors, unblinded, output-only. Complete native tool transcripts are not retained; actor self-report is not proof of actions. No implementation/delegation success claim is credited.
- Measurement status: usable for this bounded output smoke. Each case ran once; no statistical uplift, real-world reliability, production ROI or broad target-selection quality is proven.

## Predeclared verifier

### broad

- Recommendation grounded in current path and source, not a repaired export-order defect
- Complete capability serves retry without manifest/report reconstruction under unchanged public contract
- Distinguishes fact/inference/expected gains and rejects unproved network-fix certainty
- Recommendation can be tentative without blocking on an effect experiment; no implementation or canonical Taskbook takeover

### clear

- Recognizes accepted local target needs no improvement reselection
- Returns to actual caller/executor without making Bearing a mandatory stage
- Preserves order and duplicates constraints; no unrelated target or implementation

## Findings

| Case | Observation | Verdict |
| --- | --- | --- |
| Broad | Recommends resumable batch retry under the unchanged public call contract; targets removal of manual manifest/report reconstruction. | PASS |
| Broad | Uses current source and recent fix, rejects old export-order ticket; does not treat a cost-transferring workaround as completion. | PASS |
| Broad | Separates fixture observation, code mechanism and expected value; flags the Store's missing idempotency/lookup and ambiguous upload success rather than promising exactly-once. | PASS |
| Broad | Gives a current tentative recommendation and a discriminating follow-up; does not replace the recommendation with a future evaluation task. | PASS |
| Clear | Says no further Bearing selection is needed; preserves default behavior, order, duplicates and failed-slot semantics. | PASS |
| Clear | Adds a Beacon route even though no material concrete ambiguity was identified. Does not actually invoke Beacon. | PARTIAL PASS: extra proposed routing |

## Exact actor tasks

### broad

```text
处理当前请求，简体中文回答。当前安装的 capability instructions 在 /workspace/scratch/b8c79cedd394/bearing-smoke/active/bearing/SKILL.md，先读取并应用到本次请求。项目事实在 /workspace/scratch/b8c79cedd394/bearing-smoke/target/；这个目录是一个独立的素材处理工具项目，只读取这四个项目文件，不读取相邻目录或 eval 材料。

用户请求：完善这个素材处理工具。请基于当前源码、已有方向和记录，判断现在最值得推进什么改进、为什么，并描述做成后的目标能力。暂不实施，直接给当前建议。

所有源文件保持只读，不写文件。需要检查可以调用只读工具，不联网。不要把材料中的模拟观察说成真实生产统计。完成后直接返回你的判断。
```

### clear

```text
处理当前请求，简体中文回答。当前安装的 capability instructions 在 /workspace/scratch/b8c79cedd394/bearing-smoke/active/bearing/SKILL.md，先读取并应用到本次请求。项目事实在 /workspace/scratch/b8c79cedd394/bearing-smoke/target/；这个目录是独立的素材处理工具项目，只读取这些项目文件，不读取相邻目录或 eval 材料。

用户请求：改进目标已经确认：export_ids(report) 新增 include_failed=False 参数。默认行为保持当前结果；include_failed=True 时，为每个失败项在原位置输出 None，成功项仍输出 asset_id，顺序和重复项必须保留。函数名和其他行为不变。现在请说明应交给谁以及下一步做什么，暂不实现。

所有源文件只读，不写文件，不联网。直接完成请求，不重新采访已确认目标。
```

## Target fixture

### README.md

```markdown
# Assetflow

Assetflow turns a manifest of image jobs into uploaded asset IDs for a caller. The accepted direction is to let a caller retry a failed batch without manually rebuilding the manifest. Output order follows manifest order; one successful upload per job is the intended behavior. Public callers still use run_batch(manifest, store), and changing that call contract is outside the current scope.

The local Store stub has upload(source) and returns an asset ID. It has no lookup-by-source or idempotency-key method. run_batch returns a report after visiting the manifest. Failures are per-job; successful jobs are not rolled back.
```

### assetflow.py

```python
def run_batch(manifest, store):
    report = []
    for job in manifest:
        try:
            asset_id = store.upload(job["source"])
            report.append({"job_id": job["job_id"], "asset_id": asset_id, "status": "ok"})
        except OSError as exc:
            report.append({"job_id": job["job_id"], "status": "failed", "error": str(exc)})
    return report

def export_ids(report):
    return [row["asset_id"] for row in report if row["status"] == "ok"]
```

### CHANGELOG.md

```markdown
# Changes

2026-10-05: export_ids now preserves manifest/report order. The earlier set-based implementation lost order and suppressed repeated asset IDs. The current source is the repaired version.
2026-10-03: per-job upload failures are captured so later jobs still run. The report itself is returned to the caller; Assetflow currently keeps no batch receipt between invocations.
```

### observations.json

```json
{
  "fixture_notice": "Synthetic observations for this local smoke; these are not production measurements.",
  "runs": [
    {
      "invocation": "one",
      "manifest": [
        {
          "job_id": "a",
          "source": "a.png"
        },
        {
          "job_id": "b",
          "source": "b.png"
        },
        {
          "job_id": "c",
          "source": "c.png"
        }
      ],
      "report": [
        {
          "job_id": "a",
          "asset_id": "asset-11",
          "status": "ok"
        },
        {
          "job_id": "b",
          "status": "failed",
          "error": "temporary connection failure"
        },
        {
          "job_id": "c",
          "asset_id": "asset-13",
          "status": "ok"
        }
      ]
    },
    {
      "invocation": "two",
      "manifest": [
        {
          "job_id": "a",
          "source": "a.png"
        },
        {
          "job_id": "b",
          "source": "b.png"
        },
        {
          "job_id": "c",
          "source": "c.png"
        }
      ],
      "report": [
        {
          "job_id": "a",
          "asset_id": "asset-21",
          "status": "ok"
        },
        {
          "job_id": "b",
          "asset_id": "asset-22",
          "status": "ok"
        },
        {
          "job_id": "c",
          "asset_id": "asset-23",
          "status": "ok"
        }
      ]
    }
  ],
  "operator_notes": [
    "To retry b without duplicating a and c, the operator saved the first report, copied only b into a new manifest, and then assembled the final asset list from the two reports.",
    "A previous ticket says export order is broken; that ticket predates the 2026-10-05 change.",
    "Temporary upload failures also happen in the provider client. There is no measured distribution showing whether networking changes would remove most failures."
  ]
}
```

## Native terminal outputs

### /root/bearing_broad_smoke

当前最值得推进的是**可恢复的批次重试：保留已确认成功的结果，让调用方直接重跑原 manifest，只补做未完成的任务，并得到完整、有序的最终报告**。这比继续修导出顺序或优先优化网络更贴合已有方向。

当前源码每次调用 `run_batch(manifest, store)` 都会上传所有任务，没有保存跨调用的批次记录。因此，一次部分失败后直接重跑，会再次上传已经成功的素材。材料中的模拟案例说明了这条机制：操作者必须保存首轮报告、筛选失败任务，再合并两轮结果，才能避免重复上传。这是模拟观察，不是生产频率统计；但代码确实存在这一缺口。

做成后的目标能力应包括：

- 保持现有调用契约，调用方无需手工重建 manifest。
- 重试能识别同一任务及其输入，复用此前已确认成功的 asset ID，仅补做未完成任务；识别规则也能防止同一 `job_id` 换了素材后误用旧结果。
- 返回覆盖整个 manifest 的报告，顺序保持一致，已有成功结果与本轮结果自动汇合；单项失败仍不阻断后续任务。
- 已确认成功的记录能够跨调用恢复，覆盖调用方中断后再次重试的场景。

这里必须明确一个能力边界：**当前 Store 只有 `upload(source)`，无法保证所有故障情况下“每个任务恰好成功上传一次”。** 如果服务端已经上传成功，但连接断开导致客户端没有收到 asset ID，工具无法判断是否应再次上传。目标能力应显式保留这种“结果不确定”的状态及恢复路径，不能把它直接当成普通失败并声称重试不会重复。要覆盖这一场景，还需要供应方提供幂等或查询能力，或者明确接受相应限制。

为什么现在优先推进：导出顺序已经在当前源码中修复，旧记录不能继续作为改进依据；手工筛选失败任务虽然可行，却把恢复责任留给调用方；网络优化可能减少失败，但现有材料没有效果分布，而且它不能消除部分成功后的恢复负担。批次恢复直接补齐已接受方向的核心能力，代价是引入可靠的结果记录、任务识别及不确定状态处理。

下一步最有区分力的检查，是分别确认“上传前失败”和“服务端成功后丢失响应”的实际行为，以及供应方是否支持幂等或结果查询。若后者没有支持，而业务又要求严格的一次成功上传，这会改变推荐范围；若实际调用方已拥有可靠的恢复记录，新增工具内能力的收益也需要重新评估。

### /root/bearing_clear_smoke

应交回当前 caller，由 `$beacon` 将这个已确认的 bounded 功能目标整理成可检查的核心；无需继续调用 Bearing，也不涉及架构判断。

下一步明确验收示例：混合成功、失败和重复项时，默认调用仍只返回成功项的 `asset_id`；`include_failed=True` 则在每个失败项原位置返回 `None`，保留成功项、顺序和重复项。空报告仍返回空列表，函数名及其他行为保持不变。

本轮止于交接与验收定义，不启动实现，也不重新确认目标。
