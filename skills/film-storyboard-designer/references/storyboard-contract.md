# Storyboard Contract

## Script-to-shot-to-frame coverage

`storyboard-plan.md` 必须包含按剧本顺序排列的覆盖表。每行字段：

- Order / Source Scene / Beat / Script Range
- Shot ID / Narrative Function
- Framing / Angle / Composition / Screen Direction
- Character & Prop Action Phases
- Camera Movement: start / trigger / path / end or STATIC
- Dialogue / Sound / Silence / Bridge
- Planned Duration / Cut or Handoff
- Representative Frame IDs
- Coverage Status: `MAPPED / FRAME_READY / SEQUENCE_PASS / NO_STATIC_FRAME_REQUIRED / MISSING_SHOT / MISSING_FRAME / CONFLICT / RETURN_SHOT`
- Review Evidence / Return Reason

除 Frame IDs、Coverage Status、Review Evidence 和 Return Reason 外，其余字段只读继承 Screenplay、Shot List 与 Continuity Ledger。摘要不一致时以上游合同为准并标 `CONFLICT`，不得在分镜表中静默改写。

## Board states

- `PLANNED`
- `GENERATED_PENDING_REVIEW`
- `REWORK`
- `READY FOR MOTION DESIGN`
- `USER-APPROVED`
- `REJECTED`

只有实际图片经过审核后才能 READY；用户对确切 Frame 明确说审核通过时可直接记 `USER-APPROVED`，无需 AI 再做像素审核。记录文件路径、Frame ID、版本、批准范围和人工来源；单帧批准不自动扩大到整段顺序或 Animatic。

内容交付继承范围和上游版本，PLAN_ONLY/HANDOFF 的文字、参考和构图图计划可在媒体待补时完成，Board 保持 PLANNED，不把占位符当批准图片。生产就绪检查当前所需资产的确切文件/版本/用途/视图/状态是否在 Approval Scope 内，不以资产总体 APPROVED 外推。

## Frame types

- `BOARD`
- `HERO_FRAME`
- `START_KEYFRAME`
- `END_KEYFRAME`
- `INTERMEDIATE_STATE`

一帧可以同时是 BOARD + START_KEYFRAME，但必须在合同中写清用途。

## Required frame fields

- Frame ID / Source Shot ID
- Source Scene / Beat / Script Range
- Type / Status / Version
- Represented Instant
- Audience Read / Instant Selection Basis / Previous State / Next Handoff
- Viewing Stance / Must Read / Must Withhold / Source Composition Relations
- Narrative Function
- Frame Earning Reason
- Dramatic Read: subject / relation, perception or consequence / visible action or HOLD
- Aspect Ratio
- Delivery Variants / Protected Subject & Text Safe Region / Crop or Recomposition Rule
- Asset IDs and versions
- Reference roles: STYLE / IDENTITY / WARDROBE / TOPOLOGY / POSE / STATE
- Reference Input Map: slot/label / exact path / version / role / allowed influence / must not transfer / prompt binding / required
- Composition Guide ID / Version / Type / Status / Exact Path / Allowed Influence / Must Not Transfer，或具体 `NOT_NEEDED` 理由
- Image Generation Brief: subject / represented instant / composition / camera intent / light / material / continuity locks / exclusions
- Depends On / State Changes / Affected Dependents
- World Position / Axis Projection
- Composition & Depth
- Visible Character / Prop State
- Observable Performance Snapshot: posture / weight / gaze / breath-pause / hand-prop / costume-hair response
- Scene Look & Light State ID / Version
- Narrative Look Arc ID / Atmospheric Medium State
- Rhythm Role / Required Hold
- Look / Light Deviation & Trigger
- Presentation Mode / Artistic Rule IDs & Versions / Layer / Trigger / Preserved Features or HOLD
- Light / Time State
- Continuity In / Out
- Must Show / Must Avoid
- File Path
- Review Evidence and Results
- Frame Review: Correctness / Expression & Artistic Rule（PASS / REVISE / NOT_EVALUATED）, Evidence / Issues / Return Layer
- Actual Observation / Approval Scope
- Source Versions / Freshness: `CURRENT / STALE / BLOCKED / RECOMPILE`
- Attention & Response Snapshot: `MAIN / SUPPORT / HOLD / PREVIOUS RESIDUE / TRIGGER / DELAY / VISIBLE CHANGE / HANDOFF`

