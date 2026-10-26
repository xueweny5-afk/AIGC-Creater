---
name: film-video-method-curator
description: 从用户提供的视频、影视作品、图片序列或创作案例中拆解可迁移的叙事、视觉、镜头、动态、声音、提示词与验收方法，形成开放式 Method Pack，并在真实样片和 QC 证据充分后创建或升级 film-method-* 专项 Skill。用于参考学习、影视参考拆解、类型方法沉淀与跨项目复用；不复制原作、不执行未授权生成，也不把未验证观察包装成正式方法。
---

# Film Video Method Curator

把“这个视频做得不错”转成可追溯、可验证、能进入现有电影流程的专业方法。类型体系开放增长；不预设固定风格枚举，也不因题材相似就强行归类。

优先级固定为：`用户当前要求 > 当前项目批准合同 > 专项 Method Skill > 公共电影流程 > 通用模型经验`。

## Modes

- `STUDY`: 完整分析参考并建立 Study；不声称方法已验证。
- `CURATE`: 与现有 Method Pack 比较，创建、合并、拆分或修订候选方法。
- `ADOPT`: 为具体项目建立 Method Adoption Receipt 与阶段覆盖范围。
- `PROMOTE`: 核对真实 Pilot、QC 和适用边界后，创建或升级 `film-method-<slug>`。
- `REVIEW`: 用新项目、相反证据或模型变化复核、缩小或退役方法。

## Required inputs

按任务需要接收：

1. 用户提供的真实媒体路径、链接、图片序列或可核验案例；
2. 用户明确喜欢、想迁移或不想复制的部分；
3. 已存在的 Study / Method Pack / 专项 Skill（若为更新）；
4. PROMOTE 时的真实 Pilot Prompt、模型/入口/参数、Take、完整播放与 QC；
5. ADOPT 时的 Project Brief、项目锁定合同和目标范围。

无法读取完整媒体时可以输出 `PARTIAL STUDY`，但必须列出未覆盖范围。缺少真实样片或 QC 时不得 PROMOTE。

## Load resources

- 分析参考时读取 [method-study-guide.md](references/method-study-guide.md)，并使用 `assets/style-study-template.md`。
- 比较、创建或更新方法时读取 [method-promotion-contract.md](references/method-promotion-contract.md)，并使用 `assets/method-pack-template.md`。
- 为项目采用方法时读取 [workflow-integration-contract.md](references/workflow-integration-contract.md)，并使用 `assets/method-adoption-receipt-template.md`。
- 晋升专项 Skill 时同时读取 `skill-creator`，使用 `assets/specialist-skill-blueprint.md`；不得初始化没有真实内容的空专项 Skill。

## Outputs and placement

第一次产生内容时才创建目录：

```text
AIGC Creater/pipeline/knowledge/style-method-studies/<study-id>.md
AIGC Creater/pipeline/knowledge/style-methods/<method-id>/method-pack.md
AIGC Creater/skills/film-method-<slug>/                 # 仅 PROMOTE 后
```

具体项目的采用回执保存到：

```text
AIGC Creater/projects/<project-id>/direction/method-adoption.md
```

原始媒体保持在用户提供的位置；不得复制进 Skill 或公共知识目录。Study 可以记录本地路径、校验值和时间码，但专项 Skill 只保留去项目化方法和证据索引。

## Workflow

