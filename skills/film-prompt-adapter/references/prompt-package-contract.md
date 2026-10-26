# Prompt Package Contract

## Profile status

- `VERIFIED`: 当前官方来源或用户提供的权威 profile 可追溯。
- `USER_PROVIDED`: 用户明确给出能力和参数，尚未独立核实。
- `UNVERIFIED`: 无可靠当前依据；不得进入 Generation。
- `STALE`: 资料版本或日期不足以支持当前执行。

## Package status

- `CONTENT DRAFT`：内容交付，允许明确待补媒体/用途批准/能力验证；不可提交生成，不代表源合同或模型通过。

- `READY FOR GENERATION`
- `MODEL VERIFICATION REQUIRED`
- `CREATIVE INPUT RETURN`
- `INCOMPATIBLE — USER DECISION`

Package Identity 记录 Delivery Boundary / Scope。CONTENT DRAFT 的 Unit Card 使用现有 NOT_READY，依赖项另记 WAITING_DEPENDENCY，不新创执行状态。草稿可完整交付文字，引用待补逻辑别名但不伪造真实文件/槽位。生产状态按单元范围汇总；混合就绪与待补的包不整体标 READY FOR GENERATION，逐 Unit 显示具体阻断项。

## Required sections

1. `Package Identity`
2. `Model Profile Receipt`
3. `Source Version Lock`
4. `Input File Map`
5. `Prompt Units`
6. `Prompt Coverage Receipt`（每个 Unit）
7. `Compatibility & Degradation`
8. `Reverse-check`
9. `Generation Order`
10. `Decision Register`
11. `Next Stage`

另含 Intent Preservation Map 与 Prompt Review；十三项回执继续沿用原枚举，不新增平行批准来源。

每个 Unit 还必须记录 `Source Freshness: CURRENT / STALE / BLOCKED / RECOMPILE`。只有 `CURRENT` 可以进入生成；`RECOMPILE` 必须先依据当前源合同重新输出 Package 与执行卡。

项目采用 Method 时，Package 记录 `Method ID / Version / Adoption Scope / Controlled Fields / Protected Project Fields / Validation Status`。只编译当前 Unit 范围内的 Method 模块；多个 Method 对同一字段未裁决时标 `CONFLICT`，候选 Method 只能进入 TECHNICAL_PILOT。

## Integrated storyboard-prompt delivery view

面向用户、导演和生成执行者的默认可读交付不得要求在多份文件之间来回对照。除结构化底层合同外，还应输出一份整合视图，顺序固定为：

1. 全段标准分镜总表；
2. 按场景放入已批准的人物站位/路径图与机位/轴线叠加图（适用时），注明 ID、版本、适用镜头及未知边界；
3. 按镜号依次展开；
4. 每镜先给标准分镜字段；
5. 紧接该镜 Reference `@` Binding Map；
6. 紧接该镜完整关键帧/编辑 Prompt（如适用）；
7. 紧接该镜完整视频 Prompt 或目标模型 Prompt；
8. 最后给该镜排除项、连续性输出和验收点。

不得把所有镜头的绑定表集中在前面、所有 Prompt 集中在后面，迫使执行者跨页匹配。结构化源合同仍可分文件保存，但整合视图必须保留精确 Frame/Asset ID、路径、版本、逻辑别名、上传顺序和 Prompt 全文；不能只链接到另一文件或用“同上”省略。

整合视图的执行标签统一为：

- `操作｜参考图与关键帧 @绑定`：按表上传和选择输入槽，不复制表格。
- `直接复制｜关键帧主提示词`：复制到图片生成或编辑主提示词框。
- `直接复制｜视频主提示词`：复制到视频模型主提示词框。
- `直接复制｜负向提示词`：平台有独立负向栏时复制；没有时只把高风险约束压缩追加到主提示词末尾。
- `不要复制｜生成后验收`：只用于人工或 Agent 检查结果，不发送给模型。

