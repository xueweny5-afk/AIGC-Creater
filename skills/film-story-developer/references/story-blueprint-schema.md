# Story Blueprint Schema

V1 使用 Markdown。Story Blueprint 是研究与剧本之间的稳定接口，不是 Treatment 或场景大纲。

## 标记规则

### 决策状态

- `LOCKED`：用户已确认，下游不得擅改。
- `OPEN`：尚未决定。
- `ASSUMED`：为了试跑采用的可撤销决定。

### 内容来源

- `USER_FACT`：用户明确决定。
- `RESEARCHED`：能回到 Research Pack 的 `CLM-### / SRC-###`。
- `CREATIVE_PROPOSAL`：本阶段提出的原创连接、人物功能或结构选择。
- `UNKNOWN`：尚无依据或尚待决定。

已填决定使用 `[状态 · 来源]`。研究与创作同时参与时并列说明，不能把 `CREATIVE_PROPOSAL` 写成 `RESEARCHED`。

## 固定章节

1. `Story Identity`
2. `Continuity Contract`
3. `Original Story Contract`
4. `Source Adaptation Contract`（仅原作驱动项目）
5. `Story Core`
6. `Story Engine`
7. `Grounding & Fiction Boundary`
8. `Character Functions`
9. `Conflict, Stakes & Change`
10. `Story Movement`
11. `Emotional Design`
12. `Originality & Reference Boundaries`
13. `Production-Aware Story Constraints`
14. `Decision Register`
15. `Next Stage`

## Original Story Contract

每条输入事实或用户锁定意图建立稳定 `OSC-###`，记录：

- `Input Fact / Intent`：用户输入、研究候选或原作中确实存在的内容；
- `Must Be Visible`：下游必须通过行动、结果或明确可见证据呈现的内容；
- `Allowed Connective Addition`：为了连贯允许增加但不得冒充事实的连接；
- `Forbidden Rewrite`：会改变项目性质、主体、真实性或结局原则的改写；
- `Movement Mapping`：该项由哪些 Story Movement 承担。

没有 `Must Be Visible` 的背景事实可以只作为语境。扩充篇幅时优先把已有锚点拆为原因、行动和结果，不新增独立事件来填数量。

## Source Adaptation Contract

记录 `Source Intake Version / Coverage`、`Source Invariants`、`Adaptation Choices`、`Open Decisions`、`Source IDs Used` 和 `Do Not Assert`。它只在原作驱动项目出现。来源为 `PARTIAL` 时，不得把未读内容写入 Story Core；改编选择使用 `CREATIVE_PROPOSAL`，不能伪装成原作事件或研究结论。

## Blueprint Scope

在 `Story Identity` 中固定记录：

- `Release Format`：继承 Project Brief；
- `Source Versions & Ready Scope`：简报/研究版本、本次交付与终止阶段、G1 可交接范围及受延期问题影响的内容；深化模式沿用已选 CAN ID 与选择依据，不强制重新选题。
- `Series Architecture`：继承 Project Brief；
- `Blueprint Scope`：`Standalone Film / Prototype Unit / Episodic Unit / Serial Arc`；
- `Scope Promise`：当前蓝图必须完成什么；
- `Carryover Boundary`：什么可以延续到其他单元，什么不得在当前阶段假定。

Release Format 为 `OPEN` 时使用 `Prototype Unit`。不得写“首集”“首季”“固定跨集主角”或系列资产承诺。独立系列只记录单元闭合与共享原则，不列选集；连续弧只记录累积变化逻辑，不写分集大纲。

## Story Core

- `Story Premise`：一个可持续产生选择与变化的基本故事情境，不是完整梗概。
- `Story Question`：故事通过行动与后果探索的问题。
- `Protagonist / Subject`：主角、观察主体或共同体。
- `Desire / Concern`：主体当前追求或无法回避的问题。
- `Opposing Pressure`：阻碍、制度、环境、关系或内在矛盾。
- `Stakes`：失败或不改变会失去什么，不要求一定是生死。
- `Change Vector`：人物、关系、环境或观众认知可能怎样变化。
- `Ending Principle`：结局需要完成的意义或状态，不写具体结局动作。

观察、诗性或实验项目可用关注与体验变化表述 Story Core；Opposing Pressure、Stakes 不适用时注明 NOT_APPLICABLE 及理由，不因字段存在而制造对抗或损失。

## Story Engine

