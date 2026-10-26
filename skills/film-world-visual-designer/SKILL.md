---
name: film-world-visual-designer
description: 从已批准且覆盖完整的 Screenplay、Project Brief、Research Pack 与 Character System 建立电影或剧集的 World & Visual Bible 和资产需求清单。用于定义世界、时代、空间、人物身份、服装、道具、色彩、光线、材质、视觉母题与连续性规则；不用于生成图片、人物六视图、镜头、分镜、关键帧或模型提示词。
---

# Film World & Visual Designer

把剧本中的世界与视觉含义整理成可审阅、可锁定、可供资产和导演阶段共同使用的视觉主合同。先定义世界为何这样呈现，再进入具体图像生产。

## Required inputs

优先读取：

1. `screenplay.fountain` 与 `screenplay-register.md`，Coverage 必须为 `COMPLETE`
2. `Character System`
3. `Research Pack` 与 `Source Index`（如适用）
4. `Film Project Brief`
5. `Film Treatment` 与用户批准的视觉参考

若 Screenplay 为 RETURN、PARTIAL，或上游事实/人物/结局仍阻断，不创建 Visual Bible，返回最早失效阶段。

## Load resources

- 开始设计前读取 `references/visual-development-guide.md`。
- 创建或验收交付物时读取 `references/visual-bible-contract.md`。
- 使用 `assets/world-visual-bible-template.md` 和 `assets/asset-requirements-template.md`；存在外部视觉参考时另使用 `assets/visual-reference-analysis-template.md`。
- 核心场景存在显著、重复、会变化或连续性敏感的空气介质时，调用 `film-atmosphere-designer` 建立 `atmosphere-state-register.md`；简单状态直接写入 Scene Look & Light State，不强制增加文档。

## Outputs

默认保存：

```text
AIGC Creater/projects/<project-id>/visual-development/
├── world-visual-bible.md
├── asset-requirements.md
└── reference-analysis.md              # 仅存在外部视觉参考时
```

Visual Bible 是设计合同，不是漂亮词汇集合。Asset Requirements 只说明需要什么参考资产、视图和状态，不生成图片或 Prompt。

## Workflow

1. **Verify upstream.** 确认剧本范围完整、Release Format 与 Scope 一致，记录 Source Versions & Ready Scope、本次交付与终止阶段，继承 LOCKED / OPEN / ASSUMED、研究边界、组织原则、艺术方法和授权重构。新版剧本应有 Screenplay Review PASS 且无影响交接的时长/连续性问题；旧版已批准成果核对实质范围，不因缺新字段重做已通过工作。
2. **Define the visual proposition and direction.** 从情感命题、剧本行动/体验、人物关系与空间功能提炼 Visual Proposition，说明画面让观众辨认和感受什么，不从风格标签起步。方向未定且影响整体美学时按 guide 用文字比较表达重点、人物/环境关系、媒介/现实规则和连续性代价，再记录 Direction Decision / Basis；已有方向直接沿用，不强制重选或自动生图。
3. **Build world logic.** 定义时代与社会层、地理与气候、空间类型、技术或幻想规则如何留下可见后果。
4. **Define identity systems.** 分别建立人物、群体、服装、场景和道具的身份锚点、可变状态与禁止漂移项；此阶段不画图。
5. **Define visual relations, look arc and presentation rules.** 把风格转为可观察的人物/环境分离、空间密度、色彩/明暗关系、材料与使用痕迹等 Visual Relation Rules，说明稳定项、允许变化和适用范围，不定义单镜构图或机位。建立 Narrative Look Arc 与 Scene Look & Light State ID，变化可来自故事、关系、时间或批准的感知转换，不机械暖色表温暖、冷色表悲伤。Presentation Mode 使用 PHYSICAL / STYLIZED / MIXED：物理层光源、材料和 Atmospheric Medium State 仍有来源/分布/驱动；非物理光色、绘画纹理或象征性漂浮等另记 Artistic Presentation Rules 的作用、状态范围、进入/退出触发和连续性，不伪装成物理空气介质，也不以缺物理来源否定已批准艺术规则。无真实介质时物理空气仍为 NONE。
6. **Separate evidence.** 历史、现实和文化题材区分 `DOCUMENTED / RESEARCH-INFERRED / CREATIVE / UNKNOWN`。无依据的服饰、建筑和器物不得被标为历史准确。
7. **Translate references.** 对每份外部参考登记来源、路径/版本、权利状态与实际可见内容，再分类为 `HARD_ANCHOR / SOFT_REFERENCE / EXCLUSION`。`HARD_ANCHOR` 只能引用已批准的本项目合同；风格参考只可成为 Soft Reference 或产生 Exclusion，不能自行建立人物身份、服装、空间或史实。记录允许影响、禁止覆盖与原创转换。
8. **Prioritize assets and verification.** 按故事重要性与连续性风险列最小必要人物、场景、服装、道具与状态资产，保留职责分类和审批顺序；用 Visual Rule Validation 将核心规则关联确切规则/状态 ID、Asset ID、必要视图/状态、可观察验收点和验证责任阶段。单资产证明不了的关系画面留到 Storyboard 验证，不在此处生成关键帧；文字验收点保持 PLANNED，不声称像素已通过。
9. **Review and route.** 核对视觉命题、关系规则、变化触发、参考转换与验收映射能否共同指导资产设计，在现有 Decision Register 记录 Visual Review 的范围、依据、来源、问题与结论。仅文本规则完整且审阅 PASS、无影响交接的方向冲突时标 READY FOR ASSET DESIGN；未解决的高成本方向走现有 VISUAL DECISION GATE，不让生成图片代替决定。文本通过不代表资产、关键帧或 G3 已通过，不新增审批门。

