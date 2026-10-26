# Film Project Brief Schema

本文件定义 `film-project-director` 的稳定输出接口。输出使用 Markdown，面向用户阅读，也供后续 Skill 继续开发。

## 标记规则

### 决策状态

- `LOCKED`：用户明确要求必须保留的决定。下游不得擅自更改。
- `OPEN`：尚未决定，或用户明确希望继续探索。不得为填满模板而强行选择。
- `ASSUMED`：为使项目能够继续，AI 暂时采用的可撤销选择。必须能被用户修改。

### 信息来源

- `USER_FACT`：用户明确说出或确认的信息，包括明确表达的偏好。
- `INFERRED`：AI 根据上下文作出的解释、归纳或推断，不代表用户已经确认。

需要决策的已填字段使用 `[状态 · 来源]`，例如：

```text
- **Narrative Mode｜叙事模式：** [ASSUMED · INFERRED] Observational
```

未知字段只标记 `[OPEN] 待确定`。用户明确但仍可探索的表达可标记 `[OPEN · USER_FACT]`。`ORIGINAL IDEA` 是原始记录，只标记 `USER_FACT`，不使用决策状态。

不得把外部常识、网络资料或模型记忆标为 `USER_FACT`。尚未核实的历史、现实或专业信息进入 `Facts To Verify`。

## 固定结构

### 1. Project Identity

- `Project ID`：已有项目沿用其编号；项目归属有歧义时先确认。只有确定是新项目且没有编号时，才使用 `[ASSUMED · INFERRED] FPD-YYYYMMDD-简短代号`；标题变化不产生新编号。
- `Working Title`：暂名可以是假设，但不得暗示用户已确认。

### 2. Original Idea

尽量保留用户原话；只做必要的错别字整理时注明。不得用 AI 扩写后的版本替代原始想法。

### 3. Source Basis（可选）

仅原作驱动且存在 Source Intake 时出现：

- `Source Intake Version / Status`
- `Source Scope & Coverage`
- `Source Invariants`
- `Open Adaptation Decisions`
- `Source Limits / Do Not Assert`

Source Basis 描述原作依据，不等于外部事实核验。覆盖为 `PARTIAL` 时必须保留未读范围，不能用简介、评论或记忆补齐。

### 4. Creative Core

- `Project Expression`：用 1–2 句概括主体、基本情境与核心体验，能够脱离模板独立理解。剧情作品可体现目标或压力，诗性/观察作品可体现关系、时间或体验；不强求同一结构，不用宣传口号代替，也不扩写尚未批准的剧情。
- `Premise`：项目最基本的情境，不展开完整情节。
- `Subject`：影片真正关注的人、群体、地点、事件或现象。
- `Theme`：希望探索的主题领域，不写成道德结论。
- `Central Question`：影片持续追问、但不预设答案的问题。
- `Emotional Core`：最主要的情感张力。
- `Emotional Thesis`：影片希望通过哪种具体人物关系、生活经验或不可回避的感受触达观众；不写成营销口号、道德答案或抽象“治愈/感动”。用户尚未表达时保持 `OPEN`。
- `Core Image / Motif Seed`：来自用户经验、故事事实或明确假设的核心意象，以及它可能承载的叙事含义。它只是一颗后续发展的种子，不在本阶段规定镜头、色彩或反复次数，也不凭空发明象征。
- `Core Contrast`：推动项目体验的两个状态、价值、关系或时间结果之间的反差；没有明确反差时保持 `OPEN` 或写 `Not Contrast-led`，不得强造悲剧。
- `Emotional Turn`：观众体验的方向变化，例如“亲近 → 不安 → 重新理解”；这是上层情绪轨迹，不是剧情节拍或场次安排。
- `Audience Experience`：希望观众经历的情绪或认知变化。
- `Target Audience`：主要观众及其与题材有关的经验或前置知识；不凭空推断人口属性，未知保持 OPEN。
- `Viewing Context`：观看场景与注意条件，如手机信息流、完整短片播放或展映，以及理解题材所需的背景。它与 Target Platform 分开记录，不自动推出“三秒钩子”等固定叙事规则。
- `Why Now`：为什么此刻值得开发；没有依据时保持开放。

### 5. Project Form

- `Release Format`：成片发布结构。使用 `Standalone Short / Short-form Series / Episodic Anthology / Serial Narrative Series / Feature or Long-form / OPEN`。
- `Series Architecture`：剧集单元之间的关系。使用 `Not Applicable / Standalone Episodes / Shared World Episodes / Continuous Serial / Hybrid / OPEN`。
- `Film Form`：影片的基本创作形式。
- `Genre`：类型或类型组合；不适用时写 `Not Genre-led`。
- `Narrative Mode`：组织材料和推进观看体验的主要方式。
- `Reality / Fiction Level`：事实、虚构及两者的关系。
- `Point of View`：观众通过谁或什么位置接近内容。

`Release Format` 与 `Film Form` 不得混用：前者描述单支或剧集结构，后者描述剧情、纪录、散文或实验等创作形式。若用户只说“AIGC 电影/短片”而未说明单支还是系列，正式简报前主动询问；不得因为某题材适合扩展就自行锁定剧集。

### 6. Story Seed

- `Protagonist / Subject`：剧情项目可写主角，纪录或散文项目可写观察主体。
- `Desire or Concern`：主体追求、关心或无法回避的事。
- `Pressure / Conflict`：当前可见的压力、矛盾或变化，不强求对抗性冲突。
- `Possible Change`：只写可能方向；没有人物弧时可写环境、关系或认知变化。
- `Possible Ending Direction`：方向而非具体结局；用户未提供时保持开放。

### 7. World

- `Era`
- `Place`
- `Social Context`