只选择一个主要模式：

- `Event-driven`
- `Character-driven`
- `Dilemma-driven`
- `Observational`
- `Investigative`
- `Poetic / Mosaic`

可增加一个辅助模式，但必须说明分工。

记录 `Organizing Principle / Temporal Logic`，说明主要观看动力、材料的关联原则与时间逻辑。因果、时间、记忆、意象和平行对照都可成立；非线性作品区分必要的事件时间线索和呈现逻辑，不把有意重组当成连续性错误。

## Grounding & Fiction Boundary

事实型项目：

- `Safe Grounding`：可直接使用的研究结论及 Claim ID。
- `Creative Space`：允许虚构的连接、复合人物、视角或未记录细节。
- `Do Not Assert`：不能写成事实的内容。

幻想项目：

- `Cultural Grounding`：可追溯的文化依据。
- `Type Convention`：类型共同惯例，不宣称为传统事实。
- `Original Proposal`：本项目原创设定。
- `Do Not Copy`：现有作品不可迁移的独特内容。

艺术/实验项目可将符号、梦境或抽象表达放入 Original Proposals；从研究继承的 ARTISTIC_PROPOSAL 只有拟采用时才映射为本阶段 CREATIVE_PROPOSAL，继续保留其来源与决策状态。每项记录 `Artistic Method / Story-Emotional Function / Movement Mapping / Contract Boundary`，不在此处规定构图、运镜或提示词。无采用项写 NONE。艺术提议不冒充已核实的外部事实或已批准决定。

## Character Functions

每个功能项只记录：

- `Function`：在故事中制造选择、压力、信息或情感关系的作用；
- `Relationship Pressure`：与主体之间的张力；
- `Knowledge Position`：知道什么、不知道什么；
- `Status`：是否需要下一阶段发展为完整人物。

不为填表而新增角色。两个功能可由一人承担时保持精简。

## Story Movement

按内容所需数量组织抽象段落，模板中的段落块可按需复制并保持稳定编号，不设固定段数。每段包含：

- `State`：当前状态；
- `Pressure / Discovery`：新增压力或发现；
- `Choice / Response`：主体的选择或反应；
- `Change`：状态、关系或认知变化。
- `Connection From Previous`：前段留下的行动、问题、时间、意象或体验，以及本段怎样承接；首段写 OPENING。
- `Emotional Role`：此段延续或改变什么感受，依据是什么；不只列“悲伤/温暖”等结果词。

压力、选择等不适用时写 NOT_APPLICABLE 并说明观察或感知过程，不虚构对抗以填表。Conflict, Stakes & Change 中的冲突、代价、升级与不可逆变化也按模式判断，不适用项允许标明理由。Movement 是故事组织骨架，不是拍摄顺序；不得写具体场景、对白、镜头或逐场事件列表。

## Emotional Design & Story Review

Emotional Design 记录起始、变化、结束感受与观众余味，并用 `Ending Setup & Response` 回指结尾所回应的 Movement；`Intended Clarity / Open Interpretation` 区分必须可读的内容与有意开放的解释，非含混作品可以写 NONE。结尾未定保持 OPEN，不为通过审阅补写未经批准的结局。

Decision Register 内记录 `Story Review: READY / REVISE / PARTIAL`、Scope & Evidence、Blocking / Deferred Issues；具体按 story-development-guide 的审阅执行。它只证明对应蓝图范围的连贯性与情绪组织，不能标为独立冷读、用户批准或整个 G2 已通过。

## 完整性要求

- 所有 `LOCKED` 能回到用户输入。
- 所有 `RESEARCHED` 能回到 Claim / Source。
- 历史、现实和科学项目明确 `Do Not Assert`。
- 幻想项目明确 `Original Proposal` 与 `Do Not Copy`。
- Story Movement 的变化有因果或适合模式的关联依据，关键段间承接与情绪作用明确。
- 结尾回应有前文支撑，重复包含差异或有意停留价值；必要可读内容与开放解释范围分明。
- 拟采用的艺术方法能回到故事/情绪作用、Movement 与合同边界，不能只提供装饰标签。
- 每个 `Must Be Visible` 均有 Movement Mapping，且没有为了结构配额新增重大事件。
- Production Constraints 不得反向篡改项目主题。
- Next Stage 只给一个首要建议。
- Blueprint Scope 与上游 Release Format 一致；原型不得被暗中当作第一集。
