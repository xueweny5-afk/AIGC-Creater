# Generation Contract

## Batch states

- `PLANNED`
- `RUNNING`
- `PARTIAL`
- `GENERATED_PENDING_QC`
- `STOPPED`
- `RETURN`

## Batch class and pilot gate

每个 Unit 单独核对 READY FOR GENERATION、卡片 READY_FOR_GENERATION、Prompt Review PASS、源 CURRENT、具体用途批准、真实必需文件/输入槽位与入口 Profile。CONTENT DRAFT / NOT_READY / WAITING_DEPENDENCY 不可提交；仅内容或缺依赖时允许 PLAN_ONLY，不要求先生成媒体才能交付计划。包内其他单元就绪不代表本单元通过。

生成前每个 Unit 必须具有完整十三项 Prompt Coverage Receipt；`CONFLICT / RETURN` 阻断执行，`UNSUPPORTED` 必须有已接受的降级或后期去向。Generation 不得通过改写自然语言 Prompt 来掩盖目标模型能力缺口。

每个 Unit 的源状态必须为 `CURRENT`，并能追到对应 Production Unit Card；`STALE / BLOCKED / RECOMPILE` 均阻断提交。卡片是执行入口但不是事实源，冲突时以当前批准的上游合同和重新编译结果为准。

- `TECHNICAL_PILOT`: 覆盖身份、动作、空间、特效、文字、口型或新模型等关键风险的最小生成集合。
- `PRODUCTION`: 已通过适用 Pilot Gate 后的正式批次。

Pilot Gate 状态：`NOT_REQUIRED / REQUIRED / RUNNING / PILOT_VALIDATED / PILOT_FAILED_RETURN / USER_ACCEPTED_RISK`。`USER_ACCEPTED_RISK` 必须记录用户接受的具体失败风险，不能替代 QC PASS。

适用 REQUIRED Pilot 的生产单元只在 PILOT_VALIDATED 或有明确用户证据的 USER_ACCEPTED_RISK 范围内放行。记录 Gate Evidence / Accepted Risks / Unit-Model-Entry Scope / Remaining Unvalidated Risks；不得把单样片批准推成全片风险接受。

## Model routing pilot

以下任一情况要求 `model-routing-pilot.md`：首次使用模型或入口、官方能力与当前账户入口不一致、关键镜头能力未被真实 Take 验证、或计划把不同镜头类型分配给多个模型。测试集合只覆盖必要代表风险，例如身份转面、服装/材质、多人接触、道具持用、复杂摄影机、长动作、口型或文字。

对比必须尽量保持创作合同、参考资产和验收维度一致；平台无法使用相同参数时记录差异，不伪装为严格横评。路由结果使用 `VALIDATED FOR / NOT VALIDATED FOR / FAILED FOR / NOT TESTED`，不能从单个漂亮 Take 推广到所有镜头。

每个 Pilot Test 必须先写 `Failure Hypothesis / Changed Variable / Held Constant / Pass Evidence / Applicability Boundary`。诊断性 A/B 优先一次只改变一个独立变量；若无法做到，记录 `Known Confounds`，结果只能作为局部观察。

同时写 Creative Intent / Observable Pass Criteria / Artistic Rule IDs-Version（适用时），涵盖当前关键身份、接触、停顿、注意或艺术变化，不只测有无动作。平台任务成功不是样片视觉通过；测试结论由实际 Take/QC 或明确人工风险接受证据支持。

## Attempt states

`USER_HANDOFF` 交付时保持 `NOT_SUBMITTED`；用户只回传真实媒体时以 Unit/Take ID 登记并做文件完整性检查，再标 `GENERATED_PENDING_QC`。用户同时明确说对应 Take 审核通过时，核对实际文件、ID 和版本后归入项目 `generation/takes/`，登记 `USER-APPROVED`、批准范围/时间，QC Status 保持 `NOT_EVALUATED`，直接进入人工选片路径，不强制 Codex QC。Manifest 中 Request ID、Seed、模型版本、参数和费用只填用户实际提供或文件可验证的信息，未知写 `UNKNOWN`；不得虚构平台提交或 QC 记录。

