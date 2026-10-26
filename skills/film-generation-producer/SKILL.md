---
name: film-generation-producer
description: 执行已批准的图像或视频 Prompt Package，管理输入文件、平台调用、尝试预算、种子与参数、输出 Take、错误分类和生成日志。用于实际生成或规划/恢复生成批次；不用于改写创作主合同、把文件存在当作质量通过、进行最终连续性质检、剪辑或发布。
---

# Film Generation Producer

可靠地执行 Prompt Package，并为每次尝试留下可复现、可追溯的生产回执。生成结束的状态是 `PENDING_QC`，不是“镜头合格”。

## Required inputs

1. `prompt-manifest.md`、`prompt-package.md` 与对应 Production Unit Card；本次执行的 Unit 为 READY FOR GENERATION、卡为 READY_FOR_GENERATION，源 CURRENT，十三项回执无未解决 CONFLICT / RETURN。混合包只取已明确放行的单元，不执行 CONTENT DRAFT。
2. 已核实的目标模型 Profile；`GENERATE / RESUME / RETRY` 还需可调用工具
3. 所有参考文件的真实路径和批准版本
4. 输出目录
5. 用户授权范围：`GENERATE / RESUME / RETRY` 需明确外部服务、付费额度、最大尝试数、可接受等待和数据上传范围；`USER_HANDOFF` 记录用户自行执行的范围
6. Shot/Prompt Manifest 中的 `Risk Level / Risk Hypothesis / Pilot Priority`；高风险项目还需当前 Pilot Gate 状态
7. 项目采用 Method 时的 `direction/method-adoption.md`、Method Version、专项 Pilot Hypothesis 与 QC 清单

缺少权限、额度或真实输入时，可以 PLAN_ONLY，不得发起调用。

逐 Unit 检查 Package/卡片状态、Prompt Review、Profile 的平台/版本/入口/输入模式及确切用途批准。CONTENT DRAFT、NOT_READY、未满足的 WAITING_DEPENDENCY 不可提交；包里部分可执行不代表全部就绪。沿用已有授权，预算内且范围不变的执行/重试不重复询问；超出范围才补授权。草稿可用于文字规划，不要求先回传媒体。

## Modes

- `PLAN_ONLY`: 建立批次、尝试预算、文件检查和执行顺序，不调用外部模型。
- `USER_HANDOFF`: 沿用 Project Brief 的 `USER_GENERATE`，交付已批准的逐镜执行卡与回传命名，不调用外部模型；用户回传实际媒体后登记并交给 QC。
- `GENERATE`: 在授权与工具可用时执行实际生成。
- `RESUME`: 从已记录的请求/任务 ID、日志和现有文件继续，不重复提交未知状态请求。
- `RETRY`: 只针对已分类失败修改被授权的执行字段；Prompt/Creative 问题返回上游。

每个批次另标 TECHNICAL_PILOT 或 PRODUCTION。适用 REQUIRED Pilot 只有 PILOT_VALIDATED，或用户明确以 USER_ACCEPTED_RISK 放行列明范围后，才能执行对应 Production Units；无风险接受证据不得推定放行。样片外的镜头类型、入口与风险仍未验证。

没有已定项目路线或实际生成要求时默认 `PLAN_ONLY`。Project Brief 的镜头视频方式为 `USER_GENERATE` 时进入 `USER_HANDOFF`；为 `AUTO_GENERATE` 时仍需满足本阶段的实际调用授权。单批改选由用户明确提出并记录，不在每批重新询问。方式为 `OPEN` 且准备执行时才确认。

## Load resources

- 执行前读取 `references/generation-operations-guide.md`。
- 创建批次、日志或验收执行证据时读取 `references/generation-contract.md`。
- 使用 `assets/generation-manifest-template.md`、`assets/take-log-template.md` 与 `assets/model-routing-pilot-template.md`。
- 当一次尝试属于技术样片、单变量诊断、失败返工或可能产生复用知识时，在 Take Log 标记 `Learning Case Candidate`；本阶段只保存证据，不判断通用规律。

## Outputs

```text
AIGC Creater/projects/<project-id>/generation/
├── generation-manifest.md
├── generation-log.md
├── model-routing-pilot.md         # 新模型、未验证能力或多模型比较时
└── takes/<unit-id>/<take-id>.<ext>
```

