---
name: film-scene-director
description: 将完整剧本、世界视觉圣经和资产状态转化为逐场导演设计，明确场景功能、人物目标、表演行动、空间调度、信息控制、声音、时间与出入场状态。用于进入镜头设计前解决一场戏为什么存在、人物怎样在空间中行动；不用于景别、机位、焦段、运镜、分镜图或生成提示词。
---

# Film Scene Director

把完整剧本解释成可表演、可调度、可交给摄影设计的 Scene Design Pack。先解决人物与空间发生什么，再决定摄影机怎样看。

## Required inputs

1. `screenplay.fountain` 与 `screenplay-register.md`，Coverage 为 `COMPLETE` 或明确的完整场景子范围
2. `world-visual-bible.md`
3. `asset-manifest.md` 与相关资产合同
4. Character System、Treatment 及用户锁定的导演决定

继承上游确切版本、本次场景范围与交付边界。资产尚未覆盖所需用途时可交付 `DRAFT_ASSET_PENDING` 场景文字设计及依赖，不要求先回传媒体，也不推荐生产级 Shot Design。`READY FOR SHOT DESIGN` 须场景审核 PASS，且当前所需 P0 文件、版本、用途、视图与状态均在 Approval Scope 内；资产名旁的 APPROVED 不代表全部用途通过。

## Load resources

- 开始设计前读取 `references/scene-direction-guide.md`。
- 创建或验收时读取 `references/scene-design-contract.md`。
- 使用 `assets/scene-design-pack-template.md`。
- 关键反应、克制表演或抽象情绪需要动作化时，使用 `film-micro-performance-designer` 建立 Performance Beat；本 Skill 仍负责人物目标、策略、触发、调度和拒绝边界。

## Output

默认保存：

```text
AIGC Creater/projects/<project-id>/direction/scene-design-pack.md
```

## Workflow

1. **Verify coverage and assets.** 确认请求范围内剧本完整、Scene ID、连续性、上游审阅结论和核心资产用途覆盖；完整场景子范围不要求全片完成，但注明边界。剧本文本缺失或锁定结果冲突返回 Screenplay；缺失视觉合同返回 Visual Development。媒体依赖待验证不阻止内容交付。
2. **Set the directing thesis.** 用一句话说明观众最终应如何理解这组场景，以及导演通过何种行为、空间和信息路径实现；不以风格词替代。
3. **Preserve world, look and artistic state.** 固定每场进入时的人物、物件、空间、知识、关系、时间和身体状态；关键实体使用稳定 ID，记录数量、所有者、位置、可见性、开合/损坏状态和知情状态。继承 Visual Bible 的 `Narrative Look Arc / Scene Look & Light State / Atmospheric Medium State` 及 `Presentation Mode / Artistic Rule IDs`，没有批准触发时保持 HOLD。真实空气变化须有物理作用；梦境、象征和非写实空间变化按已批准艺术规则记录作用层、触发和保持项，不冒充真实空气或虚构已知物理拓扑。
4. **Design connected performance beats.** 按场景实际需要组织行动段：事件/持续状态 → 谁察觉或未察觉 → 行动/倾听/回应 → 关系、信息或感受的变化/延续 → 下一段承接。段数不设配额，不机械细分每次呼吸。人物目标与策略在适用时明确；陪伴、等待、观察或共同做事可保持原策略，写 HOLD 及其作用，不强制冲突或转折。把情绪落实为可执行行为和必要身体响应，不要求演员抽象地“表现某种情绪”。
5. **Bound the space evidence.** 为关键空间锚点标记 `VISIBLE / INFERRED / UNKNOWN`；推断项写置信度和依据。对门内外、两岸、多出入口、追逐、传物等空间或动作连续性敏感的场景，在 `Scene Design Pack` 画最小方位卡：固定地标、区域边界、人物/道具进入位置、行动路径和未知范围。只画世界中的相对关系，不写摄影机或画面左右；普通单点场景可记 `NOT_NEEDED` 及理由。单视图资产默认只支持有限同侧空间，不为需要反拍或大幅绕行的调度虚构不可见空间。
6. **Design blocking.** 在证据支持的空间或已批准艺术空间规则内安排进入、停留、接近、回避、跨界与离开。说明动作/不动的触发、关系或实际任务理由，以及他人如何回应；允许亲近、协作、习惯和共同注意，不把一切归为权力对抗。无移动必要时保持位置，不为摄影机方便而移动世界。
7. **Control information.** 明确观众知道、人物知道、刻意隐藏和何时公开的内容；说明哪些内容暂时不能展示。
8. **Track performance continuity.** 为主要人物记录进入策略、姿态/重心、视线/倾听、呼吸/声音/停顿、手与道具、服装/头发响应、触发变化与退出延续；用可表演行为代替情绪形容词，禁止用随机眨眼、无动机喘息或持续飘发填充生命感。
9. **Design sound, time and rhythm intent.** 定义场内声音、沉默、时间压缩/延长和必要的声画关系；为每场记录 `Rhythm Intent`：故事压力轨迹、行动/声音能量、必须停留的反应或静默、释放点及触发原因。它说明为什么快或慢，不提前规定逐镜切法、平均镜长或配乐选曲。
10. **Close the scene chain.** 每场明确 Exit State 与下一场 Entry 的承接方式；直接延续核对状态，省略/倒叙/并置按已批准 Temporal Logic 标出时间、感知或意象连接，不强行改成线性因果。未解决或有意保持也须说明观看作用。
11. **Audit and route.** 记录 Scene Review（PASS / REVISE / NOT_EVALUATED）、覆盖场景、行动衔接、表演可执行性、空间/艺术依据、跨场连续性及问题归属。PASS 且当前所需 P0 用途覆盖、无阻断项才标 READY；设计问题留 REVISE 并局部修改，上游冲突 RETURN。内容交付可带明确待验证依赖完成，不能把文本审核写成实际表演或画面已验证。

