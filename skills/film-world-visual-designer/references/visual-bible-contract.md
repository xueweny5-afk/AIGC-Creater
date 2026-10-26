# World & Visual Bible Contract

## Required deliverables

### `world-visual-bible.md`

固定包含：

1. `Visual Bible Identity`
2. `Continuity Contract`
3. `Visual Thesis`
4. `World Visibility Rules`
5. `Character & Group Identity Rules`
6. `Costume & State Logic`
7. `Location & Spatial System`
8. `Prop & Material System`
9. `Environment Detail & State System`
10. `Color / Light / Texture Grammar`
11. `Narrative Look Arc`
12. `Scene Look & Light States`
13. `Motif & Change Rules`
14. `Reality / Research Boundaries`
15. `Reference Translation`
16. `Continuity Risks`
17. `Decision Register`
18. `Next Stage`

Visual Bible Identity 记录 Source Versions & Ready Scope、本次交付与终止阶段。Visual Thesis 包含 Visual Proposition 与 Direction Decision / Basis；方向未定时才附 Direction Comparison 的表达重点、人物/环境关系、媒介/现实规则和连续性代价，已定方向可标 NOT_APPLICABLE。选择继续使用 LOCKED / ASSUMED / OPEN 及来源，不把比较当作已批准。

World Visibility Rules 记录 `Presentation Mode: PHYSICAL / STYLIZED / MIXED` 及适用范围；Color / Light / Texture Grammar 的 Visual Relation Rules 记录 Rule ID、Story / Scene Scope、Relation、Stable / Allowed Change、Observable Criterion。只定义项目/场景级关系，不进入镜头机位和构图。

Artistic Presentation Rules 放入 World Visibility Rules，记录 Rule ID、Story Function、Scene / State Scope、Visible Rule & Stable Features、Entry / Exit Trigger、Allowed Change、Protected Identity / Facts。无艺术规则写 NONE；非写实不是事实准确性声明，也不自动改变批准身份或剧情。

### `asset-requirements.md`

每项资产记录：

- `Asset ID`
- `Type`: CHARACTER / GROUP / COSTUME / MAKEUP-HAIR / COMBINED_LOOK / LOCATION / PROP / MATERIAL / ENVIRONMENT_STATE / GRAPHIC / EFFECT STATE
- `Narrative Function`
- `Required Views / States`
- `Material / Environment Detail Plates`
- `Physical / Lighting Response`
- `Dependencies`
- `Locked Features`
- `Variable Features`
- `Evidence Status`
- `Continuity Risk`
- `Priority`: P0 / P1 / P2
- `Approval Gate`
- `Visual Rule / State IDs`、`Observable Acceptance`、`Verify At Stage / Validation Status`：核心规则的资产/状态映射、可观察验收点与实际验证责任阶段。设计时为 PLANNED，不能填资产或画面已验证；跨主体构图留给 Storyboard，不为证明规则自动生成关键帧。

此文件只提出任务，不包含生成 Prompt。

### `reference-analysis.md`（条件式）

只有存在外部视觉参考时创建。每条记录至少包含：`Reference ID / Source / Exact Path or Version / Rights Status / Observed Qualities / Classification / Project Contract Source / Allowed Influence / Must Not Override / Original Transformation / Exclusions / Evidence or Approval`。

- `HARD_ANCHOR` 必须指向已批准的项目合同字段；不得由外部风格参考本身推断。
- `SOFT_REFERENCE` 只迁移抽象方法，不传递具体人物、服装、构图、文字、品牌或标志性表达。
- `EXCLUSION` 明确记录水印、错误人物、错误时代元素、文字、品牌及其他必须排除内容。
- 没有外部参考时不创建该文件，并在 Visual Bible 写 `NOT_APPLICABLE`。

## Scene look and light state

先用 `Narrative Look Arc ID` 记录时期/章节/关系阶段、叙事功能、色彩/对比、光线/空气倾向、材料呈现、进入条件和退出触发。每个核心场景状态再使用稳定 ID，例如 `LLS-LOC03-NIGHT-RAIN-V1`，至少记录：Location/Scene State、Narrative Look Arc ID、Time/Weather、motivated sources and direction、contrast/exposure relationship、color-temperature relationship、Atmospheric Medium / Source / Distribution / Density / Driver / Light Interaction、subject light、material response、allowed changes、change trigger。没有空气介质时明确写 `NONE / CLEAN AIR`。下游默认继承该 ID，只有剧情触发或已批准导演意图才记录偏差。

另附 Presentation Mode / Artistic Rule IDs，STYLIZED / MIXED 的非物理光色或材料效果引用对应艺术规则，不能假填物理光源。Atmospheric Medium 字段只描述真实空气层，无真实介质仍为 NONE；非物理纹理或象征形态在艺术规则中独立记录。光色变化可由批准的感知/记忆转换触发，不机械对应悲喜。

## Validation and review

Continuity Risks 包含 Visual Rule Validation：`Rule / State ID / Asset IDs & Views or States / Observable Criterion / Verify At Stage / Validation Status`，责任范围与 Asset Requirements 一致；文本设计阶段为 PLANNED。单资产证明不了的关系、关键帧整体或动态转换写明后续验证阶段，不以文档存在推定图像通过。

Decision Register 包含 Visual Review：`Result: PASS / REVISE / NOT_EVALUATED`、Scope & Evidence、Findings & Resolution 和来源。按 guide 审阅视觉命题、关系语法、变化触发、参考职责及验收映射。PASS 与 READY FOR ASSET DESIGN 只表示文本合同可交接，不代表用户批准、像素质量或 G3；范围和影响交接的 OPEN 项须明确。

## Evidence status

- `DOCUMENTED`: 有直接可靠视觉或文本依据。
- `RESEARCH-INFERRED`: 从多个可靠资料推导，需说明限制。
- `CREATIVE`: 原创设计，不能冒充史实或传统定制。
- `ASSUMED`: 低风险临时设计，可更改。
- `OPEN`: 未决定。
- `UNKNOWN`: 资料不足，不能填造。

## Identity vs state

- `Identity anchor`: 跨场和跨图不可漂移的辨识特征。
- `Variable state`: 剧本要求发生变化的脏污、损坏、天气、伤势、服装层或道具状态。
- `Presentation choice`: 背景、视角、排版等资产展示方式，不属于角色或场景身份。

## Status

- `READY FOR ASSET DESIGN`
- `VISUAL DECISION GATE`
- `RESEARCH RETURN`
- `SCREENPLAY REVISION`
- `CHARACTER REVISION`