`USER_GENERATE` 的整合视图还应适合逐卡复制到无限画布：一镜/一 Unit 一卡，卡首标 ID、目标文件名、依赖状态与回传 ID；参考图操作、平台参数、主提示词、负向提示词、验收与回传各自独立。只复制提示词区的连续正文，不能把 Markdown 表格、路径或验收文字混入模型输入。依赖真实图片或 Take 的卡在收到并审核前标 `WAITING_DEPENDENCY`。

手动包的首页必须列批次执行顺序、可并行 Unit、前置批准依赖与返工回路；每张卡在提示词前提供编号操作步骤：检查 READY、选择已核实的平台入口、按 Upload Order 放参考图、设置外部参数、复制主/负向提示词到对应输入栏、生成并按 Unit/Take ID 保存、回传原文件。用户可同时明确说“审核通过”，则按其范围直接入库和解锁依赖；未给审核结论时等待 Codex QC。平台入口、槽位或参数未知时标 `MODEL VERIFICATION REQUIRED` 并说明待确认项，不写猜测性点击路径。

Prompt 中的逻辑别名必须在执行前替换为平台真实 `@图1 / @Image 1 / slot`；若平台以首帧/尾帧专用槽完成绑定，则使用专用槽并保留简短职责句，不把文档路径复制给模型。

整合视图以 `Production Unit Card` 为最小执行单元。它是编译产物：可以汇总 Shot、Frame、Motion、Prompt、风险与验收，但不得成为动作、资产状态或镜头事实的唯一来源。用户在卡片上提出内容修改时，先把差异回写到最早责任合同，再重新编译；只改措辞且不改变语义时可以直接 `RECOMPILE`。

每张卡必须显式展示 `MAIN / SUPPORT / HOLD` 和 `PREVIOUS RESIDUE → TRIGGER → DELAY → VISIBLE CHANGE → HANDOFF`。Prompt 可按模型语法压缩这些字段，但验收区必须保留完整链条，便于判断模型是否遗漏延迟反应、误动 HOLD 对象或抢走主要注意力。

`Generation Order` 必须区分 `TECHNICAL_PILOT` 与 `PRODUCTION`。存在 REQUIRED Pilot 时，Production Units 可以先完成编译，但不得被标为可批量执行，直到 Pilot QC 返回 `PILOT_VALIDATED` 或用户明确接受记录在案的风险。

状态变化 Unit 还必须先于其依赖 Unit。依赖 Unit 可以预编译，但只有关键状态的真实 Frame/Take 形成 `Actual Observation` 并通过相应审核后，才标为 `READY FOR GENERATION`；实际观察与计划不一致时重编译依赖 Unit，不倒改已批准主合同。

## Parameter provenance

每个参数标记：

- `USER_LOCKED`
- `OFFICIAL_PROFILE`
- `ADAPTER_DEFAULT`
- `OPEN`

Adapter Default 只能用于低风险执行值，并必须处于官方允许范围。

## Model profile receipt

至少记录：Provider、Model/Version、Official Source、Access Date、Profile Status、supported input modes、duration/aspect/resolution limits、reference count and semantics、first/last-frame support、audio/dialogue/lip-sync/text support、negative-prompt behavior、required prompt schema、external parameters、async/result behavior、account/region differences 和 unknowns。未核实字段保持 UNKNOWN，不用自然语言Prompt伪装支持。

同时记录 Platform / Task Entry / API or UI Route / Account-Region Scope 与逐项能力来源；同名模型的不同入口不得共用未经核对的能力结论。USER_PROVIDED 标提供者和限制，不自动升级成独立核实；来源不清的控制项保持待核实。Profile 证明接口能力，不能证明当前镜头效果。

## Reference role and binding map

每个输入文件登记：upload order、path、version、role、approval scope、allowed influence、must not override、platform slot/token、prompt binding text 和 required/optional。角色语义必须来自已核实模型Profile；不能假设“图1”在所有模型中都代表人物身份。对视频输入另记 `START / MID / END / REFERENCE`；对 STYLE 输入保留原始风格锚点，避免只沿上一张生成图累积漂移。

