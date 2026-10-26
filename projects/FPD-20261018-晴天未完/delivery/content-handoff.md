# 《风进来的下午》工作流文字交接 v1.0

> 当前迭代已转向[v2第一人称样例](pov-v2-handoff.md)，依据用户对实际生成效果的反馈。本页保留v1文字范围与历史检查，不表示v1达到用户审美目标。

Project ID：FPD-20261018-晴天未完｜2026-10-18｜U01 Prototype Unit｜CONTENT_ONLY。

本次按[pipeline/film-production-pipeline.md](../../../pipeline/film-production-pipeline.md) v1.27补齐样例文字链，终止Stage 13。当前只是一个原型，不称“第一集”；系列结构、人物复用及正式片名仍可调整。

## 先看这个样例

夏日午后，一位成年人坐在窗边看书。风使白纱帘向室内鼓起，窗外绿地露得更多。阅读者先停顿，再抬眼望向窗外。帘子回落，人仍安静看着外面。

目标是舒服、惬意、略带梦感。蓝天、自然绿、奶白和浅木色维持清透关系；光柔和但人、书、白布和云都可辨。约12秒、16:9、单镜头是本次提案，不是用户硬性锁定规格或平台能力承诺。

## 阶段责任与入口

| Stage | 当前责任产物 | 本轮检查与状态 |
|---|---|---|
| 00 Source Intake | 不适用 | 没有长篇原作改编；用户视频进入参考研究 |
| 01 Project Direction | [Project Brief](../project-brief.md) | G0 READY仅限原型定义；用户意图/假设/开放项已分开 |
| 02 Research | [Research Pack](../research/research-pack.md)、[Source Index](../research/source-index.md)、[原片Study](../research/reference-study.md) | G1 READY仅当前虚构文字范围；视频Study仍PARTIAL，未试听音轨 |
| 03 Story | [Story Blueprint](../story/story-blueprint.md) | 阅读→环境吸引→停留；文字SELF-AUDIT READY |
| 04 Character | [Character System](../characters/character-system.md) | 一位Prototype-only阅读者；文字SELF-AUDIT READY |
| 05 Treatment | [Complete Treatment](../treatment/treatment.md) | 完整散文过程与段落映射；文字自检PASS |
| 06 Screenplay | [剧本正文](../screenplay/screenplay.fountain)、[Register](../screenplay/screenplay-register.md) | 覆盖S001 COMPLETE，文字自检PASS；时长ESTIMATED |
| 07 Visual Development | [Visual Bible](../visual-development/world-visual-bible.md)、[Requirements](../visual-development/asset-requirements.md)、[Reference Analysis](../visual-development/reference-analysis.md) | 文本可交资产规划，像素与审美效果尚未验证 |
| 08 Asset Design | [Manifest及五项合同](../assets/asset-manifest.md) | PLAN_ONLY，全部PLANNED；真实图像和Approval Scope NONE |
| 09 Scene Direction | [Scene Design Pack](../direction/scene-design-pack.md) | DRAFT_ASSET_PENDING；含空间示意、行动回应与PB01 |
| 10 Shot Direction | [Shot List](../direction/shot-list.md)、[Continuity Ledger](../direction/shot-continuity-ledger.md) | SHOT EXPLORATION；单镜约12秒、左人右帘、同侧短前移 |
| 11 Storyboard | [Plan](../storyboard/storyboard-plan.md)、[Readable Sheet](../storyboard/storyboard-sheet.md)、[Frame Manifest](../storyboard/frame-manifest.md) | PLANNED；一个Shot、两个状态合同；CG01未生成，非实际分镜图 |
| 12 Motion | [Motion Spec](../motion/motion-spec.md)、[Clip Ledger](../motion/clip-state-ledger.md) | MOTION EXPLORATION；时间闭合、触发与保持明确，动态未验证 |
| 13 Prompt Adapter | [Prompt Package v1.1](../prompts/model-neutral/sample-package.md)、[Unit Cards](../prompts/model-neutral/production-unit-cards.md) | CONTENT DRAFT / NOT_READY；具体平台Profile UNVERIFIED，不提交生成 |

每个Stage记录自己的来源与审阅范围；SELF-AUDIT不是用户批准或独立审核，不从文字检查外推生产Gate通过。

## 当前放行边界

- 已交付：以上各阶段的当前原型文字内容；不要求先回传图片/视频才能拿到文本。
- G2：创作文字链已自检并可供用户整包审阅，尚未登记用户批准；不是整片生产放行。
- G3：真实资产/具体用途未批准，未通过。
- G4：构图图与真实Frame未生成，未通过。多镜Sequence/Animatic Gate对此单镜不适用；同镜静态与运动验证仍待补。
- G5：具体模型入口、真实技术样例与QC未验证。
- Stage 14—17及G6—G8：未进入；没有生成、媒体QC、后期、成片或母版交付。“delivery”内本文件只是文字交接入口。

## 版本与历史

当前创作主版本依次是Brief、Blueprint、Character、Treatment、Screenplay、Visual、Asset、Scene、Shot、Frame、Motion。Prompt和单元卡为派生视图，不反向定义事实。

早期[系列方向](../story/series-exploration.md)与[样例合稿v0.1](../direction/afternoon-sample.md)保留为探索历史，不再作当前镜头或提示词来源。旧Prompt的源依赖已重编译到v1.1；未移动或删除用户原始视频及参考证据帧。

## 下一次怎么继续

先审阅当前样例是否符合用户想要的舒适、惬意与梦感；修改时从最早受影响的主稿改起，再重编译下游。继续文字修改不需重新确认分工。

实际进入生成时，再核对最新用户授权与范围、选定平台入口、批准当前P0用途和构图/Frame，并按Shot的具体风险假设做最小真实样例。不能把本轮“按工作流整理”当成提交生成任务的授权。

文字验证记录见[content-review.md](../qc/content-review.md)。
