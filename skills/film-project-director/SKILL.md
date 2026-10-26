---
name: film-project-director
description: Turn an early or incomplete film idea into a structured Film Project Brief while preserving the creator's intent. Use before research or story development, especially when the user has not yet chosen standalone short, episodic shorts, or a serial series. Do not use to write a screenplay or treatment, design shots, or generate image or video prompts.
---

# Film Project Director

把模糊的电影想法整理成可供下游继续开发的项目简报。默认使用中文表达，保留模板中的稳定英文字段名。先保护用户的创作意图，再补充明确标记的判断与假设。

开始工作前，读取 [project-brief-schema.md](references/project-brief-schema.md) 与 [decision-guide.md](references/decision-guide.md) 的「入口与本次交付范围」「G0 项目定义审阅」；项目形式、叙事模式或调研等级不明确时，再读取对应部分。

## 输入与边界

接受一句想法、零散设定、创作限制、目标载体，以及用户提供的参考作品或拆解。原作驱动项目可接收 `Source Intake / Source Coverage`。输入可以不完整，不要求用户先填写表格。

本 Skill 只定义“正在开发什么电影项目”。不得输出：

- 完整剧本、Treatment、详细梗概或逐场大纲；
- 场景调度、镜头表、景别、焦段、机位、运镜或分镜；
- 灯光方案、LUT、关键帧及图像或视频生成 Prompt；
- 为了显得完整而新增的重大人物、事件、反转、结局或历史事实。

## 核心规则

1. **Preserve intent before expanding imagination.** 用户明确表达的题材、主题、人物、时代、形式与限制优先于模型的创作偏好。
2. 保留用户原始想法，并将项目判断区分为 `USER_FACT` 与 `INFERRED`。
3. 使用 `LOCKED / OPEN / ASSUMED` 管理决策状态，不把假设伪装成用户决定。
4. 不把所有项目强行改写成三幕剧、英雄旅程、强冲突或人物成长故事；纪录、观察、散文和诗性项目可以由别的逻辑组织。
5. 参考作品只用于记录用户喜欢的品质和期望迁移的方法，不将其转写为复制剧情、角色、世界观或可识别画面的指令。
6. 反差必须来自用户意图或项目中已经存在的两个状态、价值或关系；不得为了“更有戏”擅自加入死亡、背叛、贫富逆转或其他重大悲剧。

## 工作流

1. **保护原始意图**：忠实记录用户的原始表达，提取已知内容、硬约束和仍然开放的部分，不先美化或改写故事。
   - 先识别新项目、已有项目续作或探索。已有项目沿用 Project ID 与最新批准版本；项目归属不明确时先确认，不因改名新建目录。维护公共流程或 Skill 的任务不启动电影项目、不询问成片生成分工。
   - 正式立项前明确本次交付范围与终止阶段；沿用用户已说明的范围。未说明时优先推荐文本内容交付，图片/视频生成与剪辑交给 RunningHub 或其他平台；探索方向时可先给建议，不把未知执行方式变成创意讨论的前置问卷。
   - 若用户只提供一部长篇原作且项目判断会依赖未读内容，先推荐 `Source Intake`，不得根据简介或局部章节假装掌握全文。
   - 已有 Source Intake 时，记录文件、版本、覆盖状态和改编不变量；`PARTIAL` 不能被简报写成完整原作结论。
2. **判断是否必须追问**：只有一个错误判断会改变项目性质或让简报失效时，才先问一个关键问题，例如用户想做纪录片还是真人虚构。
   - 在正式 Project Brief 前，若用户尚未说明成片是单支短片、系列短片还是连续剧情剧集，主动询问：`你希望先按哪种形式开发：单支短片、每集独立的系列短片，还是连续剧情剧集？` 这是项目架构问题，不用 `ASSUMED` 静默代替用户决定。
   - 若用户已明确“单支”“第几集”“系列”“单元剧”“连续剧”等，只在单集独立性仍会改变开发方法时追问，不重复确认已知信息。
   - 其余缺口使用 `OPEN` 或明确的 `ASSUMED` 继续。
   - 当用户明确说“测试一下”“给几个建议”“还在想”或要求探索方向时，不要立刻用二选一阻断。先给出 2–4 个真正不同的项目方向、各自重点与代价，并推荐一个可撤销的测试假设；用户确认或授权试跑后再生成正式简报。
   - 方向比较使用「项目表达 / 表达重点 / 观众体验 / 独特之处 / 制作代价」说明真正差异，不只换片名或风格词。用户方向已明确时直接沿用，不强制再给多方案，也不为比较方向自动生成图片。
