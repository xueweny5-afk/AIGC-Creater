---
name: film-story-developer
description: Turn a Film Project Brief, Research Pack, and selected candidate into a research-grounded Story Blueprint for a standalone film, prototype unit, episodic unit, or serial arc. Use after project definition and research, before character, treatment, screenplay, shot, or prompt development.
---

# Film Story Developer

把已经选定的项目方向和研究候选转换成可继续开发的 `Story Blueprint`。默认使用中文，保留稳定的英文字段名。故事可以原创，但必须持续区分用户决定、研究依据、创作提议和未知项。

开始前读取 [story-blueprint-schema.md](references/story-blueprint-schema.md) 与 [story-development-guide.md](references/story-development-guide.md) 的「组织与连贯性审阅」，再按项目模式读取其余相关部分。

## 输入与边界

必须读取：

- Film Project Brief；
- Research Pack 与 Source Index；
- 一个用户选定或明确授权试跑的候选方向。

研究为 DIRECTION_DEEPENING 时沿用已选方向与 Selection Basis，不要求重新评分或选择；TOPIC_EXPLORATION 则使用用户选定或授权试跑的候选。继承简报/研究版本、本次交付与终止阶段、G1 可交接范围、延期问题和 ARTISTIC_PROPOSAL。G1 PARTIAL 仅允许开发不依赖阻断项的范围，不得把局部依据扩大为全片就绪；旧资料缺新增字段时核对实质内容，不机械要求重做上游。

原作驱动项目还必须读取可用的 `Source Intake / Source Coverage`，并继承其中的版本、覆盖状态、Source Invariants、Adaptation Options 与 Do Not Assert。核心结局或人物关系位于未读范围时，返回 `SOURCE INTAKE RETURN`，不能凭简介补写。

同时继承 Project Brief 与 Research Pack 中的 `Release Format / Series Architecture / Scope Contract`。字段为 `OPEN` 时，只开发 `Prototype Unit`，不得称为“第一集”、设计季弧或假定角色将跨集复用。连续剧情剧集若未说明本次要开发单集、试播集还是季级弧线，只询问这一个范围问题。

如果没有候选方向，先返回 `film-researcher`；如果候选方向会因重大事实缺口失效，输出 `RESEARCH RETURN`，不得用虚构填平事实问题。

本 Skill 只产出故事蓝图，不得输出：

- Treatment、逐场大纲、完整梗概或场景清单；
- 成段对白、旁白全文或可直接拍摄的剧本页；
- 镜头、分镜、景别、机位、焦段、运镜、灯光、关键帧；
- 图像或视频生成 Prompt；
- 未经标记的重大历史事实、现实事件、科学结论或现有作品元素。

## 核心规则

1. **Preserve continuity.** Project Brief 中的 `LOCKED` 决定不可擅改；`ASSUMED` 可优化但必须继续标记；`OPEN` 不得被偷偷锁定。
2. **Preserve scope.** 发布结构是跨阶段契约。单支、原型、独立单元与连续弧使用不同的 `Blueprint Scope`，不得因为故事有扩展潜力就升级为系列。
3. **Research grounds; creation connects.** 研究决定什么可以安全使用，创作负责组织人物、选择、压力与变化。二者必须分别标记。
4. **Contract before expansion.** 先建立 `Original Story Contract`：输入事实、必须可见、允许的连接性补充和禁止改写；不得为了满足固定节拍而增加发现、牺牲、反转或高潮。
5. **Do not force one structure.** 根据项目选择 Event-driven、Character-driven、Dilemma-driven、Observational、Investigative 或 Poetic / Mosaic；不得把所有项目套成三幕剧、英雄旅程或升级爽文。
6. **One story engine.** 一个蓝图只选一个主要故事发动机；可有辅助模式，但不能把多个完整故事硬塞在一起。
7. **Production-aware, not production-led.** 角色数量、地点数量、群体动作与连续性风险应适合当前 AIGC 制作框架，但不得因制作方便改变项目核心。
8. **References are methods, not material.** 只迁移参考作品的方法与品质，不复制人物、专名、关系组合、力量体系、情节链、对白、文风或标志性场面。
9. **Source is material, not research proof.** 获准改编的原作内容可以成为故事材料，但原作内部说法不自动成为历史、现实或科学事实；忠实度、压缩、合并和视角变化必须显式记录。

## 工作流

1. **锁定输入与范围**：列出选定候选、`LOCKED / OPEN / ASSUMED`、可安全使用的 `CLM-###`、不可越过的原创边界，以及 `Release Format / Series Architecture / Blueprint Scope`。
   - 原作驱动项目同时建立 `Source Adaptation Contract`：版本与覆盖、必须保留、允许转换、待决定、不可宣称及 Source ID 回链。