## Method overlay（采用时）

只将 Method 的场景节奏、注意力、声音或转换机制应用到 Adoption Scope 内；Scene Objective、人物行动、空间和连续性仍由 Screenplay/Visual/Asset 合同决定。多个 Method 争夺同一字段时按 Adoption Receipt 裁决，否则 RETURN。

## Per-scene requirements

- Scene ID 与来源剧本文本
- Direct Cause / Scene Function
- Entry State / Exit State
- Character Objective / Obstacle
- Initial Tactic / Shift Trigger / New Tactic
- Performance Actions / Listening / Refusal
- Scene Beat Chain: event or sustained state / perception / action-response / effect or hold / handoff
- Performance Continuity: posture/weight / gaze / breath-voice-pause / hand-prop / costume-hair response / entry-to-exit carryover
- Scene Look & Light State ID / Version; deviation and narrative trigger or HOLD
- Narrative Look Arc / Atmospheric Medium State; deviation and physical trigger or HOLD
- Presentation Mode / Artistic Rule IDs & Versions; artistic layer / trigger / preserved features or HOLD
- Blocking & Spatial Power
- Spatial Evidence: visible / inferred with confidence / unknown / coordinates / scale
- Audience Beat / Information Design
- Sound / Silence / Time Strategy
- Rhythm Intent: story pressure / action energy / sound energy / required hold or silence / release trigger
- Sound Cue / Source / Trigger / Bridge
- Required Assets / State Changes
- Must Show / Must Withhold / Must Avoid
- Next-scene Trigger

## Non-negotiable boundaries

- 不写 Shot ID、景别、焦段、机位、构图、轴线投影、摄影机运动或逐镜时长。
- 不生成 Storyboard、Keyframe、Hero Frame、图片或任何 Prompt。
- 不改写锁定对白、故事结果或人物决定；发现问题返回 Screenplay/Treatment/Character。
- 不用“更有张力、电影感、压迫感”代替具体人物行动、空间关系或声音变化。
- 不把表演写成情绪命令；把“悲伤、愤怒、紧张”转成角色为达成目标采取的行为。
- 不为填字段添加人物目标、对抗、移动或转折；允许可观察的日常行为、沉默和感知积累。
- 不因资产未批准而虚构具体外貌或空间细节。

## Mode calibration

- **观察式：** 场景变化可来自重复行为的微差、停顿、协助边界和时间积累；不强制对抗高潮。
- **诗性 / 非线性 / 艺术表达：** 继承已批准的组织原则、时间逻辑和艺术规则，以感知、声音、重复或意象联系说明承接；不擅自添加剧情因果或超现实规则。
- **历史 / 现实：** 调度不得创造无依据关键行动或空间关系；需要特定位置才能成立时返回 Research。
- **幻想 / 科幻：** 世界规则必须通过人物能做与不能做的动作体现，不靠对白说明。
- **群像：** 为群体保留内部差异和多条行动路径，不用一个代表人物替所有人表态。

## Completion gate

- 请求范围内所有 Scene ID 都有设计且无跳过；
- 每场行动段的察觉、回应、变化或保持可连接，Function、Exit 与下一场按批准的时间/组织逻辑承接；
- 表演行动、调度和信息设计服务剧本；
- 主要人物的进入、变化和退出表演状态可传给相邻场景；
- 核心场景继承确切 Look/Light State，所有偏差都有叙事触发；
- Atmospheric Medium 的来源、分布和驱动力被继承，调度造成的变化有物理触发；
- 非物理艺术变化继承确切规则、触发与保持项，未被误判为物理错误；
- 声音来源、触发、静默与跨场 Bridge 可供镜头和剪辑继承；
- 每场节奏意图来自故事压力和人物行动，快慢变化有可见或可听触发；
- 世界坐标、资产状态和连续性得到继承；
- 调度没有超出已知空间证据，关键实体的数量、所有权、位置与知情状态闭合；
- 空间或动作连续性敏感的场景有可读方位卡，图中未知区域没有被当作已批准拓扑；
- Scene Review 为 PASS、无阻断项且所需 P0 用途在批准范围内才为 READY；文字完整与实际媒体验证分别记录；
- 没有提前进入摄影机、镜头、分镜或 Prompt。