## Contact sheets

多格故事板、宫格和 Animatic Contact Sheet 可以作为顺序审阅派生物，但必须能回到独立 Frame ID、原图路径和版本。Contact Sheet 不能成为唯一生产资产，也不能因整体看起来连贯而跳过单帧身份、肢体、空间和文字检查。

## Composition Guides

Composition Guide 位于正式 Frame 之前，只解决机位、景别、主体占比、画面位置、前中后景、负空间、遮挡和屏幕方向。ID 使用 `S005-SH01-CG01`，目录为 `storyboard/composition-guides/<composition-guide-id>/`。

每项必须记录：`Guide ID / Source Shot / Target Frame IDs / Type / Status / Version / Aspect Ratio / Camera & Framing / Subject Blocks / FG-MG-BG / Negative Space / Occlusion / Screen Direction / Exact Path / Allowed Influence / Must Not Transfer / Review Evidence`。

类型为 `EXISTING_SOFT_REFERENCE / CLEAN_SCENE_BLOCKING / GRAYSCALE_LAYOUT / NOT_NEEDED`；状态为 `PLANNED / GENERATED_PENDING_REVIEW / COMPOSITION_APPROVED / REWORK / NOT_NEEDED`。复杂或关键 Frame 未绑定批准 Guide 时不得生成。Composition Guide 不锁人物身份、服装、美术细节、最终光色和道具版本，不进入资产 manifest、Animatic 或图生视频首帧。

## Sequence review and animatic gate

同镜存在多个关键状态时，附 State Pair Check：`Frame IDs & Versions / Facing & Gaze / Hand-Prop & Contact / Action Phase / Camera State / Planned Change & Preserved Anchors / Static Evidence / Pending Motion Validation`。无多状态需求写 NOT_APPLICABLE 及理由。静态通过不代表运动可行或模型已验证；不要在本阶段补写完整 Motion Spec。

包含两个及以上镜头的场景或段落必须输出 `sequence-review.md`，按顺序记录相邻 Frame 的身份、位置/朝向、视线、表演状态、道具、环境/材质状态、光线、动作相位和声音交接。顺序 Contact Sheet 可以作为证据路径，但不能替代逐帧审核。

有 Scene Orientation Card 的场景在 SPATIAL READ 引用 Card ID / Version，先不读说明检查可见区域、方向和状态，再核对 Shot 的机位叠加图。若原图未落实正确合同则返工 Frame；若合同本身有空间缺口则返回 Shot/Scene，不移动地标补救。艺术空间和有意非连续按批准规则审核；完整含义依赖声音时结合声音判断，不强求纯视觉解释离画声或全部心理。

进入 Motion Design 前建立 `animatic/animatic-plan.md`：每个 Frame 的顺序、计划时长、对白/临时声音、声音 Bridge、切点理由和累计时长，并增加 Rhythm Map：`story pressure / action-information density / visual energy / sound energy / required hold-reaction-silence / shift trigger`。实际预览存在时记录路径与完整播放结果；无法渲染时标 `NOT_RENDERED`，不得声称已观看。Animatic 只验证节奏与叙事，不定义连续运动或模型 Prompt。

Sequence Review 单列 Result（PASS / REVISE / NOT_EVALUATED）、Covered Frame Versions、Evidence、Issues / Return Layer；计划阶段未查看顺序图不填 PASS。Animatic Plan Review 同样记 PASS / REVISE / NOT_EVALUATED，和预览状态 PLANNED / NOT_RENDERED / RENDERED_PENDING_REVIEW / REVIEWED_PASS / RETURN 分开。REVIEWED_PASS 仅在确切预览完整播放审核或用户明确批准该预览后使用；用户仅批准计划不能算预览通过。多镜生产放行须单帧范围、Sequence Review 与实际 Animatic 审核满足要求；单镜不需多镜 Gate 时在 Applicability 写 NOT_APPLICABLE 与理由，不新增预览状态。

