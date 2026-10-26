---
name: film-screenplay-developer
description: 将已批准且状态为 READY 的 Film Treatment 与 Character System 写成可读、可拍、可交接的电影或剧集单元剧本，并维护场景、连续性与来源登记。用于 Treatment 已完整，需要发展具体场景、可见行动、对白和声音，但尚未进入视觉圣经、场景导演、镜头、分镜、关键帧或图像/视频提示词的阶段。
---

# Film Screenplay Developer

把已批准的 Treatment 转化为人类可读的剧本主版本。用具体场景、行为、声音和对白讲清故事；不要把剧本写成 AI 生成指令。

## Required inputs

优先读取：

1. `Film Treatment`，且 Readiness 为 `READY`
2. `Character System`
3. `Story Blueprint`
4. `Film Project Brief`
5. `Research Pack` 与 `Source Index`（历史、现实、文化或科学题材）
6. 用户本轮锁定的剧本决定

若输入是 `TREATMENT DECISION GATE` 或任一 Return 报告，不得写剧本；原样返回其上游路径。

## Load resources

- 创建、改写或诊断剧本前读取 `references/screenplay-writing-guide.md`。
- 创建交付物或验收时读取 `references/screenplay-contract.md`。
- 使用 `assets/screenplay-template.fountain` 建立剧本主版本。
- 使用 `assets/screenplay-register-template.md` 建立结构化交接登记。

## Outputs

默认保存：

```text
AIGC Creater/projects/<project-id>/screenplay/
├── screenplay.fountain
└── screenplay-register.md
```

`screenplay.fountain` 是创作语义主版本；`screenplay-register.md` 记录范围、场景功能、连续性、研究依据、假设和未决项。不要在主剧本中塞入模型提示词或内部检查表。

## Workflow

1. **Verify readiness.** 确认 Treatment 为 READY，范围与 `Standalone Film / Prototype Unit / Episodic Unit / Serial Arc` 一致。
2. **Inherit the contract.** 记录 Source Versions & Ready Scope、本次交付和终止阶段，继承 LOCKED / OPEN / ASSUMED、研究依据、人物知识与边界、Behavior Logic、Perception & Response Logic、Change / Stability Basis、结局和 Carryover Boundary。接住 Treatment 的组织原则、时间逻辑、艺术方法与已授权 Dramatized Choices；部分上游依据不得扩大为全片可用，旧资料缺字段时核对实质内容，不要求重做已批准成果。
3. **Build the scene spine.** 按完整过程把 Treatment Sequence 转为必要场景，不机械一段一场，也不提前按 Clip 时长切碎。每场有进入状态、行动/观察/感知作用与退出状态；地点变化本身不构成功能。叙事检查行动与回应，观察/诗性可保持状态但应有明确体验作用，不强制每场转折。
4. **Write visible and audible content.** 把抽象心理或艺术意图落实为可见可听的行为、现象和声音，写清人物的回应或有意无回应；不逐项添加微动作。梦境、象征、抽象与非线性表达遵守 Treatment 的关联及开放解释范围，保留必要时间与状态线索，不写机位、构图或运镜。真实心理未知仍为 UNKNOWN，授权重构单列创作来源，不冒称史实。
5. **Write character-specific dialogue and silence.** 结合人物、关系和情境确定对白作用，可是请求、试探、回避、陪伴、闲谈或诗性表达，不要求每句都操控对方。回答或沉默应有关系依据，潜台词与人物差异来自信息、关注和回应方式；不让对白重复动作、替角色解释已知背景或用旁白掩盖缺失过程。无对白项目不为填表加台词。
6. **Connect scenes and preserve state.** 继承物理条件、物件、知识、关系和未完成行动，并说明前场留下的行动、疑问、声音、时间或情绪怎样被后场承接。跳时、梦境或有意断裂明确必要线索和允许变化；转场词不能代替实际联系。结果写入 register 的 Scene Connection Review，不在正文暴露台账或写剪辑覆盖方案。
7. **Read through and check timing.** 先仅读剧本复述故事/体验路径，检查可读性、人物回应、重复、铺垫与结尾，再对照 Treatment、人物系统和场间状态修正。自检注明 SELF-AUDIT，未独立验证不能宣称独立冷读。按 guide 朗读对白并顺演动作，在 Timing Review 记录 ESTIMATED / TIMED / NOT_EVALUATED、范围、方法、目标与差值；对白、动作、停顿可重叠时不机械相加。时长未知保持 OPEN，未计时只写估算；明确目标有未解决冲突时先改表达或提出具体取舍，不静默加速台词、删剧情或改片长。
8. **Save and route.** 完成主剧本与 register，在现有 Decision Register 记录 Screenplay Review 的范围、证据、来源、问题与修正。只有 Coverage COMPLETE、正文及场间审阅 PASS 且无影响交接的时长/连续性问题，才推荐 World & Visual Bible Development；PARTIAL 继续写，问题返回正确上游。审阅不等于用户批准、独立冷读或真实播放验证，不新增审批门。

