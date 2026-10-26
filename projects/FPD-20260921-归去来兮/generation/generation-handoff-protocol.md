# GENERATION HANDOFF PROTOCOL

## PROJECT DECISION

- **Project ID：** FPD-20260921-归去来兮
- **Decision Date：** 2026-09-24
- **Generation Policy：** CONFIRM PER BATCH
- **Available Modes：** AUTO_GENERATE / USER_GENERATE
- **Current Batch Mode：** USER_GENERATE
- **Review Owner：** Codex
- **Purpose：** Codex 先完成提示词编排与依赖控制，再由用户为每个新批次选择自动生成或自行生成；无论来源如何，均由 Codex 执行像素审核、返工判断、命名与归档。

## MODE CONFIRMATION

- 每个新批次在提示词完整展示后，只确认一次生成方式。
- `AUTO_GENERATE`：Codex 使用当前可用图像工具生成，并逐张审核。
- `USER_GENERATE`：用户在网页模型或统一会话中生成并回传，Codex 逐张审核。
- 当前批次的选择不自动继承到下一批；连续动作的依赖帧属于同一批，批内不重复询问。
- 用户未作选择前，提示词可以准备和修改，但不得开始实际生图。

## REQUIRED LABELS

每条生成任务必须包含：

1. `Batch ID`
2. `Asset ID / Frame ID`
3. `CREATE NEW` 或 `EDIT FROM <ID>`
4. `Target Filename`
5. `Reference Images`：逐张编号并说明唯一用途
6. `Positive Prompt`
7. `Negative Prompt`
8. `Locked Continuity`
9. `Review Checklist`

## DEPENDENCY ORDER

```text
人物主参考
→ 人物三视图与状态
→ 服装状态
→ 场景拓扑与关键道具
→ 人物入景分镜
→ 连续动作的 Start / Intermediate / End
→ 动态设计与视频生成
```

- 上游母图未批准时，不批量派生下游图。
- 同一人物尽量在同一个网页会话中持续生成，并重复上传已批准身份母图。
- 连续动作使用上一张批准图作为编辑母图，不把每一帧当成独立新图。
- 人物、服装、场景和道具可以按同一阶段集中交付提示词，但仍按依赖顺序生成。

## USER RETURN FORMAT

- 最佳文件名：`<Asset ID or Frame ID>.png`
- 无法改名时：上传图片并逐张注明对应 ID。
- 多张图不要只写“第一张、第二张”；以 ID 作为唯一对应关系。

## REVIEW RESULT

Codex 对每张回传图输出：

- `PASS`：身份、结构、连续性和范围通过，可归档。
- `REWORK`：只列失败字段并提供定向返工提示词。
- `REJECT`：存在身份、时代、拓扑或关键动作错误，不进入下游。

审核通过不等同于历史精确复原；研究推定与原创部分继续按资产合同标记。
