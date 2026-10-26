---
name: film-motion-designer
description: 将已批准的 Storyboard/Keyframes、Shot List、剧本和资产规则转化为逐镜人物、道具、摄影机、环境、时间、声音同步与转场运动规格。用于定义每个视频 Clip 从起始状态经何种触发和动作阶段抵达结束状态；不用于改写镜头、编写模型专用提示词、调用视频生成或审核成片。
---

# Film Motion Designer

把静态分镜之间的时间和物理过程设计清楚。Motion Spec 是模型无关的运动主合同，后续 Prompt Adapter 只能翻译，不能重写。

## Required inputs

1. Storyboard / Frame Manifest，状态 `READY FOR MOTION DESIGN` 或 `USER-APPROVED`
2. `shot-list.md` 与 `shot-continuity-ledger.md`
3. `screenplay.fountain` 和 Scene Design Pack
4. APPROVED 资产合同
5. 总时长、对白/口型和帧率需求（已知时）
6. `atmosphere-state-register.md`（存在显著或连续性敏感空气介质时）
7. `storyboard/lighting/lighting-pass.md` 与 lighting continuity ledger（项目执行过分镜光影 Pass 时）

继承上游确切版本、本次范围和交付边界。PLAN_ONLY 或未审核分镜可完整交付 MOTION EXPLORATION，并将缺失参考、批准用途或预览证据列为待验证；可交 Prompt Adapter 编译明确标注的内容草稿，不得标执行就绪或提交生成。生产级 Motion Spec 仍须当前所需帧、资产用途与适用序列/Animatic Gate 通过，不能从单帧 USER-APPROVED 外推整段。

## Load resources

- 设计前读取 `references/motion-design-guide.md`。
- 创建或验收时读取 `references/motion-spec-contract.md`。
- 使用 `assets/motion-spec-template.md` 与 `assets/clip-state-template.md`。
- 存在已批准 Performance Beat，或抽象情绪需要展开成时间链时，使用 `film-micro-performance-designer`；只把其动作链分配到 Clip 时间和物理层，不重新发明人物心理。

## Outputs

```text
AIGC Creater/projects/<project-id>/motion/
├── motion-spec.md
└── clip-state-ledger.md
```

## Workflow

1. **Verify frame roles and state connection.** 确认 START / MID / END / REFERENCE、文件/版本、用途批准和计划时长，继承 Stage 11 State Pair Check。列 State Connection Plan：已知首尾、必须经过的动作/接触节点、必须保持项、静态证据与待运动验证项。没有 End 图时可依据批准 Shot/Scene 计划结束状态，不强制补一张尾帧；未知状态不由模型猜。宫格不作为单镜输入。
2. **Freeze creative decisions.** 不改变 Shot 数、景别、机位、构图目的、对白或故事结果。无法连接首尾时返回 Storyboard/Shot。
   - 存在批准 Lighting Pass 时，继承世界光源、静态受光与连续性；只有 Pass 已授权的灯光开关、遮挡、人物/摄影机穿越光区、天气或时间触发才能成为动态光线变化。
3. **Define continuation or change.** 写 Input Frame Role → Start State → Trigger or Continuation Basis → Motion/Hold Phases → End State。MID/END 作为时间起点时从可见阶段继续，不重播已完成动作；若作为目标尾帧约束则锁目标状态，不把它误当开场。持续动作、等待、观察可保持原策略，写 HOLD/持续依据，不强加新事件或情绪转折。
4. **Separate performance and artistic layers.** 分别设计身体、视线、呼吸/声音/停顿、手与道具、服装/头发、摄影机、环境、空气和光线；无必要运动写 HOLD，不用微动作填满时间。继承 Presentation Mode / Artistic Rule IDs 与版本，真实空气/物体按物理来源与驱动，非物理形变、绘画空间或象征变化按批准规则写作用层、变化过程、触发/持续依据与保持项，不强制写实，也不借艺术模式改变身份、故事或未授权空间。
5. **Design contact checkpoints.** 对关键交互按需写接近、接触建立、承重/所有权转移、释放、稳定后的状态；注明施力者、支撑点、重心/惯性与遮挡后保持项。并非每次接触都有五阶段，不为简单持物强建动作。传物须给出同一实体的给予者释放与接收者获得，不能复制、瞬移或跳过承重；非物理作用按批准艺术规则分别记依据。
6. **Close timing.** 各阶段时长之和等于 Shot 时长；给对白、反应和停顿留出空间。不要用模糊的“慢慢”替代节奏。
7. **Coordinate attention over time.** 按时间段记主导对象、支持/HOLD 层、摄影机配合与注意力交接。可在已批准范围内同步人物和摄影机运动，关键是主次可读，不机械错开所有复杂动作。固定机位与持续静止均有效；不新增 Shot 未批准的运动行为。
8. **Specify the inherited camera event.** 运动写启动/持续依据、路径、主体关系、速度变化、终点与停止理由；依据可为动作、声音、持续观察或批准艺术规则，不强制新剧情触发。静止写观察/等待目的。焦距、焦点变化与机位位移分开。
9. **Design transitions.** 核对当前 End 与下一 Start 的状态、动作相位、余势、声音和必要停留；省略、倒叙、并置或艺术转换继承 Shot 的依据，说明保持项与观众定位，不把有意不连续伪装匹配。
10. **Review and route.** Motion Review（PASS / REVISE / NOT_EVALUATED）检查状态连接、接触/艺术依据、注意力、阶段时长与声音、跨 Clip 衔接及风险。文本 PASS、当前范围上游就绪且无阻断项才 READY FOR PROMPT ADAPTATION；文字逻辑通过不证明实际运动或模型能力。草稿保留 MOTION EXPLORATION 和待验证依赖；局部问题 REVISE，上游冲突按责任返回。只改失败字段和受影响依赖。