## Method overlay（when adopted）

仅加载 Adoption Receipt 指定的场景、行动、表演、声音或节奏字段。Method 若会改变故事因果、人物选择或结局，先返回上游；不能把类型机制拖到 Prompt 阶段补写。Screenplay 继续作为人类可读创作主版本。

## Screenplay format

使用简洁 Fountain 语法：

- 场景标题：`INT.` / `EXT.` / `INT./EXT.` + 地点 + 时间，并使用稳定场景号 `#S001#`。
- 动作：现在时、可见、可听；避免小说式内心说明。
- 人物与对白：中文人物名可用 `@人物名` 强制识别；括号说明只在含义无法由行动或语句判断时使用。
- 转场：只在叙事意义明确时使用，不把剪辑和镜头设计提前塞进每场。
- 声音：可写重要环境声、画外信息及已确定的叙事性声音/静默线索；具体配乐制作和混音留给导演与后期阶段，不靠“悲伤音乐起”替人物和事件建立情绪。

## Non-negotiable boundaries

- 不输出 Shot List、景别、焦段、机位、构图、摄影机运动或剪辑覆盖方案。
- 不输出 Storyboard、Hero Frame、Keyframe、人物六视图或视觉资产。
- 不输出图像 Prompt、视频 Prompt、模型参数或 Seedance / Kling / Veo 适配文本。
- 不因 AIGC 可执行性而在每段机械重复人物全名、服装、环境和镜头参数。
- 不用旁白替代尚未解决的因果，不用对白朗读世界观。
- 不擅自添加改变 Treatment 伦理、结局或人物能动性的重大情节。
- 不把 Prototype Unit 称为第一集，不为 Standalone Film 制造未经授权的续集钩子。

## Historical and real-world rules

- 仅把已核实的言行写成事实。
- 合理重建只用于连接已知事件，并在 register 标为 `RECONSTRUCTION`；不得创造改变历史结果的行动。
- 未证逐字对白优先省略、间接表达或保持沉默；若项目明确允许戏剧化对白，必须标记其创作性质。
- 群体行为有记录但个体心理无记录时，保留群体差异，不创造代表全体的虚构英雄。

## Completion gate

推荐下一阶段前必须满足：

- 请求范围内所有场景均已完成，不以梗概代替缺失场景；
- 每场有行动、观察或感知作用，状态变化或有意维持均可读；场间承接、时间线索与允许变化明确；
- 人物选择与 Character System 一致；
- 主要行动存在可理解的原因，并处理明显更安全或更简单的替代方案；
- 对白或沉默有情境与关系作用，人物差异、潜台词和回应可理解，无对白时明确不适用；
- 结局兑现 Treatment；
- register 能追溯重要事实、重建、假设和连续性；
- Screenplay Review 为 PASS，顺读证据与时长检查方法、范围和限制明确；时长估算不冒称实际计时或成片播放，无影响交接的已知冲突；
- 没有越界进入视觉、镜头、分镜或 Prompt。

若长篇无法一次完成，在完整场景边界停止，在 register 标明已覆盖与未覆盖场景，并给出唯一继续锚点；不得把不完整草稿称为完整剧本。
