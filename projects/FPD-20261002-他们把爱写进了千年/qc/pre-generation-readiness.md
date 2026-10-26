# 生成前审查与交接｜2026-10-02

> **状态更正：** 本文件记录较早的自审判断；按项目 V1.9 流程的最新关口结论以 `workflow-gate-audit.md` 为准。当前 G2/G3/G4 未正式通过，后续提示词是草稿，不得作为可执行包。

## 当前交付

已形成可审查的四组八镜方案：项目简报、史料与出处、故事和人物、对照处理、执行剧本及文字登记、视觉基线、场景/镜头表、八张独立首帧、联系表、运动规格、模型中立与 MiniMax-H3 逐镜提示词、13 项覆盖回执、Unit Cards 与未来试镜计划。逐阶段核对见 `pre-video-workflow-walkthrough.md`。统一视觉事件是 **温馨双人 → 同地同物硬切 → 一人和空位**；八镜共 24 秒。没有进行新的视频生成。

## 流程门状态

| 门 | 当前证据 | 结论 |
|---|---|---|
| G0 Scope Lock | `../project-brief.md` 记录用户修订与“仅生成前”范围 | 通过；发布平台等开放项已明示 |
| G1 Research Ready | `../research/research-pack.md`、`../research/source-index.md` | 有条件通过；史料不确定性已标，片中不宣称唐氏本名为可核史实 |
| G2 Creative Master | `../story/`、`../characters/`、`../treatment/`、`../screenplay/screenplay-master.md`、`../screenplay/screenplay-register.md` | 工作版完成；逐字字幕仍为执行提案 |
| G3 Visual Asset Ready | `../visual-development/world-visual-bible.md`、`../assets/asset-manifest.md`、八张独立首帧 | 当前 S01–S08 范围通过：用户认可联系表与人物外观；P0 是影像重构参考，非史学原貌认证 |
| G4 Static Storyboard Ready | `../direction/shot-list.md`、`../storyboard/frame-manifest.md`、`../storyboard/sequence-review.md`、联系表与节奏图 | 当前八镜静帧通过：用户于 2026-10-02 回复“可以的”；严格动作匹配仍非当前合同 |
| G5 Technical Pilot Validated | `../prompts/prompt-coverage-receipt.md`、`../prompts/minimax-h3/prompt-manifest.md`、`../generation/production-unit-cards.md`、`../generation/generation-manifest.md` | 未开始；H3 官方规格已核，当前账户提交能力和真实 Take / QC 未验证，用户本阶段禁止视频生成 |
| G6–G8 | 需真实镜头、后期和交付 | 不在当前范围 |

## 逐对可见风险与解决路径

| 镜头对 | 静帧核查 | 视频试镜时必须证明 |
|---|---|---|
| S01/S02 | 碑拓和书案同物可读；前后手势不同 | 手指正常、以碑拓承接硬切仍然顺畅 |
| S03/S04 | 书页和空椅清楚；苏轼均托腮 | 侧目时脸稳定、书页不乱变 |
| S05/S06 | 石径和月洞门连续；折信较小 | 路径轴线不漂、手中信件不变形 |
| S07/S08 | 两只碗和空席最清楚；沈复的手势前后不同 | 餐具数量稳定、碗的位置与硬切节奏成立 |

## 执行前仍需确定

1. **字幕审批：** 以 `../screenplay/screenplay-master.md` 为准；创作文案与古籍原句不得混标。唐氏人名卡需要进一步决定呈现方式。
2. **未来模型实测：** MiniMax-H3 模型专用包已编好；实际提交前须核实账户余额/计费入口，并以 S07/S08 做技术试镜，再按 `../generation/generation-manifest.md` 扩展。若改用其他模型，从当前源合同重新编译。

**边界：** 当前八镜视觉和静帧已获用户认可，前期包可供未来技术试镜；不等同于已生成视频、真实 Take 通过或成片锁定。用户限定本阶段不制作视频。
