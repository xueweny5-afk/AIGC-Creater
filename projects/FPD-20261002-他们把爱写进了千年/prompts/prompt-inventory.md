# 《他们把爱，写进了千年》提示词总索引

> **2026-10-12 当前入口：** 用户已指定 Seedance 2.5。Stage 13 新版见 [`seedance-2-5/video-prompt-package.md`](seedance-2-5/video-prompt-package.md)、[`seedance-2-5/model-profile.md`](seedance-2-5/model-profile.md)、[`seedance-2-5/coverage-receipt.md`](seedance-2-5/coverage-receipt.md)。八张 `key-v2.png` 已入库并获用户画面认可；旧 MiniMax 与旧模型中立包仍只作历史记录。SH06 因现有帧是动作终态，须先按 [`seedance-2-5/sh06-start-frame-handoff.md`](seedance-2-5/sh06-start-frame-handoff.md) 补一张起始帧。以下 2026-10-03 内容为当时记录，旧 G3/G4 状态不代表当前关口。

**版本：** 2026-10-03  
**项目边界：** 用户自行生成图片；本项目暂不制作视频。  
**创作主版本：** `../screenplay/screenplay.fountain` v3（G2 已通过）。  
**当前关口：** G3 未通过；八张旧首帧只是已认可的视觉方向，不是批准的独立资产或新版动作分镜。

## 现在可以取用：Stage 08 独立资产提示词

想在一个文件里顺序复制，打开[全部独立资产生图提示词合订本](../assets/prompts/all-asset-prompts-v1.md)；想分批查看，打开[用户生图总交接](../assets/prompts/user-generation-handoff-v1.md)，按其中的依赖顺序操作：

| 批次 | 具体提示词 | 用途 | 状态 |
|---|---|---|---|
| FA-01 | [八位人物正面身份](../assets/prompts/face-anchor-batch-01.md) | 每人一张独立正面脸；先回传审核 | USER_GENERATE / READY FOR USER |
| FA-REPAIR-01 | [CH01/CH02 正脸画幅修复记录](../assets/prompts/CH01-CH02-face-framing-repair-v1.md) | 保留已生成的脸，只扩图补全发髻顶部 | DONE / v2 FACE APPROVED |
| FA-REPAIR-02 | [CH03/CH04 正脸画幅修复](../assets/prompts/CH03-CH04-face-framing-repair-v1.md) | 保留苏轼、王弗现有脸与发髻，只增加上方留白 | USER_GENERATE / REWORK |
| LOC-MV-01 | [四处场景多角度](../assets/prompts/location-multiview-v1.md) | 每处先无人主视，审核后同母图左/右约 30° 和材料板 | USER_GENERATE / READY FOR USER |
| CH-MV-01 | [人物头部五角度、全身六视图](../assets/prompts/character-multiview-v1.md) | 从同一已批准正脸与全身正面逐张编辑派生 | HANDOFF / DEPENDS ON APPROVED FACE |
| CST-LOOK-01 | [八套服装与组合六视图](../assets/prompts/costume-combined-multiview-v1.md) | 独立服装正/侧/背和材料板，再与身份图组合 | HANDOFF / DEPENDS ON APPROVED FACE/BODY/COSTUME |
| PROP-01 | [四组关键道具与状态](../assets/prompts/prop-state-v1.md) | 碑拓、书、折信、双碗的基础图、变化态及材料板 | USER_GENERATE / BASE BEFORE EDITED STATE |

**第一轮原计划 12 张母图：** CH01/CH02 修复版正脸已通过 AI 自审，身份母图均为 `canon-face-front-v2.png`；CH03/CH04 正脸候选需按 FA-REPAIR-02 增加上方留白；CH05–CH08 正脸及 LOC01–LOC04 无人主视仍待回传。CH01/CH02 可按 [人物多角度提示词](../assets/prompts/character-multiview-v1.md)从 v2 逐张派生并回传审核；不要凭相同文字独立重抽角度图。

## 尚不可取用：Stage 11 / 13 分镜与图生视频提示词

| 类别 | 现有文件 | 当前结论 | 放行依赖 |
|---|---|---|---|
| 旧分镜生图记录 | `frame-generation.md` | 2026-10-02 历史生成记录；含旧双层画面，不能用于新版动作 | G3 后从新版 Shot/Frame 合同重写八场关键帧词 |
| 旧八镜整合稿 | `八镜制作总稿.md` | STALE：无新版四句对白、按纸/指页/回身/夹菜 | G3 → Scene/Shot → G4 → Motion → Stage 13 |
| 旧模型中立图生视频词 | `pre-video-prompt-package.md` | STALE：仍写托腮、泛化手势和旧首帧 | 新版 Motion Spec、G4 与目标模型 Profile |
| 旧 MiniMax-H3 包 | `minimax-h3/prompt-package.md` | STALE：旧动作与音频方案，不能提交 | 同上；另需核实当前模型能力和输入模式 |

**为什么此处不能先写可执行八镜词：** 当前 G2 剧本已锁定“短对白得到回应，硬切后相同动作无人接续”，但 CH/LOC/PROP 的独立图还不存在；旧分镜图没有这些新动作，旧 Shot/Motion 也未按新版重编。现在写成可执行镜头提示词会让模型重新发明人物、空间和动作，违背本项目的多角度一致性要求。`../direction/scene-design-pack.md` v3 已先把八场动作对齐，状态为 `DRAFT_ASSET_PENDING`；收到资产后从这里继续。

## 继续顺序

1. 用户从 CH01/CH02 已批准的 v2 正脸生成左右 45° 头部图并回传审核；CH03/CH04 先做画幅修复；CH05–CH08 正脸与空间主视图可并行生成回传。
2. 审核、记录 `APPROVED / REWORK`；用户再按现有资产提示词派生人物/场景多角度、服装及道具，直到当前八场 P0 达到 G3。
3. 根据已批准原图正式重编 Stage 09–12 的镜头、静态关键帧、顺序预演与运动；不重复制作旧八张图的无关部分。
4. 编译八场逐镜**分镜生图提示词和图生视频提示词**，每条绑定真实 Asset/Frame ID、路径、版本、参考用途与目标模型参数。此时才标为可供用户自行取用的视频前交接包；本项目仍不提交视频生成任务。

**流程依据：** `../qc/workflow-gate-audit.md` 与仓库 `pipeline/film-production-pipeline.md`；本索引只汇总状态，不替代分阶段主合同。
