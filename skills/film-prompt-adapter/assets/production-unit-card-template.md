# PRODUCTION UNIT CARD

> 本卡是从已批准合同编译的执行视图，不是新的创作事实源。源文件变化后必须重新编译。

内容草稿按实际探索稿来源登记，Package 为 CONTENT DRAFT，Execution 为 NOT_READY；直接复制区只交付文字，不代表可以执行，待补参考/能力在正文外列明。

## UNIT STATUS

- **Project / Sequence / Scene / Shot / Frame / Clip / Unit IDs：**
- **Compiled View Version：**
- **Package Status / Scope / Delivery Boundary：**
- **Pending Dependencies / Validation：**
- **Provider / Platform / Model-Version / Task Entry / API-UI Route / Account-Region Scope：**
- **Source Versions：** Screenplay / Visual / Asset / Shot / Frame / Motion
- **Source Freshness：** CURRENT / STALE / BLOCKED / RECOMPILE
- **Batch Class：** TECHNICAL_PILOT / PRODUCTION
- **Execution Status：** NOT_READY / READY_FOR_GENERATION / GENERATED_PENDING_QC / QC_SELECTED / USER-APPROVED / RETURN
- **Execution Route：** USER_GENERATE / AUTO_GENERATE / OPEN；单批覆盖及范围：
- **Target Filename / Return ID：**
- **Adopted Method IDs / Versions / Scope：**

## SHOT JOB & HANDOFF

- **Narrative Function / Rhythm Role：**
- **Viewing Stance / Information Alignment / Must Read-Withhold / Composition Relations：**
- **MAIN：**
- **SUPPORT：**
- **HOLD：**
- **Previous Residue：**
- **Trigger：**
- **Continuation Basis / HOLD Purpose：**
- **Delay：**
- **Visible Change：**
- **Handoff / End State：**
- **Sound Causality：** trigger / sync / bridge / post-only / not applicable

## LOCKED SOURCES

- **Asset IDs / Versions：**
- **Narrative Look Arc / Scene Look-Light / Atmospheric Medium State：**
- **Presentation Mode / Artistic Rule IDs & Versions / Layer / Change or HOLD：**
- **Input Frame Role / Input Use：** START-MID-END-REFERENCE / CURRENT START-TARGET END-REFERENCE ONLY；逐输入说明
- **Continuity / State Dependencies：**
- **Risk Hypothesis / Pilot Scope：**
- **Method-specific Mechanism / HOLD / Failure Risks：**

## CREATIVE AUTHORITY

- **LOCKED：**
- **DERIVED / Basis：**
- **CREATIVE — Intent / Audience Effect / Continuity Cost / Generation Risk：**
- **PROPOSAL returned upstream：**

## 操作｜参考图与关键帧 @绑定

| Upload Order | Logical Alias | File / Version | Role | Controls | Permitted Change | Must Not Transfer / Override | Platform Slot |
|---:|---|---|---|---|---|---|---|

## 操作顺序｜按编号执行，不复制到模型

1. **前置条件：** READY / WAITING_DEPENDENCY；必须先通过的 Unit/Frame 与 QC：
2. **平台与任务入口：** 模型/版本、图片或视频模式；未核实则 MODEL VERIFICATION REQUIRED
3. **参考图上传：** 按上表编号逐项上传，核对实际槽位与角色
4. **参数设置：** 画幅、时长、分辨率等已核实且适用的外部参数
5. **复制提示词：** 主提示词；平台支持独立负向栏时再复制负向提示词
6. **生成与保存：** 一次执行的目标文件名、Take ID 与实际参数记录
7. **回传与放行：** 按 ID 回传原文件；用户可同时注明“审核通过”，则按人工批准范围入库，否则等待 Codex 审核；依赖卡按相应批准范围解锁

## 直接复制｜关键帧主提示词

不适用时写 `NOT_APPLICABLE`。

## 直接复制｜视频主提示词

不适用时写 `NOT_APPLICABLE`。

## 直接复制｜负向提示词

平台无独立负向输入时，标明哪些高风险约束已被压缩进主提示词，剩余内容不得假装生效。

## 不要复制｜生成后验收

- **Start / Trigger / Delay / Visible Change / End：**
- **Identity / Wardrobe / Scene / Prop / Material / Light / Atmosphere：**
- **MAIN readable / SUPPORT subordinate / HOLD preserved：**
- **Continuity In / Out and edit handles：**
- **Unsupported / degraded capability check：**
- **Prompt Review Result / Evidence / Pending Pilot Validation：** PASS / REVISE / NOT_EVALUATED；检查完整输入组合，文本审核不等于效果通过
- **Method-specific QC：** core mechanism / target audience effect / typical failures / validation boundary

## EXECUTION EVIDENCE

- **Prompt Package / Hash：**
- **Take / Attempt / Output Path：**
- **QC Result / Issue IDs：**
- **User Approval / Date / Scope（如有）：**
- **Actual Observation / Affected Dependents：**
- **Next Action：**
