# Research Pack Schema

本文件定义研究输出、候选评分和推荐门槛。V1 使用 Markdown，不创建 JSON 或数据库。

## 文件接口

```text
research/
├── research-pack.md
└── source-index.md
```

`research-pack.md` 负责结论、候选和交接；`source-index.md` 负责来源级追溯。两者使用相同的 `CLM-###`、`SRC-###` 和 `CAN-###` 标识。

## Research Pack 固定章节

1. `Project & Research Objective`
2. `Scope & Method`
3. `Source Coverage & Limitations`
4. `Obsidian Knowledge Overview`
5. `Creative Reference Study`（研究文学、影视、绘画、摄影、音乐、舞蹈等创作作品时出现）
6. `Research Findings`
7. `Visual Evidence Leads`
8. `Trend & Audience Signals`（仅按需出现）
9. `Candidate Topic Cards`
10. `Recommendation Groups`
11. `Research Gaps`
12. `Story Development Handoff`

Obsidian 未启用时仍保留第 4 节并写明原因。没有创作参考作品时省略第 5 节；趋势未启用时完全省略第 8 节。

## Scope Contract

在 `Project & Research Objective` 中固定记录：

- `Source Brief Version / Delivery Scope`：继承本次简报版本、交付范围与终止阶段；旧简报未提供的字段保持 OPEN，不擅自补锁定决定。
- `Research Task Mode`：`DIRECTION_DEEPENING / TOPIC_EXPLORATION`。方向已定默认深化；仅在用户仍探索或要求比较时启用选题模式。
- `Release Format`：继承 Project Brief，不自行改变；
- `Series Architecture`：继承 Project Brief；
- `Research Scope Unit`：`Standalone Film / Prototype Unit / Episodic Unit / Shared-world Foundation / Serial Arc / OPEN`；
- `Expansion Boundary`：本轮明确不研究或不决定的系列、分集和季级内容。

Release Format 为 `OPEN` 时使用 `Prototype Unit`，研究当前原型成立所需的最小充分范围。候选可注明扩展潜力，但不得据此把项目升级成系列。

## Creative Reference Study

每部参考作品记录：

- `SRC-###`、作品、作者与媒介；
- 选择理由和实际覆盖程度；
- 用户喜欢的具体方面（若已提供）；
- 可直接观察、阅读或聆听到的证据，必要时附作品、片段、章节或时间码；
- 对其叙事、情绪、视觉或制作作用的解释；
- 可迁移的品质或机制；
- 在本项目中如何低成本验证的 `REFERENCE HYPOTHESIS`；
- 不应复制的独特内容；
- 尚待深入分析的问题。

可增加 `Artistic Proposal / Intent / Contract Fit / Handoff Stage`，说明拟借鉴的方法如何服务本项目及其边界。ARTISTIC_PROPOSAL 与 REFERENCE HYPOTHESIS 是创作/验证标记，不是事实证据状态；不要求艺术意象在现实中发生过，也不把它写成历史事实。无提议不强行制造象征。

所有创作作品使用 `CREATIVE_WORK / REFERENCE_ONLY`。将作品中实际存在的内容、研究者解释和迁移建议分开书写；未实际覆盖的内容不得凭记忆补齐。该章节不为虚构内容背书，不提高候选的 `Evidence Confidence`。

## Candidate Topic Card

深化模式沿用既有 CAN ID（无既有卡时建立一张），注明 `Selection Basis` 的用户决定或批准来源；保留摘要、依据、视角、参考与风险字段，评分、总分、推荐分组及 Rationale 填 `NOT_APPLICABLE — 已定方向深化`。此卡供下游引用已选方向，不触发重复选择；Recommendation Groups 说明模式即可，不重新分组。探索模式使用下列完整候选卡与评分规则。

每张候选卡必须包含：

- `Candidate ID` 与工作标题；
- 一句话 `Research-grounded Summary`：历史、现实项目概括已核实事实，原创幻想项目概括“研究依据＋原创提议”；
- 与 Project Brief 的关系；
- 内容、文化或历史重要性；
- 已核实事实或文化依据及 Claim ID；
- 单一来源、争议与未知项；
- 可拍观察视角，但不展开故事；
- 视觉证据线索及 Source ID；
- 可选的创作参考方法及 Source ID；
- AIGC 制作风险；
- 六项核心评分、总分和推荐分组；
- 可选的独立 `Trend Signal`。

