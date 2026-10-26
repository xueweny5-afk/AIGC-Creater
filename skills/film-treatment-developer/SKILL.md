---
name: film-treatment-developer
description: 将 Film Project Brief、Research Pack、Story Blueprint 与 Character System 发展为完整、可交接的电影或剧集单元 Treatment。用于故事方向和人物系统已形成，需要补全因果、行动、信息、情绪与结局，但尚未进入剧本、对白、场景调度、分镜、镜头或图像/视频提示词的阶段；也用于判断信息不足时应返回研究、故事或人物阶段。
---

# Film Treatment Developer

把已确认的故事骨架发展为可供剧本阶段使用的完整叙事或体验过程。Treatment 用连续散文展开行动、回应、关系与感知变化；叙事、观察和诗性项目按各自组织原则写完整，不强制采用同一种因果结构。

## Required inputs

优先读取：

1. `Film Project Brief`
2. `Research Pack` 与 `Source Index`（如有）
3. `Story Blueprint`
4. `Character System`
5. 用户本轮锁定的决定

缺少某份文件时不要伪造其内容。先判断缺失信息是否会改变故事性质、史实边界、人物能动性或结局；会改变则走 Gate 或 Return，不会改变则使用显式 `[ASSUMED]`。

## Load resources

- 开始工作前读取 `references/treatment-development-guide.md`。
- 需要创建或检查交付物时读取 `references/treatment-schema.md`。
- 写入项目文件时复制并填写 `assets/treatment-template.md`，不要改写固定标题。

## Workflow

1. **继承连续性。** 原样继承 Project ID、发布结构、Blueprint / Character Scope、LOCKED 内容及证据边界；记录 `Source Versions & Ready Scope` 与本次交付和终止阶段。接住蓝图的组织原则、时间逻辑、开放解释范围，以及人物的 Behavior Logic、Perception & Response Logic、Change / Stability Basis 和已授权重构。上游 PARTIAL 只支持不依赖阻断项的范围，不静默缩小用户要求后冒称完整；旧文件缺字段时核对实质内容，不要求重填上游。
2. **确定 Treatment Scope。** 只使用 `Standalone Film / Prototype Unit / Episodic Unit / Serial Arc`。发布结构仍 OPEN 但蓝图明确为 `Prototype Unit` 时，继续原型，不把它称为“第一集”。连续剧已锁定但本次要写单集、试播或阶段弧不明时，只问一个范围问题。
3. **运行 Readiness Gate。** 按组织模式检查故事/体验是否能展开、人物回应是否有依据、结尾原则是否可兑现；叙事检查因果，观察/诗性检查关系、感知或意象的积累，不把行动代价、冲突或不可逆选择设为所有作品的前提。影响故事性质、事实承诺或锁定结局的必要决定未定时走 TREATMENT DECISION GATE；不影响当前表达的开放项保留，不重复询问已批准决定。
4. **选择返回路径。** 证据不足则 `RESEARCH RETURN`；故事核心失效则 `STORY BLUEPRINT REVISION`；人物动机或权利结构无法支持行动则 `CHARACTER REVISION`。每次只给一个首要路径。
5. **先写完整过程，再建立映射。** 用连续散文写清起始、推进、回应、信息/感知变化、情绪积累和结束。叙事说明行动为何引出下一步；观察/诗性说明时间、重复、记忆或意象怎样连接和改变体验。拟采用的艺术方法落实为有作用的过程，不只出现“梦境、象征”等标签；不在此处规定镜头或表演动作。再用 Narrative Sequence Map 回查正文与蓝图，不由表格拼凑故事，也不为段数配额新增事件。
6. **标注来源。** 区分 LOCKED / ASSUMED / OPEN 与 RESEARCHED / CREATIVE_PROPOSAL / UNKNOWN，保留已有标记含义。历史/现实把可证事实、重建与创作连接分开；人物已授权的 Dramatized Choices 可作为独立创作层展开，但不能替代未知事实或扩大重构范围。
7. **检查制作约束。** 只记录角色、地点、时间跨度、复杂行动、连续性与潜在资产负担，不设计造型、构图、镜头或生成方法。
8. **顺读、修正并保存。** 先仅读 Complete Treatment，复述行动或体验路径，检查回应遗漏、跳变、重复、情绪铺垫及结尾支撑；再对照 Sequence Map、故事合同与人物系统定位修正。现有 Decision Register 记录 Treatment Review 的范围、具体段落证据、审阅来源与结论；自检注明 SELF-AUDIT。只有正文与映射一致、当前范围完整且审阅通过，Readiness 才为 READY；问题按责任返回，不让表格齐全代替完成。默认保存为 `AIGC Creater/projects/<project-id>/treatment/treatment.md`，不新增审批门或宣称全 G2 已通过。