同一 Frame Contract 中的模型无关绑定语义必须保留；Adapter 只负责把它翻译为当前入口的 `@Image 1`、`[图1]`、有序媒体数组或其他已核实语法。上传顺序、平台标签和 Prompt 中的编号必须一一对应。

### Logical `@` aliases

Prompt Package 先使用不会随平台变化的逻辑别名，再由当前 Model Profile 编译为真实槽位：

- `@IDENTITY_<asset-id>`：只锁人物脸部、年龄和可辨认身份。
- `@WARDROBE_<asset-id>`：只锁服装、甲胄、妆发或穿戴状态。
- `@SCENE_<asset-id>`：只锁空间拓扑、建筑、陈设、材质与既定光源。
- `@PROP_<asset-id>`：只锁道具形制、尺寸、材料和当前持用状态。
- `@GROUP_<asset-id>`：只锁群体的时代服饰、比例范围、密度与批准的行为边界；不得复制具体人数和脸。
- `@STYLE_<reference-id>`：只提供色彩、质感、景深或摄影倾向；不得覆盖项目事实。
- `@POSE_<reference-id>`：只提供姿态、构图或主体关系；不得传递身份、服装和背景。
- `@STATE_<reference-id>`：锁定一张编辑母图的当前可见状态；只有 Prompt 明确列出的字段允许改变。
- `@START_<frame-id>`：视频 0 秒的完整可见状态；动作必须从该状态之后继续。
- `@MID_<frame-id>`：中间动作检查点；除非 Profile 明确支持，不得冒充首帧输入。
- `@END_<frame-id>`：目标结束状态；不得把尾帧已有动作重复写成开场动作。
- `@MOTION_<reference-id>`：只提供动作、节奏或运镜；不得覆盖人物和场景外观。

逻辑别名不是模型天然认识的语法。每个执行包必须提供 `Logical Alias → Upload Order → Platform Token/Slot` 映射；未验证平台语法时，Platform Token 保持 `UNKNOWN`，不得声称 `@图1` 一定生效。

### Binding sentence contract

每个 `@` 引用必须用一句可复制绑定句同时回答：

1. **Frame/asset role：** 它是身份、服装、场景、道具、风格、姿态、START、MID、END 还是 MOTION；
2. **Allowed influence：** 画面中具体控制哪些对象、字段或时间点；
3. **Permitted change：** 当前任务允许从参考图改变什么；
4. **Must not transfer/override：** 参考图中的哪些人物、背景、构图、旧状态、文字、水印或时代错误绝不能带入。

推荐句式：

> 以 `@START_SH03` 作为视频 0 秒完整画面，锁定机位、构图、人物/道具位置和触水前状态；只允许按时间线推进动作，不得重画身份、服装或场景。以 `@END_SH03` 只作为 1.5 秒动作终点，锁定一次踏水后的水花形态；不得把其水花复制到 0 秒或再次触发第二次踏水。

### Reference precedence

发生冲突时按字段裁决，而不是笼统声明“图 1 优先”：

1. 当前 `START / END` Frame 控制对应时间点的构图、位置、状态和光线；
2. `IDENTITY / WARDROBE / SCENE / PROP / GROUP / STATE` 分别控制自己的专属字段；
3. `POSE / MOTION` 只控制姿态、动作或摄影机；
4. `STYLE` 只能影响未被硬锚点锁定的摄影表达；
5. Prompt 文字只补充参考图未承载的信息，或执行明确登记的局部状态修改。

若两张硬锚点对同一字段给出冲突状态，必须标 `CONFLICT` 并返回，不能通过多写几个 `@` 让模型自行选择。

## No phantom files

每个 reference path 必须能由当前工作区、工具返回或用户附件证明存在。URL 不等同于本地上传成功；缺失文件使对应 Prompt Unit 阻断。