经 QC 后需要整理学习案例时，由 `film-generation-pattern-curator` 在 `generation/learning/` 创建 Case；Generation 不预建空目录。

## Workflow

1. **Lock and verify the batch.** 记录 Package、Unit Card、采用的 Method ID/Version、模型、Unit 范围、输入版本、权限、预算、停止条件、Batch Class 和 Unit 依赖。先确认 Source Freshness 为 `CURRENT`，再检查每个 Unit 的十三项 Coverage Receipt；`STALE / BLOCKED / RECOMPILE`、`CONFLICT / RETURN`、未说明的 `UNSUPPORTED` 或能力伪支持均返回 Prompt/Model Verification。技术样片同时覆盖适用的 Method-specific 风险，使用最小 Unit 集合，不按镜号批量铺开。首次使用模型/入口、关键能力未验证或需要在多模型间路由时建立 `model-routing-pilot.md`，用同一批准合同和可比输入测试代表性风险，不以宣传资料直接指定整片模型。
2. **Preflight real inputs.** 检查每个文件存在、可读、类型匹配；记录大小和可用校验值。URL 或 manifest 行不等于上传成功。
3. **Plan bounded attempts and pilots.** 按 Unit/Batch 记录尝试上限、已提交数、在途任务与费用账目；查询/下载不计新生成，重提计新尝试，接口另收查询/下载费仍记费用。Pilot 写 Failure Hypothesis / Creative Intent / Observable Pass Criteria / Changed Variable / Held Constant / Applicability Boundary，针对关键接触、身份、停顿、注意或艺术规则，不只测“能动”。关键状态先生成，依赖项需 QC 或用户批准；具体状态仍须媒体检查或用户明确描述。诊断优先单变量，多变量记 Confound。只在已有授权额度内继续，超预算或扩大范围才补授权。
4. **Submit and persist once.** 提交前登记 Unit/Take/Attempt、输入与 Prompt 版本、预算预留/依据；提交后立即保存时间、请求 ID、幂等键（支持时）与完整参数。响应丢失且 ID 未知时保留 UNKNOWN — QUERY BEFORE RETRY，查平台历史/幂等回执，不因本地没文件重提；无法核实则停止该 Unit，其他独立就绪单元可继续。
5. **Resume the recorded task.** 进行中查询原句柄；完成但本地缺文件只取回/下载，已有完整文件则直接交接。超时、下载失败、客户端关闭不等于生成失败。只有权威确认原任务失败/不存在且无重复在途风险、预算与授权允许时才新提交；恢复动作区分查询、下载与新生成。
6. **Retrieve outputs.** 保存原始输出到唯一 Take 路径，记录平台输出 ID、文件大小、容器/图像格式、时长和下载状态。
   - `USER_HANDOFF` 时只接收用户回传的真实文件，按 Unit ID 和 Take ID 登记来源、用户提供的模型/参数信息（未知则标 `UNKNOWN`）与实际路径；不编造请求 ID、种子、费用或模型版本。未回传的 Unit 保持 `NOT_SUBMITTED`。用户同时明确说该 Take 审核通过时，核对文件、ID、版本后直接归入 `generation/takes/` 并登记 `USER-APPROVED`，不再提交 Codex QC。
7. **Run integrity checks.** 文件可打开、非空、基础媒体信息与请求大致相符。这里只检查可用性，不做审美或连续性通过判断。
8. **Classify before retry.** 区分 input/tool/platform/policy/profile/prompt/creative/QC，先记症状、权威任务状态、责任层、下一假设与可改字段。同类原因再次失败先复核诊断；无新依据或可验证改变时 STOP/RETURN，不机械用完次数。视觉问题由 QC 给证据，本阶段不以随机 seed 或加词代替诊断。
9. **Change minimally and preserve approvals.** 重试时列出与上一 Attempt 的差异和理由；只重做失败 Unit，已通过 Take 与已批准资产保持冻结。诊断性尝试优先只改变一个独立变量；关键状态变化后只重编译或复核其 `Affected Dependents`，不整批随机重生。
10. **Prepare learning evidence when relevant.** 对 Pilot、重试、模型路由或单变量测试记录 Baseline Take、Candidate Take、Changed Variable、Unchanged Fields、Known Confounds 和 Learning Case Candidate ID；不写“有效/无效”结论，等待 QC。
11. **Stop and hand off.** 未获用户明确批准的 Take 标 GENERATED_PENDING_QC，交实际文件、日志、风险假设与限制给 QC。用户批准 Take 按范围交选片；Technical Pilot 未经 QC 不称 PILOT_VALIDATED，只有用户明确接受记录的样片风险才以 USER_ACCEPTED_RISK 放行对应范围，单样片批准不自动等于风险接受。

