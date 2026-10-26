# Film Researcher Xianxia Sect End-to-End Test

- **Test Date｜测试日期：** 2026-09-17
- **Project ID｜项目编号：** FPD-20260917-宗门志测试
- **Input｜输入：** “我想出个各种宗门的修仙短片，有正道，邪道等等。”
- **Test Assumption｜测试假设：** 用户授权以“宗门志＋正邪镜像”为可撤销方向完成试跑。

## ARTIFACTS

- `projects/FPD-20260917-宗门志测试/project-brief.md`
- `projects/FPD-20260917-宗门志测试/research/research-pack.md`
- `projects/FPD-20260917-宗门志测试/research/source-index.md`

## OBSERVED BEHAVIOR

1. **Project Fidelity — 2/2**
   - 保留多宗门、修仙短片、正道与邪道。
   - “宗门志＋正邪镜像”标记为 `ASSUMED`，未冒充用户锁定决定。
2. **Local Knowledge Discipline — 2/2**
   - 只读检索默认 `claude-obsidian`。
   - 六组关键词无命中后如实记录；没有写入或扩大到其他 vault。
3. **Source Quality & Independence — 2/2**
   - 分开使用古典文本、遗产与文物机构、学术研究、专业评论和创作作品。
   - 明确评论共享来源及古典文化与现代类型研究的不同职责。
4. **Claim Traceability — 2/2**
   - `CLM-001` 至 `CLM-008` 均列来源状态；`SRC-001` 至 `SRC-018` 反向列出支持关系。
5. **Profile Fit — 2/2**
   - 使用 Myth, Xianxia & Fantasy。
   - 明确区分文化根系、现代类型惯例与原创提议。
6. **Research-first & Creative Reference Discipline — 2/2**
   - 在候选宗门方向前先研究资料。
   - 四部作品全部标记实际覆盖为评论、访谈、梗概或学术摘要，没有声称通读。
   - 每部作品均记录可迁移方法和不可复制项。
7. **Candidate Scoring — 2/2**
   - 四项候选均使用 `Research-grounded Summary`。
   - `Evidence Confidence` 按文化根系、类型区分与原创边界评分；`REFERENCE_ONLY` 未被当作事实证据。
8. **Handoff Quality — 2/2**
   - 给出组合式首要建议、安全依据、原创边界、视觉依据和未决问题。
   - 未输出故事、剧本、镜头、摄影参数或生成 Prompt。

## RESULT

- **Score｜得分：** 16/16
- **Hard Failures｜硬失败：** None observed
- **Status｜状态：** PASS

## ISSUES FOUND AND FIXED DURING TEST

1. `film-project-director` 在探索阶段过早二选一：已增加“先提供方向与代价，再以 ASSUMED 试跑”的规则。
2. `Factual Summary` 不适合原创幻想：已改为 `Research-grounded Summary`。
3. 原 `Evidence Confidence` 定义偏向历史事实：已增加科幻与修仙模式的研究支撑定义。
4. 原创宗门候选容易把作品参考当证据：已要求分开文化依据、类型参考和原创提议。
5. 首次生成时 `CLM-005` 误把 `CREATIVE_WORK` 放进已核实结论的支持来源：已拆分作品与评论来源，并改用 `PUBLIC_REFERENCE` 评论支持该结论。

## REMAINING NON-BLOCKING GAPS

- 用户尚未提供个人喜欢的修仙作品，因此代表作品组只能反映类型差异，不能代表个人审美。
- 未合法取得代表小说全文，本轮不能验证章节级结构与文风。
- 单集时长、平台和固定观察者尚未决定，应留给 Story Development 前的选择。