## Format adaptation

主画幅是 Frame 合同的一部分。已知存在横/竖或其他交付变体时，逐帧记录受保护主体/文字安全区、允许裁切范围以及 `CROP SAFE / REFRAME / RECOMPOSE REQUIRED`；需要重构图的变体不得延迟到最终导出阶段强裁。

## Reference input map

每帧列 Reference Input Map，不只写 Asset ID。Prompt Binding 使用模型无关语义，如“图 1 只锁身份，图 2 只锁服装”；平台语法由 Prompt Adapter 编译。计划/HANDOFF 草稿允许待补文件与依赖，标 WAITING_DEPENDENCY；必需真实文件、用途批准或 Composition Guide 尚未满足时不得标执行就绪或实际生成，但不阻止文本交付。Frame 继承 Look Arc、Look/Light、Atmospheric Medium、Rhythm Role 与独立艺术规则，偏差有对应依据；真实空气记物理驱动，艺术层不冒充空气。

每条 Reference Input 还必须有稳定逻辑别名：`@IDENTITY_* / @WARDROBE_* / @SCENE_* / @PROP_* / @GROUP_* / @STYLE_* / @POSE_* / @STATE_* / @START_* / @MID_* / @END_* / @MOTION_*`。分镜阶段只声明模型无关职责，不假设平台认识这些字符串；Prompt Adapter 负责把别名翻译成当前入口真实的 `@图1`、`@Image 1` 或输入槽。

关键帧在画面中的职责必须明确：

- `START_KEYFRAME`：锁定 0 秒完整可见状态；后续 Prompt 从它之后开始，不重复首帧已有动作。
- `END_KEYFRAME`：锁定结束时间点；不得被当作开场状态或让模型重复完成尾帧动作。
- `INTERMEDIATE_STATE`：锁定动作中间的接触、比例或空间检查点；模型不支持中间帧控制时只用于 QC，不伪装成有效输入。
- `BOARD`：说明镜头代表瞬间和构图，可作为生成参考，但不自动等于视频首帧。
- `HERO_FRAME`：说明宣传或段落代表画面，只提供批准范围内的视觉目标，不自动定义运动起点。

每条 Prompt Binding 必须明确：控制对象、允许影响、允许修改、禁止迁移。不得只写“参考图 1”或“参考附件”。

## IDs

使用 `S005-SH01-F01`。新增帧使用后缀，不重编号已引用的帧。

## Review evidence

- `NOT_GENERATED`
- `SELF-REVIEWED`
- `USER-APPROVED`

结构化合同不构成像素证据。

Frame Review 分开检查正确性与表达/艺术规则，记录具体可见证据；用户已批准范围按人工来源登记，未逐项评估保持 NOT_EVALUATED，不虚构 AI 检查或扩大批准。静态图无法证明的时间过程写入待验证项。

## Approval and dependency rules

- `APPROVED` 帧记录批准范围：`FULL FRAME / STYLE ONLY / IDENTITY ONLY / COMPOSITION ONLY / STATE ONLY`。
- 已批准源图不可被静默覆盖；失败帧创建新版本，只重新检查受影响依赖。
- `STYLE ONLY` 校准帧若包含过期人物、道具或空间状态，不得把这些状态传给新帧。
- `STATE-CHANGE CRITICAL` 帧审核后才允许将 `Actual Observation` 传给依赖帧。
- 每个 Frame 保留独立源图；Contact Sheet 不作为唯一资产或图生视频输入。
- 上游 Shot、Asset、Look/Light 或状态版本变化时，先将受影响 Frame 标为 `STALE` 或 `RECOMPILE`；不得只修改 Contact Sheet 或整合提示词手册来掩盖源合同差异。
