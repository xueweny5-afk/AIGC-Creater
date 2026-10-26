# Motion Spec Contract

## Status

- `MOTION EXPLORATION`
- `READY FOR PROMPT ADAPTATION`
- `RETURN TO STORYBOARD`
- `RETURN TO SHOT DESIGN`

MOTION EXPLORATION 可完整交付内容稿并进入提示词草稿编译，依赖与待验证项明示，不具生产执行资格。READY FOR PROMPT ADAPTATION 要求 Motion Review PASS、当前范围上游/用途批准证据齐全且无阻断项；不代表实际运动、模型或 Pilot 通过。用户单帧批准只覆盖其范围，不替代适用序列/Animatic Gate。

## Motion layers

1. Body / posture / weight / locomotion
2. Face / gaze
3. Breath / voice / pause
4. Hands / prop contact
5. Costume / hair physical response
6. Camera position / orientation / focal behavior
7. Environment / background people / particles
8. Atmospheric Medium State / physical source / distribution / driver / HOLD or triggered change
9. Scene Look & Light State inheritance and light / weather / time-state changes
10. Dialogue / lip-sync / sound-linked action

采用非物理艺术规则时另列 Artistic Motion Layer：Presentation Mode / Artistic Rule ID & Version / Layer / Trigger or Continuation Basis / Change Process / Preserved Features。真实物体与空气仍按物理依据；非物理层不强制现实作用力，不扩大到未批准身份、空间或故事变化。

不动的层写 `HOLD`，防止下游模型自行增加无意义动作。

情绪通过可观察的进入状态、变化或持续/保持与退出状态承接；不强制每镜新触发或转折。眨眼、呼吸、头发或衣摆运动仅在批准表演节奏、物理作用或艺术规则需要时启用，不随机填充生命感。Look/Light 默认继承，无批准依据不得改变。

每个 Clip 继承 Animatic/Shot 的 `Rhythm Role / Required Hold`。Atmospheric Medium 没有来源和驱动力时保持 `NONE / HOLD`；不得用粒子运动填补没有动作的时段。

每个 Clip 同时继承 `MAIN / SUPPORT / HOLD` 与 `PREVIOUS RESIDUE → TRIGGER → DELAY → VISIBLE CHANGE → HANDOFF`。Motion 负责把已批准链条分配到时间段和运动层，不负责新增人物动机。`HOLD` 对象若因物理作用必须变化，应明确触发与允许幅度。

Motion Spec 记录上游版本和 freshness：`CURRENT / STALE / BLOCKED / RECOMPILE`。`STALE / BLOCKED` 不得进入 Prompt Adaptation；只因上游版本号变化而内容等价时，经差异核对后可 `RECOMPILE`。

## Phase notation

每阶段包含：

- Time range
- Active layer
- Action
- Speed / acceleration
- Contact / physics
- Attention priority
- Resulting state

时段可以使用整秒或合理区间，不要求逐帧数据；总和必须闭合。

Phase Timeline 以连续不重叠的主时间段覆盖 Planned Duration；同段内各层可并行，不将并行时长相加。每段另记 Attention Lead / Support-HOLD / Camera Coordination / Handoff，允许批准的同步运动；静止写观察/等待作用。Timing Audit 记录 Method / Scope / Planned Duration / Phase Total / Dialogue-Sound Fit / Required Holds / Difference / Result（PASS / REVISE / NOT_EVALUATED），计划估时不冒充实测。

## State connection and contact

State Connection Plan 记录 Known Start / Planned End、Mandatory Checkpoints、Preserved Anchors、Static Evidence、Pending Motion Validation。引用 Stage 11 状态对及确切版本；无尾图但已有批准结束状态时写 PLANNED END STATE，不强制新增帧。若生产输入模式必需尾图，由 Prompt Adapter 标具体执行依赖，不能倒改 Motion Master。

Contact Checkpoints 按需记 Phase / Entity IDs / Actor & Support / Contact Establish-Transfer-Release / Weight & Occlusion Carryover / Resulting Owner-State。传物须闭合给予者释放与接收者获得同一实体，不复制道具；无交互的镜头写 NOT_APPLICABLE 及理由，不强建动作。

## Clip IDs

默认继承 Shot ID：`S005-SH04-CL01`。一个 Shot 只有在平台或动作连续性确有需要时才拆多个 Clip；拆分不能隐藏镜头修改。

## Input frame role

- `START`：动作尚未开始，允许从 Trigger 启动；
- `MID`：动作已经进行，必须从画面可见阶段继续；
- `END`：主要动作已完成，只设计余势、停顿或下一事件；
- `REFERENCE`：只约束批准的风格、身份、空间或状态，不宣称它是时间起点。

以上是画面所代表的时间角色，需另记 Input Use：CURRENT START / TARGET END / REFERENCE ONLY。MID/END 作为当前时间起点时从已发生阶段之后继续；END 作为目标约束时锁定结束状态，不当开场重播。实际能否使用这些输入由模型 Profile 验证，不在此承诺。

Motion Master 记录 `Planned Duration`。目标模型实际一次生成时长由 Prompt Adapter 写为 `Generation Duration`，二者不一致时必须显式说明拆分、延展或剪辑策略，不能倒改创作时长。

## Return rule

先记录 Motion Review（PASS / REVISE / NOT_EVALUATED）、Covered Clips、Evidence & Findings、Blocking Issues / Owner、Pending Motion/Pilot Validation；文本审核只覆盖规格。局部问题保持 REVISE 并修字段；上游冲突按下列责任返回。平台能力未验证本身不否定模型中立的文本逻辑，生产执行须在后续适配/样片关口处理。

- 静态首尾无法属于同一世界/身份 → Storyboard Rework
- 动作无法在已定机位、时长和调度中完成 → Shot Revision
- 平台能力不支持但创意规格成立 → Prompt/Generation Routing，不修改 Motion Master
- 输入帧的时间角色不清或与动作阶段冲突 → Storyboard Rework
- 艺术变化超出批准规则 → Scene / Visual Revision，经上游修正后重新检查受影响 Clip
