---
name: film-character-developer
description: Turn a standalone, prototype, episodic, or serial Story Blueprint into a compact, production-aware Character System with explicit cast continuity. Use after story development and before treatment, screenplay, visual character design, shot, or prompt work.
---

# Film Character Developer

把 Story Blueprint 中的人物功能发展为有行为依据、关系回应与明确变化范围的 `Character System`。默认使用中文，保留稳定英文字段名。人物设计服务既定故事；可以行动、观察、维持或拒绝，不用复杂身世代替行为逻辑。

开始前读取 [character-system-schema.md](references/character-system-schema.md) 与 [character-development-guide.md](references/character-development-guide.md) 的「行为与关系审阅」，再根据项目类型读取相关规则。

## 输入与边界

必须读取：

- Story Blueprint；
- Film Project Brief；
- Story Blueprint 使用的 Research Pack 与相关 Claim；
- 用户已锁定的人物决定，如有。

同时继承 `Release Format / Series Architecture / Blueprint Scope`。范围为 `Prototype Unit` 或发布结构仍为 `OPEN` 时，人物只能标为 `Prototype-only / OPEN`，不得自动定义为跨集固定角色。

继承蓝图/研究版本、本次交付与终止阶段、Story Review 与 G1 的可交接范围、组织原则、艺术提议及延期问题。上游 PARTIAL 只支持不依赖阻断项的范围；旧资料缺新增字段时检查实质内容，不要求重新填表才能开始。

如果人物作用、关系或行为依据不足以支持当前故事组织方式，返回 `STORY BLUEPRINT REVISION`；诗性/观察项目不因缺少主角目标或核心冲突自动返回。真实人物、文化身份或科学条件缺少影响本次创作的必要事实时返回 `RESEARCH RETURN`；已经允许的艺术表达无需伪造事实证明。

本 Skill 只产出人物系统，不得输出：

- Treatment、逐场大纲、完整梗概、剧本、对白或旁白；
- 镜头、分镜、景别、机位、表演调度、摄影参数；
- 图像或视频生成 Prompt、角色设定图或模型参数；
- 为制造“深度”而擅加的创伤、秘密血统、隐藏身份或重大反转；
- 未经标记的真实人物心理、历史行为、文化断言或现有作品元素。

## 核心规则

1. **Function becomes behavior with clear provenance.** 虚构角色具备符合其故事作用的行动、回应或观察依据，不按能力数量达标；真实人物的事实层只记录有据行为与权限，已授权戏剧化重构另行标记，不能冒称真实心理。观察主体保留独立生活与边界，不为填卡发明内心。
2. **Do not force a biography.** 只设计能解释当前选择的经历。观察式、群像或非虚构项目不必强造完整人物弧线。
3. **Conflict comes from legitimate logic.** 对立人物必须能从自己的信息、责任和代价出发合理行动，不能只是主题反方或纯粹阻碍。
4. **Protect affected people.** 承担制度后果、受害或求助的人物应有自身关注与边界，不能只用于教育主角。真实人物缺少某种权限时如实记录，不为人物能动性配额虚构知情、拒绝或改变历史的行动。
5. **Preserve uncertainty.** Story Blueprint 的 `OPEN` 不得被人物小传偷偷锁定；试跑选择标记为 `[ASSUMED · CREATIVE_PROPOSAL]`。
6. **References are not cast templates.** 不迁移参考作品的人物组合、关系结构、专名、语言习惯、标志性造型、秘密或人物弧线。
7. **Production-aware continuity.** 记录跨段必须稳定的身份、行为和概念级视觉锚点，但不进入造型方案、镜头或生成提示。
8. **Cast continuity follows scope.** 单片只判断当前故事必要性；独立系列区分 `Recurring / Unit-local`；连续弧可定义 `Arc-limited`，但不得用人物小传代替季弧。原型不承诺复用。

## 工作流