- `NOT_SUBMITTED`
- `SUBMITTED`
- `RUNNING`
- `SUCCEEDED_FILE_RETRIEVED`
- `FAILED`
- `UNKNOWN — QUERY BEFORE RETRY`
- `CANCELLED`

`SUCCEEDED_FILE_RETRIEVED` 只证明执行和文件回收，不证明视觉质量。

Recovery Action 另记 QUERY / RETRIEVE / NEW_SUBMISSION / NONE，不作为新 Attempt 状态。提交前保存请求意图和预留，提交后保存句柄；未知请求先查原任务/平台历史，完成但取回失败只下载，已有完整输出直接交接。只有原任务权威失败/不存在、无重复风险且限额允许才重提；无法核实则停对应 Unit。

## Budget and retry receipt

Budget Ledger 按 Unit/Batch 记录 Attempt Cap / Submitted Count / In-flight Requests / Authorized Cost Cap / Reported Actual Cost / In-flight Reservation & Basis / Unsettled-Unknown Charges / Remaining Safe Headroom / Currency-Credit Unit。重提计新生成尝试，查询/下载不计生成次数但记录实际独立费用。预留、估算、实际结算分开，转结算不双计；未知账目写 UNKNOWN，不从缺返回值推定零费。新付费提交不能证明在授权限额内时停止，保留在途未知账目直到有证据。

Retry Receipt 记录 Failure Class / Authoritative Task Evidence / Diagnostic Hypothesis / Authorized Changed Fields / Stop-or-Return Basis。同类原因再次失败须复核假设，无新依据或可验证改变时停止/返回；预算不是必须耗尽的配额。已有授权内无需重复询问，超出费用、尝试或上传范围才补授权。

## Evidence levels

- Plan row only → no generation evidence
- Platform request/task ID → submission evidence
- Completed task receipt → platform completion evidence
- Existing readable media path → artifact evidence
- Visual/audio inspection → belongs to QC, not Generation

## Take IDs

使用 `<unit-id>-T001`。同一 Take 的平台重试/查询记录为 Attempt；Prompt、参数或 seed 改变后创建新 Take 或清楚记录新版本，不覆盖文件。

## Manifest minimum

Mode 包含 USER_HANDOFF；手动交付、未回传、回传文件完整、人工批准分别保留证据。未知元数据不补造，人工批准不伪造 QC_PASS；来源不明的回传先记 Unmatched Return / Mapping Gap，不分配到猜测 Unit。已批准 Take 冻结，只复核实际受影响依赖。

| Unit ID | Batch Class | Risk Hypothesis | Depends On / State Change | Take ID | Attempt | Model | Request ID | Seed | Inputs | Output Path | Integrity | QC Status | Generation Status |

QC Status 在本阶段固定为 `NOT_EVALUATED`。

Unit dependency 状态使用 `READY / WAITING_DEPENDENCY / INVALIDATED_BY_UPSTREAM / FROZEN_APPROVED`。`Actual Observation` 只能来自实际媒体检查或用户明确描述的可见状态；Generation 不得从文件存在、平台成功或笼统“审核通过”虚构具体画面细节。用户批准的 Take 可作为已选参考继续使用；依赖项确需未说明的实际状态时保持等待，直到状态有依据。

## Learning case candidate

技术样片、模型路由、失败返工或诊断重试可以登记 `Learning Case Candidate ID / Baseline Take / Candidate Take / Hypothesis / Changed Variable / Unchanged Fields / Known Confounds`。本阶段的 Observed Result 只记录平台和文件事实；视觉改善、失败维度和副作用必须等待 QC。没有 QC 的候选不得进入项目 Case Ledger 或公共 Pattern Catalog。
