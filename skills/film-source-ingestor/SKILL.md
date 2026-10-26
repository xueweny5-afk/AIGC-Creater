---
name: film-source-ingestor
description: 将用户提供的小说、故事、剧本、纪实材料或长文原作转换为可追溯的 Source Intake 与覆盖记录，提取人物、事件、地点、物件、规则、时间线和改编边界。用于原作驱动项目前置摄入；不用于外部事实核验、改写故事、写项目简报、剧本、镜头或生成提示词。
---

# Film Source Ingestor

把原作读清楚、读完整，并形成可供 Project Direction、Research 和 Story Development 使用的来源底座。原作内容、叙述者说法、角色认知和分析解释必须分开；“提取”不等于“改编决定”。

## Required inputs

- 用户提供或明确指定的原作文件、文本或附件；
- 已知的作品名、作者/来源、版本/译本与文件范围；
- 用户希望改编的范围或当前探索目标（如有）；
- 可读取、转换和保存派生产物的授权范围。

短想法或几百字故事可以直接进入 `film-project-director`。只有原作较长、版本复杂、需要覆盖证明或下游会依赖具体细节时，才使用本 Skill。

## Load resources

- 开始摄入前读取 `references/source-intake-contract.md`。
- 输出使用 `assets/source-intake-template.md` 与 `assets/source-coverage-template.md`。

## Outputs

```text
AIGC Creater/projects/<project-id>/source/
├── source-intake.md
└── source-coverage.md
```

若 Stage 00 运行时尚无 Project ID，使用可撤销的 `[ASSUMED] FPD-YYYYMMDD-简短代号` 建立目录，并在 Project Direction 中原样继承或显式改名；不得为同一来源悄悄建立两个项目目录。

## Workflow

1. **Register the source.** 记录实际文件、作品/作者、版本、译本、页数或章节范围、文件哈希（可用时）和允许用途。多个版本不得混成一个来源。
2. **Prepare a readable copy.** 必要时使用适合文档/PDF的只读提取能力建立工作副本，不覆盖原文件；OCR、页缺失、乱码和格式损失必须登记。
3. **Plan coverage.** 按章节、场次、页码或稳定段落 ID 建立顺序覆盖表。不得因为某段看似“不重要”而静默跳读；无法读取的范围标 `UNREAD / BLOCKED`。
4. **Read and classify.** 区分 `SOURCE_EVENT`、`NARRATOR_CLAIM`、`CHARACTER_BELIEF`、`DOCUMENTED_DIALOGUE`、`ANALYST_INTERPRETATION` 和 `UNKNOWN`。人物说法不能自动升级为作品世界事实。
5. **Extract source elements.** 登记人物与别名、关系、事件、时间线、地点、物件、世界规则、母题、关键状态变化和必要的原文定位。只保留最小必要短引或定位信息，不复制大段文本。
6. **Track contradictions and uncertainty.** 保留叙述冲突、时间矛盾、版本差异、未解释规则和视角偏差，不为整洁而裁决。
7. **Define adaptation boundaries.** 区分用户要求保留的 `SOURCE INVARIANTS`、可压缩/合并/重排的 `ADAPTATION OPTIONS`、尚待用户决定的 `OPEN` 和不能宣称的内容。这里只提出候选，不替用户完成改编。
8. **Audit completeness.** 对照覆盖表确认已读、未读、受阻范围和抽取回链。覆盖不完整时状态只能是 `PARTIAL`，不得声称通读。
9. **Route.** 完整摄入后优先进入 Project Direction；若原作依赖历史、现实、科学或文化事实，再由 Project Brief 设置 Research Gate。

## Non-negotiable boundaries

- 不把原作中的历史、科学或现实说法当成外部已核实事实。
- 不从未读章节、简介、评论或模型记忆补写原作内容。
- 不自动删去支线、合并人物、改结局或决定忠实度。
- 不生成 Treatment、剧本、镜头、分镜、图片/视频 Prompt 或媒体。
- 不自动上传私人原稿到外部服务，不覆盖或整理用户原文件。

## Completion gate

- 每个结论能回到文件、版本和章节/页码/段落范围；
- 覆盖表明确 `READ / UNREAD / BLOCKED / NOT IN SCOPE`；
- 原作事件、人物认知与分析解释分层；
- 人物、地点、物件、规则与时间线使用稳定 ID；
- 改编不变量、可选项和未决项清楚，但没有替用户改写故事；
- 状态诚实标为 `COMPLETE / PARTIAL / RETURN`。
