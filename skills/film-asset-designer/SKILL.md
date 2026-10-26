---
name: film-asset-designer
description: 依据已批准的 World & Visual Bible 和 Asset Requirements 规划、生成或审核电影人物、服装、妆发、场景、道具与状态参考资产，并维护版本化身份合同和资产清单。用于人物正脸身份锚点、头部角度、全身六视图、表情、独立服装/妆发、组合造型、场景正反视图、道具与材质细节资产；不用于剧本、镜头、分镜、关键帧或视频提示词。
---

# Film Asset Designer

建立可复用、可审核的静态视觉资产，稳定后续场景、分镜和视频中的身份与空间连续性。资产图是参考合同，不是最终镜头。

## Required inputs

1. `world-visual-bible.md`，状态为 `READY FOR ASSET DESIGN`
2. `asset-requirements.md`
3. `screenplay.fountain` 与 register
4. `Character System`（人物资产）或研究来源（历史/现实资产）
5. 用户提供和已获许可使用的参考图（如有）

若 Visual Bible 为 Return/Gate，或核心身份字段仍会改变人物、文化或历史含义，不生成对应资产。可继续处理不受该决定影响的独立资产。

继承 Visual Bible / Asset Requirements 的版本、本次范围、Visual Rule / State IDs、Presentation Mode、Artistic Rule IDs 与 Observable Acceptance；新版视觉合同应已完成 Visual Review，旧版已批准成果核对实质范围，不为补字段重做。规则只授权对应设计与审核，不扩大实际生成或外部上传权限。

## Modes

- `PLAN_ONLY`: 输出资产任务、身份合同和审批 Gate，不调用生成工具。
- `HANDOFF`: 输出带编号、参考图角色、依赖顺序和目标文件名的完整提示词包，由用户在外部网页或统一模型会话中生成；收到图片后转入 `REVIEW`。
- `GENERATE`: 用户要求实际生成且可用图像工具时，生成所需最小资产，逐项检查。
- `REVIEW`: 审核用户已有或已生成资产，更新状态并给出具体返工项。

未明确要求实际生成时，默认 `PLAN_ONLY`。不要把规划误报为已生成。

## Load resources

- 开始任何资产工作前读取 `references/asset-design-guide.md`。
- 创建合同、清单或审核时读取 `references/asset-contract.md`。
- 编写人物、服装、妆发、场景、材质或道具生成提示词时，读取 `../film-prompt-adapter/references/asset-prompt-patterns.md`；涉及空气、天气与材料响应时另读 `../film-prompt-adapter/references/material-atmosphere-patterns.md`，返工时读 `../film-prompt-adapter/references/repair-and-exclusion-patterns.md`。这些是共享写法库，不改变本 Skill 的资产审批与生成权限。
- 使用 `assets/asset-manifest-template.md` 与 `assets/asset-contract-template.md`。

## Outputs

默认结构：

```text
AIGC Creater/projects/<project-id>/assets/
├── asset-manifest.md
├── characters/<asset-id>/asset-contract.md
├── costumes/<asset-id>/asset-contract.md
├── makeup-hair/<asset-id>/asset-contract.md
├── locations/<asset-id>/asset-contract.md
├── props/<asset-id>/asset-contract.md
├── prompts/                         # 仅资产生成提示词
└── generation-log.md                 # 仅实际生成时
```

真实图片保存在对应资产 ID 目录，并在 manifest 登记准确路径。目录只在有实际内容时创建。同一资产的候选版、状态版和历史版不得散落到其他类别。镜头关键帧与分镜帧属于 `storyboard/frames/`，不得放入 `assets/`。没有文件、工具结果或可查看输入时，不得声称图片存在。

## Workflow

