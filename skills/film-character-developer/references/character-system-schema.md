# Character System Schema

V1 使用 Markdown。Character System 是 Story Blueprint 与 Treatment 之间的人物接口，不是人物百科、剧本或视觉设定稿。

## 标记规则

### 决策状态

- `LOCKED`：用户已经确认，下游不得擅改。
- `OPEN`：尚未决定，不得被小传细节偷偷锁定。
- `ASSUMED`：为试跑采用的可撤销决定。

### 内容来源

- `USER_FACT`：用户明确决定。
- `RESEARCHED`：能回到 Research Pack 的 `CLM-### / SRC-###`。
- `CREATIVE_PROPOSAL`：本阶段原创的人物、关系或行为设计。
- `UNKNOWN`：没有依据或仍待决定。

已填决定使用 `[状态 · 来源]`。真实人物的公开行为不等于可确认的内心动机。

## 固定章节

1. `Character System Identity`
2. `Continuity Contract`
3. `Cast Audit`
4. `Core Character Cards`
5. `Relationship System`
6. `Agency & Information Map`
7. `Group / Community Design`（仅在适用时保留）
8. `Originality & Reality Boundaries`
9. `Production Continuity`
10. `Decision Register`
11. `Next Stage`

## Scope & Cast Continuity

在 `Character System Identity` 中记录 `Release Format / Series Architecture / Blueprint Scope / Character Scope`，同时记录 `Source Versions & Ready Scope`：蓝图/研究版本、本次交付与终止阶段、上游审阅可交接范围及延期问题。部分范围不能支持依赖缺口的角色设计；旧资料缺字段时检查实质依据，不强制重做上游。

每个 Cast Audit 项增加：

- `Continuity Class`：`Standalone / Prototype-only / Recurring / Unit-local / Arc-limited / OPEN`；
- `Reuse Evidence`：为何需要或不需要跨单元复用；
- `Accumulation Boundary`：允许跨单元累积的关系、知识或状态。

发布结构为 `OPEN` 或 Blueprint Scope 为 `Prototype Unit` 时，默认 `Prototype-only`，不得声称人物是固定主角、常驻角色或可复用资产。`Recurring` 必须来自用户已确认的系列结构和故事需要，不能只因为 AIGC 复用方便。

## Character Card

每位核心角色仅记录能改变故事选择的字段：

- `Role ID / Working Name`
- `Profile Mode`：`FULL_FICTION / EVIDENCE_LIMITED / OBSERVATIONAL`
- `Narrative Function`
- `Public Position`
- `External Objective`
- `Inner Need / Concern`
- `Fear / Pressure`
- `Contradiction`
- `Worldview & Self-Justification`
- `Moral Line / Limit`
- `Agency & Choice Power`
- `Knowledge / Belief / Misunderstanding`
- `Relationship Pressures`
- `Change Range & Cost`
- `Voice & Behavior Tendencies`
- `Behavior Logic`：关注/目的、通常策略、触发或限制、回应倾向；不写具体场景和表演动作。
- `Change / Stability Basis`：人物或关系改变的条件，或保持不变对故事/观众理解的作用及 Movement 依据。
- `Dramatization Scope / Basis` 与 `Dramatized Choices`：继承已授权范围和来源；拟采用的重构心理或行为另列 CREATIVE_PROPOSAL。无授权写 NONE，不能覆盖未知的事实字段。
- `Continuity Anchors`
- `Open Questions`
- `Provenance`

不要求每个人都有创伤、秘密、反转或完整成长弧。`EVIDENCE_LIMITED` 与 `OBSERVATIONAL` 中无依据的心理字段应写 `UNKNOWN / 不作断言`，而不是以推断补空白。

## Cast Audit

每个 Story Blueprint 人物功能选择：

- `KEEP`：必须成为独立角色；
- `MERGE`：与另一功能合并，说明不会损失的因果信息；
- `COMMUNITY`：由小型共同体承担；
- `REMOVE`：没有独立行动或压力价值。

记录 `Reason`、`Continuity Class` 和 `Production Impact`。人数不能多于故事实际需要。

## Agency Test

以下是按故事作用检查的参考维度，不设数量门槛、不要求每人全具备：

- 能主动追求一个外部目标；
- 能拒绝一种安排；
- 掌握会影响他人决定的信息或资源；
- 能作出带来代价的选择；
- 其决定会改变关系、风险或信息分布。

核心角色检查其行为/回应能否支持蓝图，配角检查必要的信息与关系作用，艺术化形象检查体验功能。受影响者或求助者保留独立关注与边界，缺少某种权限时如实记录，不为帮助主角成长而强加改变意愿或虚构行动权。

`EVIDENCE_LIMITED` 的事实层只记录有据行动、职权、限制和后果，无依据保持 UNKNOWN；项目已授权的戏剧化选择另列，不混入 RESEARCHED。`OBSERVATIONAL` 的 agency 可表现为日常、习惯、边界或受限处境，不要求制造转折。非对抗或艺术项目的外部目标、恐惧、冲突、代价等不适用时可写 NOT_APPLICABLE 并说明作用；真实人物事实未知仍用 UNKNOWN，不能改成“不适用”规避证据。

## Relationship System

每组关键关系包含：

- `Dependency`
- `Conflict`
- `Power Asymmetry`
- `Unspoken Need`
- `Change Possibility`
- `Perception & Response Logic`：双方的理解或误读、回应或不回应的依据，以及对后续选择/关系感受的影响。未被研究支持的真实心理不作断言，授权重构另列。

关系可以是压力、陪伴或持续观察，不要求每组都有冲突与权力不对称；不适用项注明理由。不写相遇、争吵或告别等具体场景。

## Character Review

放入现有 Decision Register，记录 `Status: READY / REVISE / PARTIAL`、Scope & Evidence、Blocking / Deferred Issues。按 guide 审阅行为、关系回应、变化/稳定及重构边界；这是当前人物范围的交接结论，不代表整个 G2、独立冷读或用户批准。

## Production Continuity

只记录跨生成阶段需要稳定的概念锚点：身份层级、年龄带、体态倾向、显著但非作品专属的识别原则、固定携带物的故事功能、行为节律和不可变化项。具体服装设计、色板、脸型、镜头和 Prompt 交给后续视觉阶段。

## 完整性要求

- 所有角色能回到 Story Blueprint 的功能或明确说明新增必要性。
- 人物具备符合故事作用的行为或回应依据；真实人物与观察主体没有为了行动力而被虚构事实。
- `OPEN` 结局没有被人物弧线提前锁死。
- `RESEARCHED` 可追溯，原创内容标记清楚。
- 真实人物事实层不被虚构内心、私密对白或未证实行为覆盖，授权重构独立标明范围、来源与创作性质。
- 关键关系的双方回应有依据，人物改变或保持不变均与蓝图兼容；审阅记录指向具体角色、关系和段落。
- 下一阶段只有一个首要建议。
- Cast Continuity 与 Blueprint Scope 一致；制作复用不得反向锁定创作结构。