## Method overlay（when adopted）

仅当 Treatment 在 `Affected Stages` 中时，读取对应 `film-method-*` 的结构与节奏覆盖，把它落实为完整可见过程；用户意图、Story Blueprint、Character System 和研究事实优先。影响过程但未在上游批准的 Method 改动必须返回 Story/Character，而不是在 Treatment 中静默加入。

## Non-negotiable boundaries

- 不输出剧本格式、场景标题、对白段落、旁白全文或表演调度。
- 不输出镜头、分镜、景别、焦段、机位、运镜、关键帧、人物六视图或图像/视频 Prompt。
- 不把 Sequence 当作 Shot、Scene 或 Beat Sheet 的伪装。
- 不为制造“完整性”擅自加入反派、死亡、疾病、灾难、背叛、身世秘密或大反转。
- 不把 Prototype Unit 扩展成剧集圣经、季弧或跨集悬念。
- 不复制参考作品的剧情、专名、人物关系、标志性表达或可识别结构组合。
- 不从历史结果反推真实人物的内心、对白或预知能力。

## Mode-specific rules

- **历史与真实事件：** 事实层因果由可追溯行动支撑；关键命令链、空间关系或物件依据不足且影响事件成立时返回研究。已授权的艺术重构独立标创作性质，不以结局反推真实心理、不填造史实。
- **人文与情感：** 可由时间、劳动、空间和关系节律推进，结尾也可以是习惯延续、关系或观众理解的变化；不强制冲突升级、反派、传统高潮或不可逆行为。
- **诗性与实验：** 继承蓝图的时间/意象关联和开放解释范围。梦境、象征、抽象或非线性过程须具有可感知的承接与作用，不强制改为线性剧情；明确需要理解什么、感受到什么、保留什么解释，不把未完成冒称开放结尾。
- **科学与科幻：** 明确现实科学、推演和虚构规则；关键规则须在行动后果中保持一致。
- **神话、修仙与幻想：** 通过选择与代价呈现规则，避免设定说明堆积。改变“代价由谁承担”的机制属于高风险决定，必须先 Gate。

## Decision-gate format

当存在一个阻断问题时，只输出：

```markdown
# TREATMENT DECISION GATE

- **Project ID：** ...
- **Blocking Decision：** ...
- **Why It Matters：** ...
- **Current Safe Scope：** ...
- **Question：** ...？
- **After Answer：** Treatment Development
```

只问一个问题。可在同一句中给出二至三个互斥方向，但不要同时追问片长、平台或其他非阻断项。

## Completion standard

只有同时满足以下条件才推荐 `Screenplay Development`：

- 当前范围从开端到结束完整，叙事有可解释因果，观察/诗性有可感知关联及体验积累；
- 人物行动、回应或维持状态来自既有人物系统，关系与信息未凭空重置；
- 观众的信息/感知路径及必要时间线索清楚，有意开放的解释范围明确；
- 结局兑现 Blueprint 的 Ending Principle；
- 所有重大新增均有状态与来源；
- 范围与发布结构一致；
- Complete Treatment 经顺读修正且与 Sequence Map 一致，情绪积累与结尾支撑有具体证据，Treatment Review 为 PASS；
- 没有越界进入剧本、镜头或 Prompt。
