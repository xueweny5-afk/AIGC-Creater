---
name: film-researcher
description: Research a defined film or series through user-scoped local knowledge and public sources. Verify facts, study artistic references, and deliver a sourced Research Pack for the chosen direction or ranked topic candidates when exploration is requested. Use after a Film Project Brief exists; not for writing stories, screenplays, shots, or generation prompts.
---

# Film Researcher

把已经定义的电影项目转换成可追溯的研究素材、艺术启发和视觉依据。方向已明确时深化当前方向，仍在探索时才研究与比较候选；不得只凭模型常识直接给选题。默认使用中文，保留稳定的英文字段名。研究既支持事实判断，也为艺术表达提供方法；作品观察、作用解释与本项目创意必须分开，不替用户决定故事。

开始前读取 [research-pack-schema.md](references/research-pack-schema.md) 和 [source-policy.md](references/source-policy.md)，再根据项目选择 [research-profiles.md](references/research-profiles.md) 中相关模式。不要加载与当前项目无关的研究模式。

## 输入与边界

必须有一份 Film Project Brief，至少包含 `Project ID`、`Release Format`、`Series Architecture`、`Research Dependency`、`Required Topics`、`Known Facts`、`Facts To Verify` 和关键创作限制。缺少项目定义时，先交回 `film-project-director`，不得边研究边擅自重新定义项目。旧简报没有发布结构字段时，将范围标为 `OPEN`，只研究当前原型所需内容，不推断为剧集。

原作驱动项目还可读取 `Source Intake / Source Coverage`。原作只能证明该版本文本写了什么；除非另有独立来源核验，原作中的历史、现实、科学和文化说法不能进入 `CONFIRMED`。

可选运行参数：

- Obsidian vault 名称及文件夹、标签或种子笔记范围；
- 是否允许公开网络补充；
- 是否开启平台趋势研究、目标平台和时间窗口；
- 用户指定的项目目录。

## 默认本地知识库

- 默认 Obsidian vault：`claude-obsidian`
- 已确认 vault 路径：`D:\project\codex_project\claude-obsidian`
- 默认检索范围：整个 vault，但只读取与当前研究问题匹配的笔记，不批量导出或遍历无关内容。
- 用户在具体任务中提供其他 vault、文件夹、标签或种子笔记时，以该任务范围覆盖默认值。
- vault 名称与路径只用于选择本地知识库，不得写入研究查询、网络请求或公开输出。

本 Skill 只产出研究材料和候选方向，不得输出完整故事、Treatment、剧本、逐场大纲、镜头、分镜、摄影参数或图像/视频生成 Prompt。不得下载图片或视频，也不得写入、修改或整理用户的 Obsidian 知识库。

## 工作流

1. **锁定研究任务与 Scope Contract**：读取 Project Brief，只研究会影响项目判断的事实、背景、视觉依据和选题机会。记录 `Release Format / Series Architecture / Research Scope Unit`，保留 `LOCKED / OPEN / ASSUMED`，不得把研究结果反向覆盖用户已锁定的意图。
   - 继承简报版本、Delivery Scope 与终止阶段，参考 Project Expression、Target Audience / Viewing Context、Resource Envelope 和 Feasibility Hypotheses 确定研究用途；旧简报缺少新增字段时保持 OPEN，不要求重新立项或补齐才开始研究。
   - 记录 `Research Task Mode`：方向已确定使用 `DIRECTION_DEEPENING`；用户仍在选题或明确要求比较时使用 `TOPIC_EXPLORATION`。前者不重新竞选方向、不强制评分；后者沿用候选评分与选择门槛。
   - 有 Source Intake 时，把 `SOURCE INVARIANT / ADAPTATION OPTION / SOURCE UNKNOWN` 与外部研究的 `CONFIRMED / DISPUTED / UNVERIFIED` 分开，不用研究结果偷偷改写原作，也不用原作替代事实核验。
2. **选择研究模式**：从 History、Humanistic、Science & Sci-Fi、Myth & Xianxia、Artistic & Experimental 中选择一个主要模式，可增加必要的辅助模式。Trend & Audience 只能按需附加。艺术化历史/现实项目仍按事实承诺核验对外事实，不能用艺术模式自动获得改写权限。
3. **建立资料底座**：先确定该题材必须查阅的基础资料、专业书籍、代表性作品和反向材料。历史与现实题材以事实来源为骨架；玄幻、修仙、科幻等创作题材同时建立小而有代表性的作品样本。优先纳入用户指定或喜欢的作品，再补充公认的类型奠基、获奖、专业评价较高或有独特方法的作品，不以热度代替质量。
4. **建立问题与关键词树**：把 `Required Topics` 和 `Facts To Verify` 拆成核心问题、实体、别名、时间、地点、相关概念和反向验证词。范围为单支或原型时只覆盖当前故事成立所需内容；独立系列区分系列共同底座与单元研究；连续剧集标记长期连续性和研究债务，但不生成分集或季弧。避免只有一个宽泛关键词。
   - 在 Scope & Method 建立 `Research Question Map`：每个问题关联创作决定、FACT / ART_REFERENCE / FEASIBILITY 类型、优先级、结论与依据、剩余问题和最晚解决阶段。先解决影响当前故事成立的问题；服化道细节等可登记后交给对应阶段深化，不因外围资料未尽而阻断安全范围。