1. **Select assets and required use.** 按 P0 → P1 → P2 处理，在 View Matrix 的 Need / Source 写明每个视图/状态对应的 Scene、动作、预计可见范围或连续性风险；未知机位保持待定，不要求先完成下游 Shot List 才能设计资产。不按主角身份自动生成全套；未用视图记 DEFERRED / NOT_REQUIRED 及启用条件，不作为当前生产关口的必填项。
2. **Resolve identity gates.** 检查年龄范围、体态、文化身份、服装层、空间拓扑、材料、尺度和关键状态。高影响字段 OPEN 时，只问一个最上游问题；不要用生成结果替用户做决定。
3. **Write the contract.** 分离 locked_features、variable_states、presentation_choices 和 unknowns，绑定确切视觉规则/状态版本、可观察验收点及后续验证责任；物理与艺术呈现分层，不将全局风格参考变成身份或史实依据。
4. **Choose necessary anchors, views and dependencies.** 先批准当前需要的 Canonical Anchor，再从其确切版本派生必要角度和状态。需要辨认脸部的人物使用中性正面人脸锚点；仅背影、剪影或抽象形象可按需求使用体态/轮廓锚点，注明面部身份未验证，后续露脸前再补。六视图仅在当前观看方向和连续性风险确需时建立。人物身份、服装、妆发保持独立合同，再创建有版本依赖的 Combined Look。Contact Sheet 仅作审阅，不替代独立原图或各用途审核。
5. **Assign reference roles.** 每张输入图只登记明确用途：`IDENTITY / WARDROBE / POSE / TOPOLOGY / MATERIAL / STYLE / COMPOSITION / EDIT TARGET`。身份参考不能被构图图覆盖；风格图不能被当成服装或空间事实。角色变体优先从 APPROVED 主身份图编辑派生，而不是重新抽取新身份。
   - 存在 `Atmosphere State ID` 时，干净的 Location/Topology 源图与 Atmosphere Calibration / Material Interaction Plate 分开生成和审批；带雾/烟/尘的图片不能成为唯一空间拓扑依据。
6. **Prepare the prompt.** 在调用任何生图工具前，先向用户展示本批次的完整图片提示词、负面约束、参考图用途与计划文件名；允许用户补充或修改。
7. **Choose generation handoff.** 展示本批提示词后沿用 Project Brief 的资产图片默认执行方式；只有该字段为 `OPEN`，或用户明确要求本批改选时，才询问 `AUTO_GENERATE` / `USER_GENERATE`。本批覆盖记录在交接包中，不改写项目默认方式。没有确定的方式或实际生成授权时不调用生图工具。
8. **Generate or receive.** `AUTO_GENERATE` 才调用图像工具；`USER_GENERATE` 则保留提示词与目标路径，等待用户提供生成图；用户未同时给出验收结论时进入 REVIEW，不重复生成。
9. **Inspect actual images and usable scope.** 对未获用户明确批准的图实际查看像素，先核对身份和批准呈现规则，再检查视图/状态连续性、人物比例、服装层次、道具尺度与持用关系、场景出入口，以及多余文字、肢体或背景干扰。只检查当前资产可以证明的用途，不从中性人物图推定复杂互动已成立；跨主体接触或最终构图留到 Storyboard 验证。用户明确批准确切图片时按其范围入库，不重复审核，也不补写未经评估的维度为通过。
10. **Iterate surgically.** 已批准图只对失败字段做编辑或受控派生，明确 `Change / Preserve / Constraints`；不要为了改一处问题整张重抽并丢失已通过的身份、姿态或拓扑。
11. **Set status and approval scope.** 沿用 PLANNED / GENERATED_PENDING_REVIEW / REWORK / APPROVED / REJECTED，逐文件/视图记状态。APPROVED 只覆盖列明的文件、版本、用途、视图与状态；Approval Scope 与 Unverified / Deferred Use 同时写入合同，manifest 汇总范围。用户批准记录 USER-APPROVED 来源，不冒充 Codex 检查。新需求超出旧范围时保留已批准版本，并建立待验证的扩展版本/视图，不自动扩大批准，也不因无关补图重做旧资产。
12. **Route by required scope.** 当前范围所需 P0 的具体用途、视图与状态均在批准范围内，才推荐生产级 Scene Design；不能只看资产级 APPROVED。缺口推荐对应资产补充或返工。PLAN_ONLY / HANDOFF 可完成文本交付并把依赖标待验证，Scene 草稿可标 DRAFT_ASSET_PENDING；不要求先回传媒体才能交付内容，也不把草稿写成生产就绪。