3. **建立 Creative Core**：概括 Premise、Subject、Theme、Central Question、Emotional Core、Emotional Thesis、Core Image / Motif Seed、Core Contrast、Emotional Turn、Audience Experience 与 Why Now。Emotional Thesis 说明创作者希望影片通过什么具体关系或经验触达观众，不是宣传语；Core Image 只记录用户已提供或可明确标为假设的核心意象及其叙事含义，不为了“高级感”凭空创造象征。Central Question 应是项目持续探索的问题，不是口号或答案。Core Contrast 只在确实存在时提炼；没有依据则保持 `OPEN`，不强造对立或悲剧。Emotional Turn 描述观众体验的方向变化，不展开剧情节拍。
   - 在 Creative Core 用 `Project Expression` 的 1–2 句概括主体、基本情境与核心体验，检查脱离内部标签后能否读懂；只归纳现有决定，不新增剧情。记录 `Target Audience / Viewing Context`，区分观众是谁、在哪里/怎样观看、需要什么前置知识；平台名称不能代替受众判断，未知保持 OPEN。
4. **判断 Project Form**：先确认 Release Format 与 Series Architecture，再选择适合的 Film Form、Genre、Narrative Mode、Reality/Fiction Level 与 Point of View。单支短片不设计季架构；剧集必须说明单集独立、连续叙事或混合结构，但本阶段不展开分集故事。
5. **设置 Research Gate**：根据事实依赖而非题材表面，确定 `Low / Medium / High / Very High`，列出优先核实主题、当前已知事实和待核实事实。
6. **形成 Story Seed 与 Production Frame**：只记录足以下游起步的主体、关注或欲望、压力、可能变化、结局方向、单片或单集时长、计划数量、平台、画幅、规模和限制；未知内容保持开放。
   - 分别记录资产图片、分镜/关键帧图片和镜头视频的项目默认执行方式 `USER_GENERATE / AUTO_GENERATE / OPEN`，以及用户指定的手动交接位置。未知方式不阻断故事开发，到对应生成批次前再确定；已选方式不在每批重复询问，用户可明确覆盖某批。此处只锁执行路线，不编写 Prompt 或授予生成权限。
   - 用 `Resource Envelope` 记录已有的预算、可投入时间与期限；`Feasibility Hypotheses` 只列可能改变创作方向的关键 AIGC 难点、影响、待验证问题与最晚验证阶段，无关键难点写 NONE，未知写 OPEN。未经测试不得宣称可行、估算精确成本或保证生成成功；立项不执行样片，具体验证交给后续对应阶段。
7. **前置声音与语言意图**：记录主要语言/口音、对白/旁白/无对白策略、环境声方向、音乐原则、口型需求和交付变体。未知项写 `OPEN`，不提前锁定模型，也不阻断不依赖它们的前期阶段。
8. **处理 Creative References**：只有用户提供参考作品、片段或拆解时才加入该区域；尽量记录具体片段或时间码、用户喜欢什么、它为什么有效、希望迁移的机制、不能直接复制什么，以及后续要分析什么。不在本阶段反推镜头参数或 Prompt。
9. **执行 Method Fit Check（适用时）**：当用户点名 Method、已有 `film-method-*` 明确匹配，或用户要求复用已沉淀方法时，记录 Primary/Secondary Method、采用范围、预期观众效果、受控字段、项目保护字段、冲突和 Pilot。只有候选方法时标 `CANDIDATE`，不得当成正式规则；多个 Method 的同字段冲突必须保持 OPEN 或返回用户决定。
10. **审阅项目定义并选择下一阶段**：按 decision-guide 的 G0 审阅检查范围、创作核心、约束冲突和事实依赖，在 Decision Register 记录依据、阻断项与非阻断开放项。先说明正在讲什么、希望观众经历什么、哪些具体关系或经验支持它；不以填满标签代替项目成立。原作覆盖不足先进入 Source Intake；事实基础会影响故事成立则进入 Research；否则根据项目核心进入 Story Development 或 Character Development。G0 未就绪时先修定义，不把下游草稿当作正式交接。

## 输出

使用 [film-project-brief-template.md](assets/film-project-brief-template.md) 的章节顺序输出一份 Markdown `FILM PROJECT BRIEF`。

- 不得删除固定章节；未知项填写 `OPEN`，不要编造答案。
- 没有创作参考时，完全省略 `CREATIVE REFERENCES`。
- 没有采用 Method 时，完全省略 `METHOD ADOPTION`；采用时同步建立 `projects/<project-id>/direction/method-adoption.md`，Project Brief 只保留摘要与状态。
- 没有原作摄入材料时，完全省略 `SOURCE BASIS`。
- 简报之后最多补充一段简短说明，不继续写故事、镜头或 Prompt。
- 若前置关键问题尚未回答，只输出该问题，不提前生成一份建立在高风险猜测上的完整简报。
- 探索阶段的方向建议不是 Project Brief，不得把推荐项标成 `LOCKED`；用户授权试跑时以 `[ASSUMED · INFERRED]` 记录。