1. **建立 Continuity Contract**：提取 `LOCKED / OPEN / ASSUMED`、`Release Format / Series Architecture / Blueprint Scope`、Story Engine、Character Functions、相关 Claim 和原创边界。
2. **进行 Cast Audit**：判断功能应独立、合并还是由共同体承担，并记录 `Continuity Class`：`Standalone / Prototype-only / Recurring / Unit-local / Arc-limited / OPEN`。每次增删角色都说明对因果、视角或制作规模的影响。
3. **建立 Character Core**：先选择 `FULL_FICTION / EVIDENCE_LIMITED / OBSERVATIONAL`。虚构角色只发展与当前作用有关的核心；真实人物与观察主体事实层无依据的心理保持 UNKNOWN。用 `Dramatization Scope / Basis` 继承项目已授权的重构边界，拟采用的虚构心理或行为放入独立 `Dramatized Choices` 并标 CREATIVE_PROPOSAL；未授权则 NONE，不擅改真实性、关系或结局。
4. **检查 Agency 与行为依据**：核心角色说明目标/关注、可采取的策略及限制，配角按其信息或关系作用检查，艺术化形象按其体验作用检查，不为每人补全人格或成长弧。真实人物事实层只写有据权限，观察主体记录实际日常与边界；维持、等待、受限或不行动也可成立，但应有符合故事与证据的解释。
5. **建立 Knowledge & Belief Map**：分别记录知道的事实、相信但未证实的判断、误解和不能安全断言的内容。
6. **建立关系与回应**：记录依赖、冲突、权力、未说出口的需求和变化可能，并写 `Perception & Response Logic`：双方怎样理解或误读对方、为何回应、怎样影响下一步选择或关系感受。相互陪伴或有意无回应也可成立，不强制每段关系对抗；不写具体场景或示范对白。
7. **定义 Change Range**：说明人物可能改变、坚持或退缩什么，改变需要什么条件与代价；人物不变而关系或观众理解改变也可成立。用 `Change / Stability Basis` 回指蓝图段落与开放边界，不把坚持自动解释为缺陷，不提前锁死 OPEN 结局。
8. **定义 Voice & Behavior Tendencies**：用 `Behavior Logic` 连接关注/目的、通常策略、触发或限制、回应倾向，给后续写作提供依据。描述语言密度、回避方式和决策习惯，不停在“温柔、固执”等标签；不写口头禅、示范对白、微表情或表演调度。
9. **检查事实与原创性**：检查事实层与授权重构分开、幻想人物文化依据/类型惯例/原创选择分开，真实心理不被推断成事实；核对艺术化人物功能与相似性风险。
10. **审阅、输出与路由**：按 guide 检查人物行为、双方回应与变化/稳定依据，在现有 Decision Register 记录 Character Review 的范围、证据、结论和未解决项；问题先在本阶段修正，涉及故事或事实基础则返回正确上游。只推荐一个下一阶段：`Treatment Development`、`Story Blueprint Revision` 或 `Research Return`。审阅只覆盖人物系统，不代表独立冷读、用户批准或全 G2 通过，不新增审批门。

## Method overlay（采用时）

只在 Adoption Receipt 授权的字段内使用 Method 的表演、关系或反应机制；不得为适配类型而替换人物欲望、身份、选择或弧线。参考作品角色只能产生 Soft Method，不建立本项目角色事实。

## 探索与决策

- 用户仍在探索时，可提供 2–3 个 Character Approach，每个只比较视角、关系发动机、优势和风险，不展开小传。
- 用户授权试跑时，选择最少且最能承载故事因果的角色组合，并标记为 `ASSUMED`。
- 若一个未决项会改变主角、真实度承诺或人物最终责任，只询问一个关键问题；其他项目保持开放。

## 输出

默认写入：

```text
AIGC Creater/projects/<project-id>/characters/
└── character-system.md
```

使用 [character-system-template.md](assets/character-system-template.md)。不得覆盖 Story Blueprint、Research Pack 或 Project Brief。
