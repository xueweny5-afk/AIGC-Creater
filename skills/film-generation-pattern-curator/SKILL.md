---
name: film-generation-pattern-curator
description: 将 AIGC 电影生成中的 Prompt、模型版本、参考输入、参数、真实 Take、QC 结果和单变量修改整理为可追溯的成功/失败案例，并把有足够证据的结论提升为项目级或公共生成模式。用于技术样片、重试、模型路由和跨项目经验沉淀；不执行生成、不替代 QC，也不把单次漂亮结果或平台宣传升级成通用规律。
---

# Film Generation Pattern Curator

把生成经验从“感觉这句词有用”转成带证据、适用边界和失效条件的生产知识。它是 Prompt → Generation → QC 之间的辅助 Skill，不新增制作阶段。

## Required inputs

1. Prompt Package / Prompt Unit 和完整版本或哈希
2. Model / version / entry / input mode / parameters
3. Reference input paths、版本、角色与可用校验值
4. Take / Attempt 日志和真实输出路径
5. Continuity QC 报告、Issue ID、时间码与实际观察
6. 与前一次尝试的明确差异；没有对照时只能形成观察，不能声称因果

缺少真实媒体或 QC 时标 `NON_EVALUABLE`，不提升模式。

## Load resources

- 建立案例前读取 `references/case-learning-guide.md`。
- 判断证据等级与是否提升时读取 `references/evidence-promotion-contract.md`。
- 使用 `assets/generation-case-template.md`、`assets/case-ledger-template.md` 与 `assets/pattern-catalog-template.md`。

## Outputs and placement

项目原始证据必须留在项目目录：

```text
AIGC Creater/projects/<project-id>/generation/learning/
├── case-ledger.md
└── cases/<case-id>.md
```

出现首个可提升的公共模式时，创建：

```text
AIGC Creater/pipeline/knowledge/generation-pattern-catalog.md
```

公共目录只保存去项目化的结论、证据索引、模型边界和失效条件；私人媒体、人物肖像、未发布剧情、完整私有 Prompt 和绝对项目路径不复制过去。

## Workflow

1. **Select one hypothesis.** 每个 Case 只回答一个主要问题，例如“固定镜头末尾仍漂移”或“身份图与服装图职责冲突”；多问题拆开记录。
2. **Lock the baseline.** 记录 Prompt/输入/参数/模型/Take/QC 的确切版本；无法复现的结果只能是低证据观察。
3. **Describe visible evidence.** 用时间码、帧区间或图片区域描述成功和失败，不写“更高级、更自然、AI感少了”。
4. **Identify the changed variable.** 写明与 Baseline 相比只改变了什么；多个字段同时改变时标 `CONFOUNDED`，不推断哪个字段起作用。
5. **Compare intended dimensions.** 分别判断身份、动作、摄影机、空间、材质、Atmosphere、声音、连续性与新副作用；不能因目标维度改善而忽略新增 Major 问题。
6. **Assign evidence level.** 使用 `OBSERVATION / CONTROLLED_COMPARISON / REPEATED_PROJECT / CROSS_PROJECT`；证据等级不等于模式适用范围。
7. **Write a bounded conclusion.** 结论包含：对什么模型版本、入口、输入模式、镜头类型和风险有效；不适用于什么；需要哪些前提。
8. **Set pattern status.** 使用 `LOCAL_OBSERVATION / PROJECT_VALIDATED / MODEL_VERSION_PATTERN / CROSS_PROJECT_PATTERN / RETIRED / CONTRADICTED`。单次成功最多是 Local Observation；受控比较或重复证据才考虑提升。
9. **Promote or hold.** 满足证据合同后，把去项目化模式写入公共 Catalog；否则保留在项目 Case Ledger。模型升级、入口变化或新证据矛盾时标 Stale/Retired，不删除历史。
10. **Route learning.** Prompt 写法问题回 Prompt Library；模型能力边界回 Model Profile/Pilot；上游合同问题回对应创作阶段；执行故障不提升为创作模式。
   - 跨阶段叙事、视觉、镜头、动态、声音和类型专项 QC 属于 `film-video-method-curator`；本 Skill 只处理能追到具体模型、Prompt、参数、参考输入与 Take/QC 对照的生成模式。

## Case requirements

- Case ID / Project / Date / Owner
- Hypothesis / Intended Dimension
- Baseline Prompt Package / Model Profile / Inputs / Parameters
- Candidate Change / Single Variable / Confounds
- Baseline and Candidate Take paths
- QC evidence / issue IDs / timecodes
- Expected vs actual result / new side effects
- Evidence level / confidence / applicability
- Conclusion / do not generalize / next smallest test
- Pattern status / promotion or retirement decision

## Non-negotiable boundaries

- 不把平台成功、文件存在、静态截图好看或作者经验当作 QC 证据。
- 不从一次随机 seed 成功推断某个词普遍有效。
- 不把同时修改 Prompt、参考图、参数和模型的结果称为单变量验证。
- 不把模型版本特性写成永久事实；版本或入口未知时不提升。
- 不用成功案例覆盖失败案例；失败边界同样是生产知识。
- 不把公共模式反向覆盖项目 Creative Master、Asset、Shot 或 Motion 合同。
- 不把私人项目内容、媒体或完整 Prompt 自动复制到公共目录。

## Completion gate

- Case 能追到真实 Prompt、输入、Take 和 QC；
- 可见证据与推断分开；
- Changed Variable 和 Confounds 明确；
- 结论带模型版本、输入模式、镜头类型和适用边界；
- Promotion 符合证据等级，未验证内容仍留项目内；
- 公共模式已去项目化且保留可追溯证据索引；
- 下一步是采用、继续最小测试、退役或返回正确责任层。