## 核心评分

本节及推荐分组的分数门槛用于需要事实/文化依据的 TOPIC_EXPLORATION；已定方向深化不强制评分。纯艺术表达探索且没有外部事实声明时，评分、总分和分组填 NOT_APPLICABLE，改用「意图契合 / 表达差异 / 制作风险」定性比较并等待方向选择，不用史实分数筛除想象。作品观察与 ARTISTIC_PROPOSAL 仍不作为 CONFIRMED 事实，也不靠多篇艺术参考提高 Evidence Confidence。

每项直接在其最高分范围内评分，并写一句依据：

- `Project Relevance`：0–20，是否直接服务主题、形式和用户锁定意图。
- `Significance`：0–20，内容本身是否具有足够的历史、文化、社会或概念价值。
- `Evidence Confidence`：0–20，按模式判断研究支撑是否足以承载该候选：
  - 历史与现实：关键事实的来源质量、独立性和争议程度；
  - 科学与科幻：现实科学依据、推测边界和设定一致性问题是否清楚；
  - 神话、玄幻与修仙：文化根系是否可追溯、类型惯例是否被正确区分、原创提议是否明确且已检查明显挪用风险。创作作品本身仍为 `REFERENCE_ONLY`，不能单独抬高此分。
- `Narrative Potential`：0–15，是否存在清晰的选择、变化、发现、关系或可观察过程。
- `Visual Potential`：0–15，是否有可验证且可区分的空间、人物行为、物件或环境依据。
- `AIGC Feasibility`：0–10，在角色一致性、场景规模、动作复杂度和可用素材方面是否适合当前制作。

总分为六项相加，满分 100。未知不得按满分处理；评分依据必须能回到当前研究证据。

## 推荐分组

- `PRIORITY / 优先制作`：总分 `>= 75`，`Evidence Confidence >= 14`，且没有会改变候选主体的重大未决事实。
- `BACKUP / 备选`：总分 `55–74`，或总分虽高但证据未达到优先门槛。
- `HOLD / 暂缓`：总分 `< 55`，存在重大来源冲突、核心事实无法确认，或制作风险尚无合理处理方式。

允许某一分组为空。不得为了凑够候选数量降低证据门槛。

## Trend Signal

趋势信号单独记录：

- 时间窗口；
- 实际覆盖平台；
- 支持来源；
- 信号强度 `Strong / Moderate / Weak / Insufficient`；
- 观察到的机会与风险；
- 数据限制。

Trend Signal 不参与 100 分核心评分，也不能改变证据状态。

## Story Development Handoff

只移交研究成果：Scope Contract、优先候选、可安全使用的事实或文化依据、必须保留的争议与原创边界、视觉依据和未决问题。不得在此撰写情节、角色弧、分集、季弧、场景或对白。

同时移交研究任务模式与选择依据、艺术提议及发展责任阶段，并记录 `G1 Readiness: READY / PARTIAL / RETURN`、具体证据及范围。READY 要求本次范围影响故事成立的关键问题已有充分依据，或已明确处于允许虚构范围；延期项须注明最晚解决阶段，不把模型可行性假设写成已验证。PARTIAL 只允许交接不依赖阻断项的范围；RETURN 列出会影响故事基础的未解问题。未达到 READY 时不能把全项目 G1 标为通过。

## Research Question Map

放入 Scope & Method，按问题记录：`Question / Type / Creative Decision / Priority / Finding & Evidence / Remaining Gap / Resolve By Stage`。Type 使用 FACT / ART_REFERENCE / FEASIBILITY；Priority 使用 BLOCKING_NOW / DEFERRED。事实结论回链 CLM/SRC，艺术观察回链实际作品范围，未测试可行性写 HYPOTHESIS。只有会影响当前交接的缺口才阻断当前范围；既不能无限收集外围资料，也不能把关键缺口伪装成延期细节。
