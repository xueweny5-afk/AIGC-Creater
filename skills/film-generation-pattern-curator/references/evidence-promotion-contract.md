# Evidence Promotion Contract

## Evidence levels

- `OBSERVATION`：一次真实 Take 已经 QC，但没有受控对照。只能记录现象。
- `CONTROLLED_COMPARISON`：Baseline 与 Candidate 主要只改变一个独立变量，并使用相同验收维度。
- `REPEATED_PROJECT`：相同模式在同项目的多个相关 Unit/Take 中重复，且未出现相反证据。
- `CROSS_PROJECT`：在不同项目、相同模型边界和相近任务条件下重复成立。

`NON_EVALUABLE` 用于缺媒体、缺 QC、版本未知或证据无法对应的记录，不属于证据等级。

## Pattern status

- `LOCAL_OBSERVATION`：项目内经验，不供其他项目默认采用。
- `PROJECT_VALIDATED`：在当前项目定义的镜头范围内通过。
- `MODEL_VERSION_PATTERN`：可作为特定模型/版本/入口/模式的候选生产规则，仍需项目 Pilot。
- `CROSS_PROJECT_PATTERN`：跨项目重复成立，仍不能覆盖当前 Model Profile 与项目合同。
- `CONTRADICTED`：有可追溯相反证据，等待重测或缩小范围。
- `RETIRED`：模型、入口或工作流已失效；保留历史，不再推荐。

## Promotion minimum

| Target status | Minimum evidence | Additional requirements |
|---|---|---|
| LOCAL_OBSERVATION | OBSERVATION | 真实媒体 + QC + 确切版本 |
| PROJECT_VALIDATED | CONTROLLED_COMPARISON or repeated observations | 无未解释 Major 副作用；范围限于项目 |
| MODEL_VERSION_PATTERN | CONTROLLED_COMPARISON + relevant repetition | 模型/版本/入口/输入模式明确；至少覆盖目标风险 |
| CROSS_PROJECT_PATTERN | CROSS_PROJECT | 项目间条件与差异可比较；没有未解决相反证据 |

数量不是唯一标准。两个不可比较的案例不能因为“出现两次”升级；一个严格受控比较也不能自动推广到不同镜头类型。

## Staleness and contradiction

Model version、UI/API 入口、参考语义或控制能力变化时，把相关模式标 `REVIEW_REQUIRED` 或 `RETIRED`。新案例与既有模式冲突时，先缩小适用范围或标 `CONTRADICTED`，不挑选喜欢的结果覆盖旧证据。

## Use rule

Prompt Adapter 可以引用公共 Pattern ID 作为候选写法，但必须同时满足当前 Creative Master、Model Profile 和输入模式。Generation 仍需按风险执行 Pilot；Pattern Catalog 不是成功保证。