1. **Clarify the valued result.** 分开记录用户明确看重的部分与系统观察。用户未指出偏好时先做证据分析，不把推断写成 `USER_VALUED`。
2. **Verify and inspect the source.** 登记来源、版本、权限状态、文件信息、覆盖范围；完整观看，结合转录、顺序抽帧、镜头边界、声音和可见制作界面建立证据。
3. **Separate content from method.** 把可观察事实、推断机制、作品独有表达、禁止复制项和待验证假设分开；不复制人物、台词、品牌、独特构图或完整 Prompt。
4. **Extract only relevant layers.** 按实际证据分析叙事、视觉、资产、镜头、动态、声音、Prompt、后期和 QC；不为填满模板虚构不存在的层级。视觉参考先以 `TEXTURE / COLOR / PHOTO / MOOD` 四轴建立完整判断，再按任务增加剪辑、表演、声音或文字等专项轴；四轴是观察入口，不是封闭风格标签。
   - 影视作品可以作为 Soft Reference。按具体场景、时间码或可核验片段记录观察，不从片名、海报或印象推断整部作品风格。
   - 多参考必须建立 Reference Map：每个作品只承担明确轴或机制，并记录要迁移、要重建和绝不能复制的部分；不得用“整体参考某片”代替设计。
   - 多段落可以有不同质感、色调和摄影策略，但必须先定义共同视觉不变量、每段叙事功能、变化轴与转场关系，避免随机换风格。
5. **Compare before classifying.** 与现有 Method Pack 按核心机制和受控字段比较：相同则补充，部分相同则建立模块或组合关系，核心不同则新建候选；冲突证据并存，不挑选喜欢的结果覆盖。
6. **Create a bounded candidate.** 写明适用/不适用条件、创作不变量、可变字段、阶段覆盖、风险、Pilot 假设和专项验收。状态最高为 `PILOT_READY`。
7. **Adopt explicitly.** 在项目中用 Method Adoption Receipt 锁定 Method 版本、范围、主次关系、受控字段、项目保护字段、冲突裁决和 Pilot；不直接把整个方法库塞入各阶段。
8. **Validate through the existing pipeline.** 让各责任 Skill 应用覆盖；Generation 执行最小 Pilot，Continuity QC 同时检查通用合同和 Method-specific QC。
9. **Promote conservatively.** 只有 Study 完整、用户意图明确、原创转换完成、代表性 Pilot 与 QC 通过、适用边界清楚时才创建或升级专项 Skill。状态为 `VALIDATED_FOR_SCOPE`，不是全类型保证。
10. **Feed evidence back.** 跨阶段创作方法回本 Skill；具体模型、参数、参考职责和 Prompt 变量证据交 `film-generation-pattern-curator`。新证据可以扩展、拆分、合并、缩小、复核或退役方法。

## Status

- `STUDY_ONLY`
- `CANDIDATE`
- `PILOT_READY`
- `VALIDATED_FOR_SCOPE`
- `REVIEW_REQUIRED`
- `RETIRED`

## Boundaries

- 不维护封闭类型表；Method ID 描述可复用机制，不把题材标签当方法。
- 不把参考作品当历史、现实、科学或模型能力证据。
- 不从一次漂亮结果或作者讲解推断稳定生成规律。
- 不因用户允许参考影视，就复制演员身份、服装造型、标志性构图、场面调度、对白、字幕设计或完整视听组合。
- 只有片名而没有可检查片段时，只登记 `USER-SUGGESTED SOFT REFERENCE`；不得凭印象填写四轴分析。
- 不创建未经过真实 Pilot 与 QC 的正式专项 Skill。
- 不让 Method 覆盖用户决定、项目批准合同、研究事实、资产身份或当前 Model Profile。
- 不复制原视频、完整私有 Prompt、未发布项目内容或无授权素材到专项 Skill。
- 不执行外部上传、付费生成、发布或分享，除非用户另行授权。

## Completion gate

- Study 的实际观察、推断、用户偏好和不可复制内容已分开；
- Method 的适用条件、控制字段、阶段覆盖、风险和 QC 可执行；
- 新建、合并、拆分或保持独立的理由明确；
- 未验证方法没有被包装成正式 Skill；
- PROMOTE 有真实 Take、完整 QC、证据索引和范围限制；
- ADOPT 有项目保护字段、冲突裁决和最小 Pilot；
- 输出进入正确公共知识或项目目录，没有复制原始媒体。