## Attempt record

本阶段 QC Status 为 NOT_EVALUATED；生成/文件完整性状态与人工批准单独记录，不将其写成 QC_PASS。

Budget Ledger 分别记 Unit/Batch Attempt Cap / Submitted Count / In-flight Requests、Authorized Cost Cap、Reported Actual Cost、In-flight Reservation & Basis、Unsettled/Unknown Charges、Remaining Safe Headroom。统一币种/积分口径，预留/估算不冒充结算；预留转结算后不重复扣算。无法核实余额写 UNKNOWN；付费重提若无法证明在授权限额内则停止，不假定免费或零成本。

- Batch / Unit / Take / Attempt ID
- Prompt package hash and source versions
- Target model/version and tool
- Input paths/checksums/upload IDs
- Seed, duration, size, aspect, reference weights and all settings
- Submitted/started/completed timestamps
- Request/task/output IDs
- Cost/credits when exposed by platform
- Recovery Action: QUERY / RETRIEVE / NEW_SUBMISSION / NONE；权威状态证据与预算更新
- Provider / Platform / Task Entry / Input Mode / Approval Scope Evidence
- Result status and exact error
- Output path/size/media probe
- Retry reason and changed fields
- Test hypothesis / observed result / next single change
- Learning Case Candidate ID / baseline-candidate relation / unchanged fields / confounds
- Depends On / state change / affected dependents / actual observation receipt

## Non-negotiable boundaries

- 不执行未获授权的付费调用、外部上传、声音/肖像使用或发布。
- 不在 Prompt Package 之外静默改变主体、镜头、动作、时长、资产或结局。
- 不因平台超时、网络中断或状态未知而重复提交同一任务。
- 不把成功 API 响应、任务完成、文件下载或媒体可打开称为 QC PASS。
- 不选择“最好 Take”并宣称通过；只可标记候选和明显不可用文件。
- 不在 REQUIRED Pilot 尚未 `PILOT_VALIDATED` 且用户也未明确以 `USER_ACCEPTED_RISK` 放行时批量执行 Production Units。
- 不删除失败 Take 或覆盖旧版本；保留可追溯状态。
- 不执行尚未满足依赖的 Unit，不因一个 Unit 失败而覆盖已通过的非受影响 Take。
- 不编辑、拼接、调色、配音或发布。

## Retry policy

- `EXECUTION RETRY`: 短暂平台/网络错误，参数和 Prompt 不变；重用原任务或幂等机制。
- `PARAMETER RETRY`: 参数不符合已核实 profile；修正后创建新 Attempt，记录差异。
- `PROMPT RETURN`: 输出可用但主要动作/构图无法满足，返回 Prompt Adapter，不在此改写。
- `MOTION / SHOT / ASSET RETURN`: 问题来自更早合同，返回最早错误层。
- `STOP`: 达到尝试/费用/权限边界，任务状态或账目无法核实，或同类失败无新诊断依据与可验证改变。

## Completion gate

- 每个 Unit 有明确状态和 Attempt 历史；
- 实际 Take 路径存在、可读且与日志对应，或明确未生成；
- 请求 ID、参数、种子和输入映射在平台或用户提供时可追溯；手动回传未知项标 `UNKNOWN`；
- 重试未超预算且没有未知状态重复提交；
- Unit/Batch 账目包含在途与未结算项，恢复查询/下载未误记成重新生成，未知费用未冒充结算；
- 未获用户明确批准的生成结果只标 `GENERATED_PENDING_QC`；用户批准的 Take 保留 `USER-APPROVED` 来源，不冒充 `QC_PASS`；
- 新模型/入口或多模型比较项目有可追溯的样片矩阵；路由决定只覆盖实际测试通过的镜头类型和风险；
- 下一阶段为 Continuity QC、用户明确批准后的选片/后期，或明确 Return/Stop。
