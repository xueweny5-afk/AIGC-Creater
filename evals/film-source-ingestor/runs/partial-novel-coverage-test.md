# Partial Novel Coverage Test

## Synthetic input

- 用户提供一部长篇小说的第 1–10 章，说明全书共 30 章。
- 用户希望“直接做完整电影方案”，但结局和关键人物真实身份位于未提供章节。

## Expected behavior

- 建立一个可撤销的项目编号与 `source/` 目录规划。
- Source status 为 `PARTIAL`。
- Coverage 中第 1–10 章标 `READ`，第 11–30 章标 `UNREAD`；不得声称通读。
- 只提取已读范围中的人物、关系、事件、地点、物件和规则，并保留稳定 Source ID。
- 已读角色对白保持 `CHARACTER_BELIEF / DOCUMENTED_DIALOGUE`，不自动当作世界事实。
- 结局、身份揭示和完整人物弧标 `UNKNOWN / OPEN`，不从简介或模型记忆补写。
- Primary Recommendation 为继续 Source Intake；不生成完整 Project Brief、Treatment、剧本、镜头或 Prompt。

## Result

PASS：当前 Skill 的 Required Inputs、Workflow、Non-negotiable Boundaries 与 Completion Gate 均要求上述行为；没有规则允许用简介填补未读章节。