## Method overlay（采用时）

当 Visual Development 被 Adoption Receipt 列入影响阶段，读取对应 Method Pack 的视觉转换、保护字段、允许变化、参考语义和典型失败；只写入项目批准范围。Method 是 Soft Overlay，不能覆盖人物身份、历史证据、Scene State 或用户锁定视觉决定。

## Non-negotiable boundaries

- 不生成、编辑或声称已经生成任何图片。
- 不写图像或视频 Prompt，不选择 Seedance、Kling、Veo 等视频模型。
- 不输出人物六视图、头部角度、表情状态、场景图、道具图、Storyboard、Keyframe 或 Shot List。
- 不锁定剧本未要求且会改变人物身份、文化含义或历史准确性的外貌特征。
- 不用通用“电影感”配方默认加入青橙、雾、颗粒、浅景深、轮廓光或宽银幕。
- 不把镜头级焦段、机位和运镜写入项目视觉圣经。
- 不用 AIGC 方便生成的内容替换更重要但困难的故事要求。

## Mode calibration

- **历史 / 现实：** 视觉结论必须追溯来源；证据不足的服装、建筑、文字和器物保持 UNKNOWN 或返回 Research。
- **人文 / 情感：** 从劳动、使用痕迹、空间关系和时间变化建立视觉系统，避免自动怀旧滤镜和贫困美学。
- **科幻：** 从功能、能源、维护、人体工学和环境后果推导设计；不靠无功能发光线条表示未来。
- **神话 / 修仙：** 将制度、修炼代价、资源流向和宗门功能外化为材料、空间与状态差异；不复制现有 IP 的门派和法宝语言。
- **艺术 / 梦境 / 非写实：** 在已批准表达范围内定义媒介、抽象与感知规则；人物身份、事实承诺和剧本意义仍保持边界。非物理效果单列 CREATIVE 呈现规则，物理空气状态按实际需要记录，不能混写成有史实或物理证据。

## Completion gate

推荐 Asset Design 前必须满足：

- 视觉规则能回指故事、人物或世界功能；
- Visual Proposition、Direction Decision / Basis 与 Presentation Mode 明确，风格关系可观察，已知方向不被重复改选；
- 每类核心资产都有身份锚点、可变状态和连续性风险；
- 研究证据与原创设计清楚分层；
- 参考作品只留下抽象可迁移品质；
- 适用的参考已完成硬锚点、软参考和排除项转换；
- 核心场景具有可继承的 Scene Look & Light State ID；
- 适用的时期/章节具有 Narrative Look Arc，且变化能回指叙事；空气介质有物理来源或明确为 NONE；
- 复杂空气状态如适用已有 Atmosphere State ID，并能被资产、场景、Motion、Prompt 与 QC 引用；
- OPEN 决定不会被误当成 locked design；
- 已给出最小必要资产与审批优先级；
- 核心关系/艺术规则有稳定项、适用范围和变化触发，Visual Rule Validation 关联资产、验收点与责任阶段；实际画面未出现时仍为 PLANNED；
- Visual Review 为 PASS 且无影响交接的开放方向冲突，艺术呈现与物理空气层分开，不以文本就绪宣称 G3 或画面效果已验证；
- 没有输出图片、镜头或 Prompt。