此规则阻断执行，不阻止 CONTENT DRAFT 文本交付；计划参考写待补与启用条件，不将伪路径放入已验证输入表。真实文件存在仍需核对确切版本及用途批准。

## Look, atmosphere and rhythm inheritance

Unit 同时记录 Viewing Stance / Information Alignment、Must Read/Withhold、Composition Relations、Input Use（CURRENT START / TARGET END / REFERENCE ONLY）及 Presentation Mode / Artistic Rule IDs-Version / Layer / Change or HOLD。Input Frame Role 与实际用途不同：END 作目标不当开场，MID/END 作起点不重播。持续/保持依据继承 Motion，不强制新触发；非物理层独立于真实空气，不统一改成写实材质/运动。

每个视频 Unit 记录上游 `Narrative Look Arc / Scene Look & Light State / Atmospheric Medium State / Rhythm Role / Required Hold`。空气介质必须保留来源、分布、驱动力和受光方式；没有定义时不补通用雾或粒子。模型时长或时间线控制不足以保留必要反应/静默时，标 `UNSUPPORTED / CONFLICT` 并拆 Clip、降级或返回，不能静默压缩。

## Applied generation patterns

若使用公共 Pattern Catalog，每个 Unit 记录 `Pattern ID / Status / Evidence Level / Model-Version-Entry-Mode Match / Shot-Risk Scope Match / Last Verified / Applicability Decision`。`LOCAL_OBSERVATION / PROJECT_VALIDATED` 不得冒充跨项目规则，`REVIEW_REQUIRED / CONTRADICTED / RETIRED` 不得默认应用。Pattern 只能帮助选择表达或测试假设，不能覆盖 Profile、上游合同、Coverage Receipt 和 Pilot Gate。

## Prompt coverage receipt

Intent Preservation Map 记录 Protected Intent / Source ID-Version / Carrier / Target Location / Status / Gap；保护观看立场、构图、注意、必要保持和结束状态，Status 沿用下方回执枚举。图像承载的内容须有实际输入角色依据，不能只看 Prompt 文本误判缺失。

每个 Prompt Unit 用固定十三项回执证明信息去向：Reference anchors、Overall concept、Dynamic description、Image texture/cinematography intent、Shot language、Scene、Color/style、Light、Composition、Emotion/observable performance、Shot timeline、Sound、Exclusions。

每项状态只使用：

- `MAPPED`：已进入可复制 Prompt 或已核实的外部参数/输入槽；
- `NOT_APPLICABLE`：本任务确实不需要；
- `UNSUPPORTED`：目标模型不支持，必须写降级或后期去向；
- `CONFLICT`：来源合同或目标能力冲突，不得静默选择；
- `RETURN`：缺少或错误的上游合同阻断执行。

同时记录 Source Contract、目标 Prompt/参数位置和说明。回执是审计接口，不得原样拼进 Copy-ready Prompt；模型不支持的声音、负向提示或控制项不能用自然语言伪装为已支持。

## Prompt review and release

Prompt Review 使用 PASS / REVISE / NOT_EVALUATED，列 Covered Units、Evidence & Findings、Blocking Issues / Owner、Pending Pilot Validation。逐项核对语义保留、绑定/槽位对应、角色与时长、艺术规则、支持边界；反查对象为 Prompt + 实际参考/职责/上传顺序 + 已核实控制项。未核实的维度不写 PASS，用户已有批准按范围记录，不虚构检查。

Fallback 记录 Unsupported Field / Alternative / Expression Cost / Source Permission / Pending Validation。不得自行改变锁定机位、动作、停顿或艺术规则；有变化返回责任上游，不能只加词伪装支持。

READY FOR GENERATION 的 Unit 须源版本 CURRENT、批准用途和真实必需依赖齐备、Profile VERIFIED、Prompt Review PASS、十三项回执无未解决 CONFLICT/RETURN，UNSUPPORTED 有获准去向；Pilot/关键状态依赖继续按原门处理。草稿完成不等于执行放行，文本审核不证明模型效果。
