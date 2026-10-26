# Prompt Compilation Guide

## Compile, do not rewrite

先确定交付边界：生产包从批准且 CURRENT 的源合同编译；CONTENT DRAFT 可从明确的探索稿编译，列缺失参考、用途批准和能力待核实项，不要求先回传媒体，不可执行。草稿不能把冲突内容当事实，也不能伪造文件路径。

Prompt 只编码已经批准的内容：

```text
Source identity and world
→ current start state
→ trigger
→ primary action and phases
→ camera event
→ environment / secondary motion
→ end state
→ continuity exclusions
→ supported parameters
```

编译前确认源版本 freshness 为 `CURRENT`。`RECOMPILE` 表示从当前源重新生成 Prompt/Unit Card，不表示可以继续沿用旧 Prompt；`STALE / BLOCKED` 直接返回。

若 Prompt 中首次出现新角色、新道具、新动机、新场景结构或新结局，它不是编译，而是越权创作。

## Compactness

压缩前建立 Intent Preservation Map：`Protected Intent / Source ID-Version / Carrier: Input-Prompt-Control / Target Location / Status / Gap`。保护观看立场、信息先后、Must Read/Withhold、构图、注意层级、必要保持及结束状态。图像负责的内容无需全部重写，真实输入角色要可追踪；删词不删意义。缺失输入可记待补，不能把尚不存在的承载点标 MAPPED。

- 每条信息只出现一次，放在目标模型最容易解析的位置。
- 使用具体主体和动作，不使用“它、他们、自然地”等歧义指代。
- 风格信息从批准资产和 Frame 提取，不重复长篇世界观。
- 模型不支持结构化字段时，转换为清晰自然语言，但仍保留 manifest 映射。
- 十三项覆盖回执只用于证明信息去向，不是 Prompt 段落清单；`NOT_APPLICABLE / UNSUPPORTED / CONFLICT / RETURN` 不得被填充词掩盖。

## Route by input mode

先选择目标模型已核实支持的执行模式，再编译语言：

- `T2V`: Prompt 承担视觉锚点和完整运动，但不能假装有参考图锁定。
- `I2V`: 图像负责身份、构图和初始状态；文字重点写触发、变化、摄影机、表演、声音和结束状态，不重复长篇重画首帧。
- `START_END`: 核实当前入口支持，区分当前起点和目标尾帧；连接遵循批准的物理或艺术规则，文字可解释不代表运动已验证。
- `MULTI_REFERENCE`: 为每份参考分配单一清晰职责，避免身份、服装、姿态和风格互相覆盖。
- `EDIT / EXTEND`: 写清 Change / Preserve / Constraints 与连接边界，不把编辑任务当全新生成。
- `AUDIO / PERFORMANCE DRIVEN`: 音频或表演参考的允许影响必须由Profile确认，不自动改变人物身份和场景。

模型、时长、画幅、分辨率和控制参数默认写在Prompt外；模型要求时间线或字段名时才按其schema保留。

Profile 按 Provider / Platform / Model-Version / Task Entry / API-UI Route / Input Mode / Account-Region Scope 留来源与访问日期；不能把其他入口的同名模型能力外推。逻辑别名与真实槽位分开；未核实不编参数、按钮或绑定语法。这里只规定核实方法，不锁定任何模型的最新能力。

## Image prompt

至少编码：资产身份、Frame 的单一时刻、空间/轴线投影、构图深度、可见动作、光线/时间、Must Show 与 Must Avoid。不要加入时间过程。

## Video prompt

至少编码：首帧状态、触发、主要运动阶段、可观察表演链、人物/道具接触、摄影机、环境、继承的 Look/Light State 或有触发的变化、时长、结束状态和禁止漂移。不要只描述最终画面。

继承 Animatic/Shot 的 Rhythm Role 和 Required Hold；模型单次时长不足时显式拆 Clip 或记录降级，不静默压缩人物反应。Atmospheric Medium 只有在上游已经定义介质、来源、分布、驱动力和受光方式时才进入 Prompt；否则保持清洁空气或省略，不补通用烟雾颗粒。

先保留 `MAIN / SUPPORT / HOLD`，再将 `PREVIOUS RESIDUE → TRIGGER → DELAY → VISIBLE CHANGE → HANDOFF` 压缩为目标模型易解析的时间顺序。SUPPORT 不得获得比 MAIN 更强的动作描述；HOLD 对象不写随机眨眼、漂发、粒子或镜头游移。完整链条保留在 Production Unit Card 的验收区，即使模型 Prompt 需要更短。

继承 Motion 的 Trigger or Continuation Basis；等待、持续劳动或观察不必有新触发/变化。Input Use 与 Frame Role 分开：MID/END 作 CURRENT START 从当前阶段后继续，END 作 TARGET END 约束目标，REFERENCE ONLY 不定义时间零点。图片仅描述当前快照；视频保留批准的持续/变化，不新增微动作。

Presentation Mode / Artistic Rule ID-Version、作用层、变化过程与保持项单列继承。真实空气须有物理驱动；非物理绘画、形变、象征空间按艺术规则编译，不自动加真实皮肤、粒子或摄影透视。模型不支持时显式 UNSUPPORTED，不用自然语言冒充有效控制。

## Coverage before release

对每个 Unit 完成十三项回执：Reference anchors、Overall concept、Dynamic description、Image texture/cinematography intent、Shot language、Scene、Color/style、Light、Composition、Emotion/observable performance、Shot timeline、Sound、Exclusions。每项写 `MAPPED / NOT_APPLICABLE / UNSUPPORTED / CONFLICT / RETURN`、来源合同与执行落点。先解决 Conflict/Return，再发布；Unsupported 必须有明确降级或后期去向。

## Model incompatibility

比较方案时记录 Unsupported Field / Alternative / Expression Cost / Source Permission / Pending Validation。下列路径是候选顺序，不授权改变已批准镜头、表演、艺术规则或必要停顿；有意义变化返回责任上游。保留可行的文本创意，不以平台局限倒改主合同。

按顺序处理：

1. 检查是否可通过已批准 reference/start/end frame 支持。
2. 在不改变 Shot 的前提下拆分执行 Clip。
3. 按 Motion Spec 的简化优先级删除次级运动。
4. 推荐另一个已核实模型。
5. 若仍会改变主动作或结局，停止并请求用户决定。

## Reverse-check

暂不查看创作源文件，从完整编译输入组合（Prompt、实际参考/角色/上传顺序、已核实控制项）回答，再与源合同比较：

- 谁/什么是主体？
- 开始在哪、处于什么状态？
- 什么触发动作？
- 动作按什么顺序发生？
- 摄影机是否动，为什么、何时停止？
- 结束状态是什么？
- 哪些身份、空间、道具和文字不能变化？
- 观看立场、注意对象、构图与 Must Read/Withhold 由哪里承载？
- 是新触发还是持续/HOLD，哪些停顿和艺术规则不能丢？
- 输入是当前起点、目标尾帧还是参考，实际槽位是否对应？

任何关键答案缺失都要重新编译。

Prompt Review 写 PASS / REVISE / NOT_EVALUATED、范围、证据/发现、阻断项/责任层和待 Pilot 验证。草稿缺图或能力未知时不把输入核实写 PASS；内容仍可交付，包记 CONTENT DRAFT、卡记 NOT_READY，依赖另记 WAITING_DEPENDENCY。生产单元还须批准用途、Profile、回执及 Pilot/真实状态依赖满足，不从文本反查通过推定模型成功。