## Method overlay（采用时）

按 Adoption Receipt 只增加 Method 所需的分层、状态、循环边界、参考职责或专项资产；仍使用稳定 Asset ID、版本和批准状态。专项 Method 不能用合成方便替代人物、服装、场景和道具源资产，也不能从参考作品复制身份。

## Prompt handoff gate

每次实际生图前，交付一个可直接复制的提示词包，至少包含：

- 资产 ID、用途和目标文件名；
- 正向提示词；
- 负面约束；
- 参考图各自承担的角色；
- 必须保持不变的身份、时代、结构或连续性锚点。
- 编辑任务的 `Change / Preserve / Constraints`。

Project Brief 已确定执行方式时沿用该方式；为 `OPEN` 时才询问由 Codex 自动生成还是用户手动生成。用户选择手动生成时，说明把图片放入哪个资产目录或直接上传；若用户未给出验收结论，收到图片后执行视觉审核。若用户已明确说该图片审核通过，核对文件和 ID 后直接入库、登记版本与人工批准，不再做重复视觉审核。项目默认方式不等于外部上传或付费授权。

### Centralized user-generation handoff

用户选择在同一网页模型或统一会话中集中生图时，优先使用 `HANDOFF`，并一次性交付当前阶段完整清单。每一项必须标清：

- Batch ID、Asset ID、优先级与生成顺序；
- 目标文件名和建议上传回传名称；
- 正向提示词、负面约束；
- 每张参考图的编号、路径和唯一用途；
- `CREATE NEW` 或 `EDIT FROM <asset-id>`；
- 必须保持不变的身份、服装、拓扑、材料与历史边界；
- 验收点和常见失败项。

面向无限画布时，每项资产是一张按依赖顺序排列的独立卡片；操作信息、`直接复制｜主提示词`、`直接复制｜负向提示词`、`不要复制｜验收与回传` 分区。提示词正文不夹入文件路径、说明或验收清单；尚未批准的前置资产使依赖卡标 `WAITING_DEPENDENCY`。
批次首页先列实际执行顺序、可并行项与等待项；每张资产卡按编号写 `检查前置资产 → 选任务入口（新建/编辑）→ 按序上传参考图 → 设置已核实参数 → 复制提示词 → 生成并保存目标文件名 → 以 Asset ID 回传 → 用户可同时注明“审核通过”，否则进入 REVIEW`。平台或槽位未确定时明确标待确认，不让用户猜测上传顺序；返工卡只写要改变与保持的字段。

集中交付仍按依赖顺序：先批准当前所需 Canonical Anchor，再派生必要角度与状态，不默认生成全部六视图；服装/妆发独立批准后才创建依赖它们的 Combined Look。场景结构先批准；正式带人物镜头与连续动作帧仍归 Storyboard，不在资产阶段混入。要求回传明确 Asset ID，收到图片后按审核或用户批准范围登记，返工只改失败字段。

## Asset-specific rules

### Character

