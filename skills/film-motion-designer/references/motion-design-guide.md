# Motion Design Guide

## Motion is change through time

不要重述静态画面。说明什么触发变化、哪些层先后行动、何时停下，以及结束状态怎样供下一镜继承。

坏例：人物自然地慢慢扫地，镜头电影感后退。  
可执行规格：许可后 0.5 秒保持；扫帚由分界向共享通道推进两次，第二次完成时人物停止前进；摄影机在通道清理完成后才后移，并在两摊同时进入稳定关系时停止。

## Attention hierarchy

每个时间段标一个 Primary Motion。次级运动只能支持它：

- 主动作是手与道具接触时，面部和摄影机尽量稳定。
- 主动作是反应时，不让背景人群和光线同时剧烈变化。
- 摄影机依据继承 Shot 的动作、声音、观察或艺术规则启动/持续；与主体同步复杂运动时明确主次和可读检查，不机械禁止同步。

按时间段记录 Attention Lead / Support-HOLD / Camera Coordination / Handoff，可维持同一注意对象或在批准节点交接。不要求每段都有新动作；持续劳动、等待或观察写 Continuation Basis / HOLD Purpose，不用微动作维持所谓生命感。

## State connection plan

读取 Stage 11 State Pair Check，列 Known Start / Planned End、Mandatory Checkpoints、Preserved Anchors、Static Evidence、Pending Motion Validation。首尾状态可对上只是必要依据，不能声称中间接触、遮挡或形变已验证。没有尾帧图时可从批准 Shot/Scene 取得结束状态；没有批准依据则标缺口，不补造图片或动作。

输入角色与使用方式分别判断：MID/END 若作为当前时间起点，只从其后继续；END 若作为目标约束，则约束结束状态，不从它重新启动动作。REFERENCE 不定义动作时间零点。

## Contact and weight

说明：

- 谁施力、物体由什么支撑；
- 接触点何时建立与解除；
- 重量如何影响速度和身体重心；
- 遮挡后哪些状态必须保持；
- 动作停止的物理或意图原因。

关键传递按需拆为接近 → 接触 → 承重/所有权转移 → 释放 → 稳定；给予者解除控制与接收者获得同一物件必须可衔接。遮挡前后记录持有者、持物手、接触点、动作相位和数量；不能用遮挡掩盖瞬移/复制。时间段内各层可并行，接触节点按动作顺序检查，不强制每镜填齐五段。

## Camera movement

区分：

- Translation: 摄影机位置改变；
- Rotation: 摄影机位置不变，朝向改变；
- Optical change: 焦距/焦点变化；
- Subject approach: 主体接近静止摄影机。

每次运动写触发、路径、速度曲线、终点、停止理由。若 Shot 指定静止，明确 HOLD。

## Timing and sound

- 对白开始前的吸气、反应和停顿只在剧情需要时保留。
- 口型镜头记录台词区间与说话者可见程度。
- 场内声音可以触发视线、动作或剪切；不要在 Motion Spec 选音乐。
- 转场声音与下一镜的状态必须一致。

## Observable performance

把“悲伤、紧张、松弛”等结果词编译成当前镜头可看见或听见的链条：进入姿态与重心、视线目标、呼吸/声音/停顿、手与道具关系、服装/头发对动作或环境力的响应、触发后的变化与退出状态。只保留能服务人物意图、节奏或物理作用的微动作。

同一镜头内不要让眨眼、喘息、手部、衣物、头发和摄影机全部自动运动。没有动机或环境力时写 `HOLD`。

## Look and light inheritance

继承 Storyboard 的 `Scene Look & Light State ID / Version`。光线、天气或时间变化必须写起始状态、触发、变化过程与结束状态；没有批准触发时保持 `HOLD`。Motion Spec 不用“更有电影感”改写光向、冷暖、曝光或材料反应。

同时继承 `Atmospheric Medium State`：介质、来源、空间分布、密度、运动驱动与受光方式。人物经过、开门、热源或风可以触发局部变化；没有物理作用时写 `HOLD`，不让灰尘、雾、蒸汽和头发一起自动运动。

继承 Presentation Mode / Artistic Rule IDs 的确切版本。非物理形变、平面空间、绘画笔触或象征变化单列 Artistic Motion Layer / Trigger or Continuation Basis / Change Process / Preserved Features，不伪装成空气介质；批准的艺术变化不强制现实作用力，未经授权的身份/地标/故事改变仍须返回上游。

## Rhythm inheritance

继承 Animatic 的 Rhythm Role 和 Required Hold。Motion 只把必要停顿、反应和动作能量落实到阶段时长，不重新设计剪辑节奏；若模型生成时长装不下关键停顿，返回 Shot/Storyboard 或由 Prompt Adapter 明确拆 Clip，不能悄悄删除反应空间。

Phase Timeline 用连续且不重叠的主时间段覆盖 Planned Duration，运动层可在段内并行；不要把各层并行动作时长相加造成总时长虚增。可用估算区间设计，但交接须给一组闭合的计划时段并注明估算方法；不要用小数秒冒充实测。

## Motion review and delivery

Motion Review 使用 PASS / REVISE / NOT_EVALUATED，记录 Covered Clips、Evidence & Findings、Blocking Issues / Owner、Pending Motion/Pilot Validation。检查状态连接、关键接触、艺术依据、注意力/摄影机配合、闭合时间与对白声音、跨 Clip 交接。文字可理解不等于已生成或模型可完成；风险假设交后续 Pilot，不要求本阶段先生成样片。

仅内容交付可完成 MOTION EXPLORATION，列待补参考/审批与验证条件，并交提示词适配作内容草稿；不要求用户先生成回传，不标生产 READY。生产交接仍检查当前所需帧和用途批准、适用 Sequence/Animatic 证据及文本 PASS。局部问题只修失败字段；身份/镜头事实冲突返回正确上游，不在 Motion 或 Prompt 偷改。

## Failure simplification

默认优先级：

1. 保留角色身份与世界坐标。
2. 保留主要动作和结果。
3. 保留关键道具接触与视线。
4. 简化次级衣物、环境和背景运动。
5. 最后才考虑简化摄影机路径；不得改变叙事功能。

## Self-audit

- 每个运动有触发和停止吗？
- 所有层是否无因同时运动？
- 时间总和闭合吗？
- 首尾帧真的能由中间物理过程连接吗？
- 相邻镜头有换手、瞬移、方向翻转吗？
- 是否夹带模型参数或 Prompt？
- 表演是否由姿态、视线、呼吸/声音、手部与物理响应构成，而非抽象情绪或随机微动作？
- Look/Light State 是否被继承，所有变化是否有批准触发？