每项都要区分创作设定和待核实事实。

### 8. Research Gate

- `Research Dependency`：仅使用 `Low / Medium / High / Very High`。
- `Required Topics`：会影响项目正确性或可信度的优先调研主题。
- `Known Facts`：仅列用户提供且可视为项目输入的事实，不宣称已经外部核验。
- `Facts To Verify`：需要研究确认的历史、现实、专业、文化或科学信息。

### 9. Production Frame

- `Delivery Scope`：本次交付 `CONTENT_ONLY / PREPRODUCTION / FULL_PRODUCTION / OPEN`；必须同时写明所需产物和终止阶段，不由模式名称推定是否包含图片生成。CONTENT_ONLY 不要求回传真实媒体才交付文本。
- `Target Duration`：单支短片或每集的目标时长；长片则为全片时长。
- `Planned Count / Season Scope`：单支项目写 `1`；剧集写计划集数、首季范围或 `OPEN`。
- `Target Platform`
- `Aspect Ratio`
- `Production Scale`
- `Key Constraints`
- `Resource Envelope`：已有预算或费用上限、可投入时间与期限，保留其来源和状态。未给出时保持 OPEN，不要求先填预算才允许研究或故事开发，不编造精确成本。
- `Feasibility Hypotheses`：只记录影响方向的关键 AIGC 难点，使用「难点 / 对创意的影响 / 待验证问题 / 最晚验证阶段」。无关键难点写 NONE，信息不足写 OPEN；候选难点是待验证假设，不是模型能力结论。立项不执行验证，也不让风险条目自动改变已锁定表达；具体模型与验证方案留给后续对应阶段。
- `Asset Image Execution / Storyboard Image Execution / Shot Video Execution`：分别记录 `USER_GENERATE / AUTO_GENERATE / OPEN`；项目默认方式不替代实际生成授权，单批可按用户明确要求覆盖并留痕。
- `Manual Handoff Surface`：用户指定无限画布时记录；未指定保持 `OPEN`。手动交接按 Asset/Frame/Shot ID 输出可独立复制的卡片，提示词与操作、验收分开。

未给出的制作参数保持开放，不因“AIGC 电影”自动选择画幅、时长或模型。

### 10. Audio / Language Intent

- `Primary Language / Accent`
- `Dialogue / Narration / No-dialogue Policy`
- `Environment Sound Intent`
- `Music Policy`
- `Lip-sync Requirement`: `REQUIRED / NOT REQUIRED / OPEN`
- `Delivery Audio Variants`

本阶段只固定稳定的声音与语言意图，不选择语音、音乐或视频模型，不写逐场声音设计。用户未提供的字段统一写 `OPEN`；这些开放项不阻断 Research、Story 或 Visual Development，只有进入依赖它们的表演、Prompt、生成与交付节点时才成为条件。

### 11. Creative References（可选）

仅在用户提供作品、片段、图片或拆解时出现：

- `Reference`
- `Reference Moment / Timecode`
- `What the User Values`
- `Transferable Qualities`
- `Why It Works`
- `Transferable Mechanism`
- `Do Not Copy`
- `Questions for Later Analysis`

`Reference Moment / Timecode` 仅记录用户提供或已经核验的位置；不知道时保持 `OPEN`，不得伪造精确时间码。`Why It Works` 说明参考片段中可观察到的因果关系，`Transferable Mechanism` 则把它改写为不依赖原人物和原画面的创作方法。不得在这里反推详细摄影参数或生成 Prompt。

### 12. Method Adoption（可选）

仅当用户明确采用一个或多个已存在 Method，或授权使用候选 Method 做 Pilot 时出现：

- `Primary Method ID / Version`
- `Secondary Method IDs / Versions`
- `Adoption Scope`
- `Expected Audience Effect`
- `Controlled Fields`
- `Protected Project Fields`
- `Method Conflicts / Resolution`
- `Pilot Requirement`
- `Validation Status`: `CANDIDATE / PILOT / VALIDATED / RETURN`
- `Affected Stages`

完整字段写入 `direction/method-adoption.md`。Method 不得覆盖用户要求、项目 LOCKED 决定和研究事实；未经真实样片验证的候选只允许进入 Pilot。

### 13. Decision Register

- `LOCKED`：汇总所有已锁定决定。
- `OPEN`：汇总最重要的未决问题，避免重复整份模板。
- `ASSUMED`：汇总所有临时假设，并说明它们可被替换。
- `G0 Review`：`READY / OPEN / RETURN`，附审阅依据、阻断项、可留待后续的开放项及其最晚解决阶段。READY 表示项目定义足以进入所推荐阶段，不代表所有假设被用户批准，也不代表研究、视觉或生产已通过。

### 14. Next Stage

只给一个 `Primary Recommendation`，可选值为 `Source Intake`、`Research`、`Story Development` 或 `Character Development`，并用一句话说明为什么它现在优先。

仅 G0 READY 时作为正式交接。G0 为 OPEN / RETURN 时保留候选下一阶段并说明缺口，不宣称已进入；同时注明本次终止阶段，避免把「推荐下一阶段」误当成继续制作的授权。

## 完整性要求

- 固定章节必须存在，`SOURCE BASIS`、`CREATIVE REFERENCES` 与 `METHOD ADOPTION` 除外；三者只在对应输入真实存在时出现。
- 每个决定都能追溯到用户输入或显式推断。
- `LOCKED` 不得包含 AI 自行添加的选择。
- `ASSUMED` 必须同时使用 `INFERRED` 来源。
- `OPEN` 不得被下一段文字偷偷当作已决定事项。
- Release Format 未知且会影响项目结构时，必须先询问，不能以题材或制作方便代替用户选择。