- 当前需要脸部识别时，先批准无表情、无遮挡、平视、均匀光线的正面人脸锚点；纯背影/剪影或抽象形象按体态/轮廓建立锚点，未验证正脸不得当作已可露脸。
- 头部与全身角度由 View Matrix 的实际用途决定，不设固定数量。确需六视图时可用正面、左前 45°、左侧、背面、右侧、右前 45°；只需其中部分时独立生成并审核对应视图。
- 每个角度从其用途匹配的 APPROVED Canonical Anchor / Canon Face / Body 确切版本编辑派生并保存独立原图；不得以背影母版推定未知五官已锁定，多格表仅用于审阅。
- 优先稳定脸部身份、年龄范围、体态比例、发型、手部/肢体数量与身份标记；服装和妆发作为独立资产锁定后再组合。
- 中性身份图避免戏剧性表演、极端透视、遮挡、复杂背景和镜头级灯光。
- 表情表只包含剧本/场景确实需要区分的状态；不默认九宫格。
- 不由性格、职业、正邪标签推断五官或族群刻板印象。

### Approved artistic presentation

继承 PHYSICAL / STYLIZED / MIXED 及 Artistic Rule IDs，按批准媒介、形态和内部连续性核对资产。中性参考指容易识别与复用，不意味着必须摄影写实；不以统一写实皮肤、织纹或物理比例覆盖绘画/抽象规则。形变需在批准范围内，无依据的身份漂移、随机变形仍是失败。物理空气与非物理纹理/象征形态保持分层，真实空气沿用 Atmosphere State，艺术效果不假填物理来源。

### Location

- 先锁定拓扑、出入口、固定锚点、尺度与主要光源，再做氛围变化。
- 正反向视图必须来自同一空间；检查门窗、工作面、地标和左右关系。
- 为核心场景分别批准结构/整体视图与环境细节板；细节板至少按镜头需要覆盖墙地顶表面、接缝边缘、固定陈设、使用痕迹和空气/天气状态。
- 地面湿度、积尘、污迹、破损、植被、烟雾等不是随机装饰，必须记录成可追踪的 Location State，并说明出现位置和变化原因。
- 场景参考图不等于某一镜头构图，保留导演阶段的观看自由。

### Costume, makeup/hair and prop

- 记录材料、结构、比例、穿戴/持用方式、可见面和状态变化。
- 服装不得只存在于人物定妆图中；先建立独立 Costume 资产，再生成依赖 Character + Costume + Makeup/Hair 的 `COMBINED_LOOK`。
- 服装合同除颜色和轮廓外，还要锁定层次、版型、织物/甲片结构、垂坠或硬挺、光泽、缝线扣合、磨损位置，以及动作、风、雨和灯光下的表现。
- 对会在近景出现或跨镜复用的布料、金属、皮革、木材、纸张、甲片、刺绣、磨损与污渍建立 Material Detail Plate，记录尺度和位置，不用均匀“做旧”代替真实材料。
- 历史或文化资产按 DOCUMENTED / RESEARCH-INFERRED / CREATIVE / UNKNOWN 标记。
- 未获授权的商标、人物肖像与可识别 IP 元素不得进入资产。

## Generation boundaries

- 可以为静态资产编写执行所需的图片提示词；生成前先向用户展示，执行后再保存到 generation log，不回写 Visual Bible。
- 不生成镜头图片、分镜、Hero Frame 或 Keyframe；这些属于后续阶段。
- 不生成视频或视频 Prompt。
- 不为了让模型“更稳定”改变 LOCKED 身份、证据边界或文化含义。
- 不把一次生成成功当作跨视图、跨状态连续性已经通过。

## Completion gate

- manifest 中每个资产都有唯一 ID、版本、路径和状态；
- 核心资产的 locked features 与 Visual Bible 一致；
- 所需视图和状态有用途依据且齐全，延期/不需要项及启用条件明确，不默认全套六视图；
- 真实图片已逐张审核或由用户明确批准并登记范围，或明确仍处于 PLANNED；
- 历史/文化依据和原创部分分层；
- 生产级 Scene Design 所需 P0 用途、视图与状态均有确切批准范围，单帧批准不外推整套；文本交付可继续明确标待验证的草稿；
- 实际使用检查与批准艺术规则相符，不能由一张好图推定复杂接触、最终镜头或跨视图全部通过；
- 没有越界生成镜头、分镜或视频 Prompt。