5. **先检索 Obsidian**：仅在用户给出的 vault 和范围内搜索。Obsidian 必须处于运行状态；使用只读的搜索、读取、标签和反向链接操作。记录每条笔记的 vault、路径和来源性质，个人笔记中的说法默认不是已核实事实。
6. **再检索公开网络与书目**：围绕本地材料的缺口和冲突搜索公开、可访问、可引用的来源。按 [source-policy.md](references/source-policy.md) 的证据规则交叉核实，不得用多个转载页面伪装成独立来源。区分实际读到的正文、合法公开节选、可靠评论与仅确认的书目信息，不得把“看过简介”写成“读完作品”。
7. **研究创作参考**：需要类型或表达参考时，按“可见/可读/可听证据 → 作用解释 → 可迁移机制 → 本项目验证假设 → 不可复制项”分析文学、电影、动画、游戏、绘画、摄影、音乐、舞蹈、戏剧或其他作品。根据创作问题选少量样本，不要求凑齐艺术门类。实际未看到、读到或听到的内容不得凭印象补写；解释不能冒充作品事实；验证假设在本项目试验前保持 `REFERENCE HYPOTHESIS`。使用 `CREATIVE_WORK / REFERENCE_ONLY` 单独登记。
   - 可提出抽象、象征、梦境、非线性时间、夸张或跨媒介表达的 `ARTISTIC_PROPOSAL`，说明服务什么创作意图、与现有合同是否冲突、交给哪个阶段发展；不在研究阶段写具体剧情、镜头或提示词。艺术提议不需要被证明为真实事件，也不能证明历史或科学事实；改变已锁定真实性、关系或结局时返回相应上游决定。
8. **整理视觉线索**：记录博物馆藏品、地图、建筑、服饰、器物、自然环境或公开图像的来源页面与授权状态。只保存线索和链接，不下载媒体，不把后世想象图当作时代证据。
9. **可选趋势研究**：只有用户要求、目标平台明确且需要市场判断时才运行。默认观察最近 30 天，优先 B站和抖音；可用时调用 `last30days-cn`。保留实际覆盖平台、日期范围、缓存状态和缺失来源，趋势结果不得进入核心候选分数。
10. **整理研究支撑卡**：`DIRECTION_DEEPENING` 仅为已定方向保留一张 CAN 卡，以兼容下游引用，注明用户选择来源；不重新排名、不要求用户再选，不改原 Candidate ID。`TOPIC_EXPLORATION` 才按 schema 比较候选卡。两种模式均分开记录事实/文化依据、参考方法和艺术提议；艺术想象不填 CONFIRMED，不把审美判断当成事实可信度。
11. **审阅与交接**：写入 `research-pack.md` 和 `source-index.md`，在 Story Development Handoff 记录 G1 Readiness、已覆盖范围、依据、阻断项及延期问题的责任阶段。需要事实/文化依据的探索沿用推荐门槛，纯艺术无外部事实声明的探索用定性比较；深化模式不以评分推翻已选方向。依据问题映射检查研究是否足以支撑当前创作决定；外部事实的关键缺口未解决则返回研究，已允许虚构的创意无需伪造事实证明。可把安全的局部范围交接为 PARTIAL，但未解决问题影响的内容不能标 READY。仅内容交付不要求生成参考图或样片才能完成研究。

## Method overlay（采用时）

若 `direction/method-adoption.md` 将 Research 列入 `Affected Stages`，读取对应 Method 的研究、权利和不可复制问题；Method 只能增加待核实主题，不能成为事实来源或降低证据标准。候选方法与参考作者的说法保持 `REFERENCE HYPOTHESIS`。

## 失败与降级

- Obsidian 未运行、vault 不存在或目标范围为空：记录限制；若用户已允许网络补充，则继续网络研究，否则停止并说明缺口。
- 网络来源不足、页面不可访问或只有单一来源：保留 `SINGLE_SOURCE` 或 `UNVERIFIED`，不得补写不存在的证据。
- 来源冲突：保留各方说法与来源谱系，标记 `DISPUTED`，不得为了简洁强行裁决。
- 平台趋势覆盖稀疏：明确列出可用和不可用平台，不推断全平台热度、用户情绪或虚构互动数据。
- 需要事实/文化依据的探索无候选达到优先门槛：允许“优先制作”为空，说明需要补充什么研究。深化模式不重开选题，以当前方向的依据与缺口决定交接范围；纯艺术表达探索不使用此分数门槛。

## 输出

默认写入：

```text
AIGC Creater/projects/<project-id>/research/
├── research-pack.md
└── source-index.md
```

使用 [research-pack-template.md](assets/research-pack-template.md) 和 [source-index-template.md](assets/source-index-template.md)。用户提供项目目录时，在该项目下创建或更新 `research/`；不得覆盖不属于本次研究的文件。
