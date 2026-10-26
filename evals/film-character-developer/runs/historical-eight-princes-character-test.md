# Film Character Developer Run｜八王之乱历史人物

## Input

- `fixtures/historical-eight-princes/project-brief.md`
- `fixtures/historical-eight-princes/story-blueprint.md`
- `projects/FPD-20260917-八王之乱瞬间/research/research-pack.md`

## Output

- `outputs/historical-eight-princes-character-system.md`

## Observed Behavior

- 使用 `EVIDENCE_LIMITED`，没有强行为司马玮和张华补齐目标、恐惧、世界观或私下动机。
- 只使用 CLM-002、CLM-003 支持的行动；Claim 均可回到 Research Pack。
- 把军众保留为内部差异未知的共同体，没有虚构“代表全军的觉醒士兵”。
- 因传令者身份、命令链和人物心理依据不足，正确路由到 `Research Return`。
- 未输出对白、场景、镜头、物件形制或宫斗式人物反转。

## Rubric

1. Continuity Fidelity：2/2
2. Cast Economy：2/2
3. Agency / Evidence Restraint：2/2
4. Relationship Pressure：2/2
5. Reality & Research Boundary：2/2
6. Originality Discipline：2/2
7. Production Continuity：2/2
8. Boundary & Handoff：2/2

- **Score｜得分：** 16/16
- **Hard Failures｜硬失败：** None observed
- **Status｜状态：** PASS

## Skill Change Triggered

初版人物卡字段可能诱导真实人物心理填充。已增加 `EVIDENCE_LIMITED` 模式，允许无依据字段明确保持 `UNKNOWN`，并把历史人物的 agency 限制为可核实行动与职权。