## Method overlay（采用时）

把 Method 的运动层、HOLD 层、触发、幅度、延迟、停止、循环和声画关系转换为 Clip 时间合同；只控制 Adoption Receipt 授权字段。抽象类型词必须落成可观察运动，未经上游批准不得新增动作或镜头结果。

## Per-clip requirements

- Clip ID / Shot ID
- Start Frame / End Frame / Input Frame Role
- Planned Duration；Generation Duration 由 Prompt Adapter 在独立 Prompt Package 中映射
- Start State
- Trigger
- Continuation Basis / HOLD Purpose
- State Connection Plan / Preserved Anchors / Pending Motion Validation
- Primary Motion
- Body / Posture / Weight phases
- Face / Gaze
- Breath / Voice / Pause
- Hand / Prop Contact
- Contact Checkpoints / Support / Release / Occlusion Carryover（按需）
- Costume / Hair Physical Response
- Camera Motion
- Environment / Secondary Motion
- Atmospheric Medium State / physical source / driver / HOLD or triggered change
- Scene Look & Light State ID / Version and triggered change or HOLD
- Presentation Mode / Artistic Rule IDs & Versions / Layer / Change or HOLD / Preserved Features
- Rhythm Role / Required Hold inherited from Animatic
- Dialogue / Lip-sync / Sound timing
- Speed / Acceleration / Holds
- Phase Attention / Camera Coordination / Handoff
- Occlusion / Physics / Contact constraints
- End State
- Transition to next Clip
- Failure risks / Simplification priority
- Motion Review / Evidence / Blocking Issues / Pending Pilot Validation

## Non-negotiable boundaries

- 不重新设计镜头或构图；Storyboard 无法连接时返回上游。
- 不写 Seedance、Kling、Veo 或其他模型语法、参数、负向词与参考权重。
- 不调用视频生成，不声称平台能够完成或已经完成。
- 不把“电影感运动、自然动作、丝滑运镜”当成规格。
- 不让镜头、人物、道具、衣物、环境和光线同时无因运动。
- 不用眨眼、呼吸、头发飘动等随机微动作填满所有镜头。
- 不让角色在剪切后凭空换手、换位、转向或恢复道具状态。
- 不让 MID/END 输入帧重新执行已经可见的动作，不把宫格预览当作单镜输入。

## AIGC feasibility

- 优先保证主体身份、主动作和终止状态，再保留次级运动。
- 高风险交互拆成清晰阶段，但不能改变 Shot 与表演意义。
- 对手部接触、多人遮挡、快速转面、长对白口型、反射、文字和复杂摄影机路径标记风险。
- 写明失败时的简化顺序，Prompt Adapter 不得自行猜测。

## Completion gate

- 每个 Shot 都有对应 Clip 规格；
- 所有阶段时长闭合；
- Start/End 与批准关键帧一致；
- 输入帧角色明确，动作从当前时刻继续；
- State Connection Plan 明确必经节点、保持项和待验证过程；未提供 End 图不自动阻断已有批准结束状态；
- 主运动、触发、停止和注意层级明确；
- 人物、道具、摄影机和环境运动分层；
- 姿态/重心、视线、呼吸/声音、手部和服装/头发响应形成可观察表演链；
- Look/Light State 被继承，任何变化都有批准触发；
- 物理空气、独立艺术规则和 Rhythm Role 被继承；真实空气无依据运动、艺术变化超范围或必要停留缺失须修正；
- 相邻 Clip 状态连续；
- Motion Review PASS、当前范围用途与上游证据就绪且无阻断项才生产交接；文本审核不冒称实际运动或 Pilot 通过；
- 没有模型专用 Prompt 或生成声明。