2. **判断是否回研究**：若会改变本次故事基础的外部事实、文化依据或科学边界仍有关键缺口，输出 `RESEARCH RETURN` 与具体待核实问题。仅影响后续美术细节的延期项不阻断安全范围；已允许虚构的象征、梦境或抽象表达不因“现实未发生过”退回考证，仍须遵守项目真实性与锁定决定。
3. **建立 Original Story Contract**：逐条登记 `Input Fact / Must Be Visible / Allowed Connective Addition / Forbidden Rewrite`，并把每个必须呈现项映射到 Story Movement；安静或观察式题材不得被固定冲突模板改造成另一种故事。
4. **选择 Blueprint Scope 与故事发动机**：使用 `Standalone Film / Prototype Unit / Episodic Unit / Serial Arc`。独立系列可记录共同承诺、单元闭合和可选延续；连续弧可记录累积变化原则，但本阶段不生成分集表或季级 Treatment。再选择主要 Story Engine，并说明为什么适合。
5. **建立 Story Core**：定义 Story Premise、Story Question、Protagonist / Subject、Desire / Concern、Opposing Pressure、Stakes、Change Vector 和 Ending Principle。未知项可保持 `OPEN`。
6. **划定事实与原创空间**：历史、现实、科学项目列 `Safe Grounding / Creative Space / Do Not Assert`；幻想项目列 `Cultural Grounding / Type Convention / Original Proposal / Do Not Copy`。
7. **组织 Story Movement**：按内容所需数量组织抽象 movement，不设固定段数、不为填结构新增事件。先说明组织原则与时间逻辑，再写各段状态、行动/感知、变化、与前段的连接及情绪作用；首段连接写 OPENING。叙事以行动和后果推进，观察/诗性可用行为、时间、意象或认知关联推进；无对抗的压力与选择字段可具体标 NOT_APPLICABLE。不写场景地点、调度、对白或镜头。
   - 把拟采用的艺术提议转为 CREATIVE_PROPOSAL，说明它服务什么故事/情绪作用、由哪些 Movement 承担及合同边界。研究建议不是自动批准；不采用的参考无需逐项填表，也不为“高级感”强加象征。关键事件因果与必要时间线索必须可读，有意含混的解释范围可保留。
8. **定义人物功能**：只说明故事所需的角色功能、关系压力和信息位置，不写完整人物小传。没有固定主角时可用观察主体或共同体。
9. **检查连贯性、情绪与原创性**：按 guide 顺读，叙事检查条件—行动—回应—后果，观察/诗性检查关联原则与新增理解；核对段落连接、必要铺垫、重复中的差异、情绪积累与结尾回应。记录具体 Movement 证据、问题和修正，不用“顺畅、有诗意”代替审阅。不能靠改成线性叙事解决所有含混，也不能用艺术标签掩盖无意断裂或复制。
10. **制作可行性检查**：记录角色一致性、地点规模、群体场面、时间跨度、超自然规则和资产复用风险；只提出结构层面的收敛建议。
11. **输出与路由**：使用模板输出 Story Blueprint，在 Decision Register 记录 Story Review 的范围、证据、结论与阻断/延期项，再推荐唯一下一阶段：`Character Development`、`Treatment Development`、`Research Return` 或 `Source Intake Return`。只有当前蓝图范围完整且问题已解决才能正式交接；部分范围标 PARTIAL，表达或组织问题先在本阶段修正。Story Review 不代表整个 G2、独立冷读或用户批准。交接继续保持单片/原型/独立单元/连续弧边界，不新增审批门。

## Method overlay（采用时）

若 Adoption Receipt 将 Story 列入影响阶段，只应用其已登记的信息释放、反应、反转或节奏机制；项目 Premise、主题、因果、人物能动性和结局优先。Method 要求新增重大事件或复制参考故事时返回用户决定。

## 探索与决策

- 当用户仍在探索或明确要求建议时，可先提供 2–3 个 Story Approach，每个只写故事发动机、核心视角、主要优点和代价，不展开故事。
- 用户授权测试时，可选择推荐方案继续，但必须标记 `[ASSUMED · CREATIVE_PROPOSAL]`。
- 一个会改变主角、真实性承诺或结局性质的选择仍需用户决定时，只问一个关键问题；其余保持开放。

## 输出

默认写入：

```text
AIGC Creater/projects/<project-id>/story/
└── story-blueprint.md
```

使用 [story-blueprint-template.md](assets/story-blueprint-template.md)。不得覆盖 Research Pack、Project Brief 或不属于本次故事开发的文件。
