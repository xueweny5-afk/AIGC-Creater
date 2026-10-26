# Generation Case Learning Guide

## Learn from comparisons, not anecdotes

最有价值的 Case 通常来自技术样片、失败重试或模型路由测试。优先比较：相同创作合同、相同参考输入、相同模型版本，只改变一个 Prompt 句、参考职责、参数或 Clip 拆分方式。

无法做到严格单变量时，明确列出 Confounds，并把结论限制为“这一组合得到该结果”，不要拆解虚假的因果。

## Evidence sentence

使用：

```text
在 [model/version/entry/input mode]、[shot type] 和 [fixed inputs] 条件下，
将 [single change] 从 [baseline] 改为 [candidate] 后，
[observable dimension] 在 [timecode/frame/region] 从 [before] 变为 [after]；
[other dimensions] 保持/未保持，新增副作用为 [evidence]。
```

避免：“加了电影感词后明显更真实”“Seedance 更会演戏”“这个负向词绝对有效”。

## Useful case families

- Reference role collision / identity drift
- Character turn / age / costume continuity
- Hand-prop contact and entity conservation
- Observable performance / pause / gaze / lip-sync
- Static camera drift / camera command conflict
- Start/Mid/End frame replay or transition failure
- Location topology / reflection / text
- Material response / plastic skin / uniform wear
- Atmospheric medium source / density / motion continuity
- Duration, clip split and required reaction hold
- Sound or unsupported capability degradation
- Platform, upload, parameter and execution failure

## Success and failure must share dimensions

Baseline 和 Candidate 使用相同验收维度。若只展示 Candidate 的优点而不检查身份、动作、空间和副作用，这不是学习案例。失败案例至少说明：可见症状、最早责任层、已排除的原因、下一次只改变什么。

## Public abstraction

公共模式只保留必要抽象，例如：

- 模型家族/版本/入口和输入模式；
- 镜头类型与风险；
- Baseline 与 Change 的语义差异；
- 观察到的效果、副作用和证据等级；
- 适用前提、禁用范围和失效日期。

删除人物姓名、故事结局、私人肖像、绝对路径、未发布台词和无授权媒体内容。证据索引可以使用项目内 Case ID，但不复制受限素材。
