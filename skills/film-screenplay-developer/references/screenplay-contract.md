# Screenplay Contract

## Deliverables

### `screenplay.fountain`

人类可读的创作主版本，只包含标题页元数据、场景标题、动作、人物、对白、必要括号说明和有叙事意义的转场。

### `screenplay-register.md`

固定包含：

1. `Screenplay Identity`
2. `Continuity Contract`
3. `Coverage Status`
4. `Scene Function Index`
5. `State & Continuity Ledger`
6. `Dialogue & Voice Check`
7. `Grounding & Reconstruction Register`
8. `Production Load Snapshot`
9. `Decision Register`
10. `Next Stage`

## Scene Function Index

每场记录：

- `Scene ID`
- `Treatment Sequence`
- `Entry State`
- `Scene Function`
- `Character Action / Strategy`
- `Turn`
- `Exit State`
- `Knowledge Change`
- `Provenance`

场景功能不能只写“交代背景”“增强氛围”或“推动剧情”，要说明谁因何采取什么行动，使什么状态发生改变。

观察/诗性场景可说明可见可听的观察或感知如何延续、积累或改变体验；Turn、Knowledge Change 不适用时写 NOT_APPLICABLE 及理由，不制造转折以填表。

## State ledger

只记录会跨场影响后续的状态：

- 人物位置与身体条件
- 物件持有、损坏、隐藏或转移
- 人物已知、误解与公开信息
- 关系、承诺、拒绝和权力变化
- 未完成的行动与时间限制

本节包含 `Scene Connection Review`，使用 `From → To / Carryover / Allowed Change & Cue / Read & Findings`，记录行动、信息、关系、时间、声音或情绪如何承接，以及允许变化的依据。有意跳时/断裂保留必要线索；待修问题须指向具体 Scene ID，不能用“连续、自然”代替证据。

## Dialogue & Voice Check

检查对白/沉默的情境与关系作用、潜台词、人物差异、回应及重复说明，记录 Scene / Characters、Function & Subtext、Response & Voice、Findings。无需逐句写隐含解释；无对白项目写 NOT_APPLICABLE，不添加台词。

## Timing Review

放入 Production Load Snapshot，记录 `Method Status: ESTIMATED / TIMED / NOT_EVALUATED`、Scope / Method、Target / Total / Difference 和 Conflicts。实际计时覆盖不足时不能把全片标 TIMED；未知目标为 OPEN。明确目标的已知冲突须修正或列为阻断，估算不代替后续 Animatic 播放。

## Screenplay Review

放入 Decision Register，记录 `Result: PASS / REVISE / NOT_EVALUATED`、Scope & Evidence、Findings & Resolution 和审阅来源。按 guide 顺读后对照上游及场间状态，检查人物回应、连贯性、艺术内容可读性与结尾支撑。PASS 仅覆盖文本审阅；不代表独立冷读、用户批准或真实播放。正式交接视觉阶段还须 Coverage COMPLETE 且无影响交接的时长/连续性问题。

## Provenance

- `FACT`: Project Brief 或用户明确事实。
- `RESEARCHED`: 对应 Claim ID / Source ID。
- `RECONSTRUCTION`: 连接已知事实的合理重建，不得伪装成史料。
- `CREATIVE`: Treatment 已批准的虚构内容。
- 上游 `CREATIVE_PROPOSAL` 只有在其批准范围内才映射为 CREATIVE，未批准提议保持 OPEN 或 ASSUMED，不因转写剧本成为已锁定事实。人物的 Dramatized Choices 单列创作性质与授权依据，不覆盖 UNKNOWN 事实字段。
- `ASSUMED`: 剧本阶段新增的低风险临时决定。
- `OPEN / UNKNOWN`: 未决定或无依据。

## Coverage

- `COMPLETE`: 请求范围全部写成场景。
- `PARTIAL`: 只完成部分场景，必须列出剩余 Scene ID 和一个继续锚点。
- `RETURN`: 上游未 READY 或关键合同失效，不写剧本。

## Next stage

只选一个：

- `World & Visual Bible Development`
- `Treatment Revision`
- `Character Revision`
- `Research Return`
- `Continue Screenplay`
- `User Decision`

