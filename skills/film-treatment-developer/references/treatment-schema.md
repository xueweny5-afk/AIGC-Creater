# Treatment Schema

使用 `assets/treatment-template.md` 的固定一级与二级标题。字段可按题材精简，但不得删除 Identity、Continuity Contract、Readiness Gate、Complete Treatment、Sequence Map、Decision Register 和 Next Stage。

## Identity

- `Project ID`
- `Working Treatment Title`
- `Version`
- `Source Versions & Ready Scope`：简报、研究、蓝图与人物系统版本，本次交付/终止阶段及上游可交接范围；不得以局部依据宣称完成全片。
- `Release Format`
- `Series Architecture`
- `Blueprint Scope`
- `Character Scope`
- `Treatment Scope`: `Standalone Film / Prototype Unit / Episodic Unit / Serial Arc`
- `Scope Promise`: 本 Treatment 完成什么
- `Carryover Boundary`: 哪些状态不会被擅自扩展

## Status and provenance

- `[LOCKED]`: 用户或上游已确认，不能擅自改写。
- `[RESEARCHED]`: 可追溯到 Claim ID 或 Source ID。
- `[ASSUMED]`: 为完成 Treatment 所作的低风险临时选择，可撤回。
- `[OPEN]`: 仍待创作决定，但不阻断当前交付。
- `[UNKNOWN]`: 当前资料不能支持，尤其适用于真实人物内心和未证细节。
- `CREATIVE_PROPOSAL`：来源标记，用于明确继承或本阶段提出的创作连接、艺术方法与授权重构；另行保留其 LOCKED / ASSUMED / OPEN 决策状态，不能标成 RESEARCHED。

组合信息可写 `[RESEARCHED + ASSUMED]`，并说明哪部分属于哪一类。不要用 `[ASSUMED]` 绕过高风险决定。

## Readiness outcomes

- `READY`: 当前 Treatment 范围完整，正文与 Sequence Map 一致且 Treatment Review 为 PASS，可以交接剧本；不能由输入齐全直接填写。
- `TREATMENT DECISION GATE`: 只差一个会改变故事性质的用户决定。
- `RESEARCH RETURN`: 关键事实或现实依据不足。
- `STORY BLUEPRINT REVISION`: 核心问题、发动机、结局原则或因果骨架需重做。
- `CHARACTER REVISION`: 人物行为、回应、信息或关系依据不足以支撑既定过程；无外部目标或对抗的艺术形象不因此自动退回。

非 READY 的草稿或局部正文不得称为完整 Treatment 或正式交接；有上游阻断时只输出判断、证据、缺口和一个首要返回路径。普通组织或表达问题在本阶段继续修正，直到正文审阅通过，不制造新的用户审批门。

## Complete Treatment

写成连贯散文，而不是字段罗列。必须包含：

- 起始状态与观察入口；
- 触发变化的行动或过程；
- 每一步如何引出下一步，或时间、关系、意象与感知如何关联；
- 人物对信息或处境的回应，或维持状态的依据；
- 情绪从哪些关系、经历或认知变化积累；
- 适用时展开代价、选择与后果，不强制每部作品具有不可逆选择；
- 结束状态与余味。

长度服从项目复杂度，不设机械字数。短片可以短而完整；Serial Arc 可以更长，但不得退化成分集列表。

## Narrative Sequence Map

Sequence 数量服从完整过程与表达密度，不设默认段数、不为填数量新增事件。正文完成后建立映射，每段记录：

- `Start State`
- `Process / Action`
- `Choice / Response`
- `Consequence`
- `Information Change`
- `Emotional Movement`
- `Blueprint Mapping / Connection From Previous`：对应蓝图 Movement、承接前段的内容与方式，首段写 OPENING。
- `Provenance`

叙事 Sequence 是因果段落，观察/诗性 Sequence 可由时间、意象、关系或感知联系组织。Choice、Consequence 等字段不适用时注明 NOT_APPLICABLE 及作用，不捏造对抗来填表；Emotional Movement 应回指过程依据，不只列情绪词。Sequence 不是地点切换、场景标题或镜头清单。

## Supporting maps

- `Character Progression`: 核心人物开始位置、行动/回应与结束位置，或保持不变对关系/观众理解的作用；继承 Behavior Logic、Change / Stability Basis，不强制造成长。
- `Information & Causality Map`: 重要信息由谁知道、何时公开、造成何种行动；观察/诗性项目可记录必要时间线索与感知关联，不强连不存在的因果。
- `World / Rule Use`: 只记录影响过程、理解或体验的规则，不堆设定说明。
- `Grounding & Reconstruction Map`: 历史/现实题材将 Sequence 对应到 Claim、重建与创作连接；纯虚构项目可简写或省略。
- `Production Feasibility`: 角色量、地点量、时间跨度、复杂行动、连续性风险、潜在复用资产；不做视觉设计。

## Treatment Review

放入现有 Decision Register，使用 `Result: PASS / REVISE / NOT_EVALUATED`，记录 Scope & Evidence、Findings & Resolution 与审阅来源。先仅据正文复述并修正，再核对蓝图、人物系统与 Sequence Map；检查承接、回应、情绪积累、结尾支撑及授权重构边界，具体按 guide 执行。PASS 不表示用户批准、独立冷读或全 G2 通过；Readiness READY 另须符合当前范围完整性要求。

## Next Stage

只选一个：

- `Screenplay Development`
- `Research Return`
- `Story Blueprint Revision`
- `Character Revision`
- `User Decision`

必须给出一句可检验的理由。

