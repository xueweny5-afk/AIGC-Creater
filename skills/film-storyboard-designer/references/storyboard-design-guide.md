# Storyboard Design Guide

## Script-to-board coverage

在挑选分镜帧前，先把上游决定编译成一张按剧本顺序排列的覆盖表。它回答两个问题：剧本是否都有镜头承接；每个需要视觉证明的镜头是否都有合适的 Frame。

每行至少包含：

- Source Scene / Beat / Script Range
- Shot ID 与顺序
- Narrative Function
- 景别 / 角度 / 构图与屏幕方向
- 人物与道具动作阶段
- 镜头运动的 start / trigger / path / end 或 `STATIC`
- Dialogue / Sound / Silence / Bridge
- Planned Duration / Cut or Handoff
- Representative Frame IDs
- Coverage Status / Return Reason

表格中的景别、构图、动作、运镜、声音和时长都是 Shot List 的只读摘要。分镜阶段只能补 `Frame IDs / Coverage Status / Review Evidence`；任何上游字段不清、互相矛盾或无法静态预演时，返回 Shot Design。

### Coverage status

- `MAPPED`：剧本内容已映射到 Shot，所需 Frame 已规划。
- `FRAME_READY`：代表 Frame 实际存在并通过单帧审核。
- `SEQUENCE_PASS`：相邻帧与声音顺序审核通过。
- `NO_STATIC_FRAME_REQUIRED`：声音 Bridge、离画动作或其他内容不需要独立画面，理由已写明。
- `MISSING_SHOT`：剧本内容没有 Shot 承接。
- `MISSING_FRAME`：Shot 需要静态证明但没有 Frame。
- `CONFLICT`：剧本、Shot、连续性或声音摘要互相矛盾。
- `RETURN_SHOT`：必须返回镜头设计处理。

Coverage 不是“每句剧本一镜”或“每镜一帧”。一句动作可能需要多个 Shot，一个 Shot 也可能承载动作、反应与声音；关键是叙事信息、状态变化和声音落点都有可追溯去向。

## Readable storyboard sheet

面向导演、客户或制作审阅的分镜页应把图片和执行摘要放在一起，但保持层级清楚：

1. 代表 Frame 或 `NOT_GENERATED` 占位；
2. Shot ID / Frame ID / 来源剧本节拍；
3. 景别、角度、构图和画面关注点；
4. 当前 Frame 锁定的单一瞬间；
5. Shot 级人物动作阶段、镜头运动和声音；
6. 时长、切点/交接、连续性与审核状态。

镜头运动属于 Shot 摘要，静态 Frame 只证明其中一个时刻。不要用箭头、速度线或在一张图中叠加多个姿态来伪装完整运动；运动细节仍由后续 Motion Design 负责。

## One frame, one instant

代表时刻先回答 Audience Read：观众此刻主要读到谁、什么关系/信息/感知，为什么选动作前、回应中、后果、等待或保持。继承 Shot 的 Viewing Stance 与 Must Read/Withhold，不为了突出表情而改变已批准景别、机位或行为。无新动作的静止也可成立；不强制每帧都处于动作高潮。

静态画面不能同时展示动作开始、过程和结束。每帧说明：

- 前一刻是什么；
- 当前锁定哪一瞬间；
- 下一刻将由什么触发。

若一个 brief 使用“同时、随后、然后、最终”串联多个状态，应该拆帧或留给 Motion Design。

## Frame economy

- 单一稳定构图和简单动作：一个 Board 通常足够。
- 构图稳定但动作结果决定下一镜：Board + End Keyframe 或一帧兼任。
- 明显摄影机位移、复杂人物接触、道具状态改变：Start + End，必要时加 Intermediate。
- Hero Frame 只选择主题和方向审批价值最高的画面。

## Continuity projection

先投影 Shot 的主体占比/位置、人物间距、深度层或平面关系、负空间、遮挡与视觉重心；构图预演先验证主要注意对象与必要关系，再处理细节。低细节布局只批准构图，不批准身份、服装、光色或艺术风格；正式帧继承源合同。相邻状态参考和原始资产共同约束，回锚不等于重做已批准帧。

从 Shot Ledger 继承世界坐标，再计算当前画面：

- 角色在画面哪侧、朝向谁；
- 离画人物的视线方向；
- 道具由谁持有、是否接触、是否越过边界；
- 固定场景锚点是否与相邻画面一致；
- 光源方向、时间与阴影是否连续。

不要移动房间或镜像资产来修正画面。

## State pair check

同镜 Start / Intermediate / End 记录 `Frame IDs & Versions / Facing & Gaze / Hand-Prop & Contact / Action Phase / Camera State / Planned Change & Preserved Anchors / Static Evidence / Pending Motion Validation`。每帧的摄影机位置依 Shot 的该时刻路径，不机械保持完全相同构图。首尾能对上只证明静态状态；接触转移、速度、遮挡和形变的中间过程交 Stage 12 设计、Pilot/生成验证。不为简单单帧强建首尾对。

## Visual review

先看正确性，再看审美：

1. 同一人物/地点/道具吗？
2. 构图和轴线投影正确吗？
3. 身体、手部、接触与重量合理吗？
4. Must Show 可见吗？Must Avoid 是否出现？
5. 相邻帧能否无解释地按顺序理解？
6. 是否存在文字、水印、额外物件或背景竞争？

Frame Review 分别记 Correctness、Expression & Artistic Rule 的 PASS / REVISE / NOT_EVALUATED，附可见证据、问题字段及责任层。注意力、关系或意象未读出时不能只凭材质漂亮通过；批准的平面化、变形或象征效果按 Presentation Mode / Artistic Rule IDs 检验，不强制现实材质或物理空间。静态图只能证明可见快照，不能证明完整呼吸、倾听或速度。

## Sequence read and evidence

先不看说明检查纯视觉的主体、方向和状态承接，再用计划对白/声音判断完整信息；静态图无须单独解释离画声或全部心理。倒叙、并置、梦境及意象转换继承 Shot 的转换依据和保持项，不把刻意非连续修成线性匹配。Sequence Review PASS 需真实顺序画面证据；文字计划只记 PLANNED，单帧批准不覆盖全段。

## Content delivery and animatic boundary

PLAN_ONLY/HANDOFF 可交完整文本与待补参考/构图图计划；缺必需真实图时卡片标 WAITING_DEPENDENCY，不伪造路径，不阻止内容交付。实际执行 GENERATE 或将卡片标可执行时才要求对应批准依赖齐备。Frame Review、Sequence Review 和 Animatic 各自记范围与证据，用户批准未评估维度保持 NOT_EVALUATED。

Animatic Plan Review 用 PASS / REVISE / NOT_EVALUATED，只验证时间与声画安排。实际预览未渲染保持 NOT_RENDERED；REVIEWED_PASS 必须对应确切预览/版本的完整播放审核，或用户对该预览明确批准。多镜段落生产放行不能用计划 PASS 替代播放；单镜不适用时记 NOT_APPLICABLE 和理由，不强建空预览。静态 Animatic 也不证明运动插值或视频模型能力。

## Self-audit

- 是否为每镜机械生成两张？
- 是否把多个时间状态塞进一张？
- 是否用箭头和文字解释失败画面？
- 是否把美图误当成故事板？
- 是否在没有查看实际图片时标记通过？
- 是否提前写视频运动或最终 Prompt？
- 是否有剧本内容没有 Shot、或有 Shot 没有必要 Frame？
- 是否把 Shot 级动作过程误画进单一静态 Frame？
- 是否在总表中修改了上游镜头决定，却没有返回 Shot Design？
