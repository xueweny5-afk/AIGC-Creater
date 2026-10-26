---
name: film-micro-performance-designer
description: 将“惊讶、悲伤、紧张、坚定、释然”等抽象情绪和表情要求转化为由触发、延迟、抑制、微动作与结束状态组成的可观察表演链。用于剧本动作描写、场景导演、镜头表演、分镜瞬间、人物运动规格和视频提示词前的微表演设计或审查；不建立固定表情词典，不诊断真实人物心理，也不改写人物目标、对白、镜头或故事结果。
---

# Film Micro Performance Designer

把“演出某种情绪”改写成观众能看到、演员能执行、模型能按时间顺序理解的行为。微表演不是更多脸部形容词，而是压力如何进入身体、被人物处理，又从哪里泄露出来。

## Required inputs

尽量取得：

- Source Scene / Beat / Character / 当前动作
- 人物即时目标、当前策略、关系对象和不能轻易暴露的内容
- 具体触发：话语、声音、视线、物件、接触、记忆线索或环境变化
- 进入时的姿态、重心、视线、呼吸、手与道具状态
- 年龄、身体条件、服装、空间、文化和已锁定行为边界
- 目标层级：剧本文字、Scene、Shot、Storyboard、Motion 或 Prompt 前置母版
- 计划景别与可见时长（已知时）

缺少目标、触发或基线时，抽象情绪不能直接编译成生产级表演。虚构人物可在已批准 Character System 范围内设计；真实人物、历史人物或观察主体只使用可观察证据，不补写无依据内心。

## Load resource

设计、改写或审查时读取 [micro-performance-craft.md](references/micro-performance-craft.md)。它包含表演链语法、动作通道、强度与景别适配、常见情绪的非固定候选路径及交付模板。

## Modes

- `TRANSLATE`：把抽象情绪句改成可观察动作。
- `DESIGN`：为一个戏剧 Beat 建立完整 Performance Beat Contract。
- `VARIANTS`：在人物目标不变的前提下，提供 2–3 种不同策略的表演路径。
- `REVIEW`：检查过演、随机微动、不可见细节、无触发动作和连续性断裂。
- `REPAIR`：只修失败的时间节点或动作通道，保留已通过表演状态。

## Workflow

1. **Locate the dramatic pressure.** 说明人物此刻想做什么、什么阻碍他，以及触发为何会改变当前策略。情绪词只能作为内部索引，不能成为交付动作。
2. **Freeze the entry baseline.** 写清触发前人物正在做什么、身体如何承重、看向哪里、手接触什么、呼吸/声音处于什么状态。没有基线，就无法看出“微小变化”。
3. **Choose a response logic.** 判断人物是立即外露、延迟理解、主动压住、转移到别的动作、保持表面不变，还是在触发后才逐步承认。选择必须符合人物、关系和场合。
4. **Build the causal chain.** 从 `Trigger → Attention Shift → First Leak → Regulation / Displacement → Secondary Change → Settle / Handoff` 中选择必要节点；普通 Beat 使用 2–5 个节点，不为填满模板强加动作。
5. **Budget the channels.** 只选一个主要通道和至多两个支持通道：姿态/重心、视线/眼睑、呼吸/声音、嘴唇/下颌、头颈、手/道具、人与空间距离。其他层写 `HOLD`。
6. **Set latency, amplitude and recovery.** 写清动作发生在触发后何时、幅度相对基线如何、持续多久、是否被人物收回。用事件和节拍描述，不用“非常自然地、微微地、缓缓地”连续堆叠。
7. **Check physical and visual plausibility.** 动作符合支撑、呼吸、接触和角色身体条件；细节必须能被当前景别、光线、遮挡和时长看到。看不见但叙事必须读到时，返回 Shot Design 或改用更大动作/声音，不强行写瞳孔等不可读细节。
8. **Close the end state.** 记录结束时姿态、视线、呼吸、手/道具、是否回答及未完成意图，供下一 Shot/Frame/Clip 继承。
9. **Translate by stage.** 剧本只保留有叙事价值的动作；Scene 保留目标/策略/触发；Shot 选择摄影机能读到的投影；Storyboard 锁定单一瞬间；Motion 展开时间链；Prompt 只编译可见、按时间发生的动作。

## Default output

- Performance Beat ID / Source / Status
- Character Objective / Current Tactic / Social Mask
- Entry Baseline
- Trigger
- Primary Channel / Supporting Channels / HOLD layers
- Chronological Micro-action Chain
- Latency / Amplitude / Duration / Recovery
- Prop / Space / Partner Response
- Voice / Breath / Silence
- Observable End State / Next Handoff
- Intended Framing / Readability Risk
- Continuity Locks / Must Avoid
- Upstream assumptions or return reason

简单改写不必输出完整表格，只给一段动作链和一句设计理由。需要保存复杂或跨镜表演时，可放入 `projects/<project-id>/direction/performance-beats.md`；不明确 Project ID 时不创建项目文件。

## Handoff boundaries

- `film-scene-director` 决定目标、策略、触发、调度和拒绝边界；本 Skill 细化可观察表演。
- `film-shot-director` 决定景别、机位和镜头运动；本 Skill 只标可读性需求，不选镜头。
- `film-storyboard-designer` 从动作链选择一个可见瞬间，不把整条时间链塞进一帧。
- `film-motion-designer` 把已批准动作链分配到 Clip 时间和物理层。
- `film-prompt-adapter` 只编译当前镜头可见部分，不重新发明情绪动作。

## Non-negotiable boundaries

- 不建立“某情绪必然对应某表情”的一对一词典；同一情绪必须受人物目标、关系、场合和抑制策略影响。
- 不把瞪眼、挑眉、嘴角下撇、握拳、叹气、低头或流泪当作通用捷径。
- 不让眉、眼、嘴、头、肩、手、呼吸和全身同时变化来证明情绪。
- 不用随机眨眼、无动机喘息、嘴角抽动、手指乱动或持续飘发填充“生命感”。
- 不默认描述瞳孔收缩/放大等难以从普通镜头可靠读取且受光线影响明显的细节。
- 不把“毫无反应”写成空白；如保持表面不变，要说明维持的行为、压力去向或稍后的可见泄露。
- 不为真实人物、历史人物或观察主体虚构内心、创伤、动机或情绪诊断。
- 不修改锁定对白、人物决定、镜头、构图、时长或故事结果。
- 不声称动作已经由演员、模型或最终画面验证。

## Completion gate

- 表演变化有明确基线和触发；
- 动作服务人物目标与策略，不只是情绪展示；
- 时间顺序、延迟、幅度和结束状态清楚；
- 主要与支持通道有层级，其余层明确 HOLD；
- 动作符合角色身体、道具接触、空间和连续性；
- 细节能被计划景别和时长观察，或已明确返回上游；
- 输出没有固定表情公式、过演、随机微动和抽象情绪命令。
