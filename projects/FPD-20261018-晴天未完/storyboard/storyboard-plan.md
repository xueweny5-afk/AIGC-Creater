# STORYBOARD PLAN

## PROJECT

Project ID：FPD-20261018-晴天未完；Version：v1.0；Sources：[Shot](../direction/shot-list.md)、[Continuity](../direction/shot-continuity-ledger.md)、[Manifest](../assets/asset-manifest.md)均v1.0；Shot Review为文本PASS，资产Approval Scope NONE。Mode：PLAN_ONLY；Status：PLANNED；U01/S001，CONTENT_ONLY，终止Stage 13；16:9提案，变体OPEN。Method：NONE。

## SCRIPT → SHOT → FRAME COVERAGE

只读继承上游，Frame不新增动作或机位。

| Order | Source Scene / Beat | Shot / Function | Framing / Composition | Action / Camera | Sound | Duration / Cut | Frames / Coverage |
|---|---|---|---|---|---|---|---|
| 1 | S001/B01—B03，完整剧本 | S001-SH01，感知打开 | 斜向环境中景，左人右帘，书和窗外可读 | 阅读→帘起→抬眼→保持；一次短前移后停 | A01—03，无对白，无音乐 | 约12秒，结尾保持约3秒 | F01起始、F02结束对照；文字映射COMPLETE，图像未验证 |

## FRAME SELECTION

| Frame | Type / Instant | Earning Reason | Depends On | Real File / Status |
|---|---|---|---|---|
| S001-SH01-F01 | START_KEYFRAME，0秒 | 锁阅读基线及人与窗帘关系；VID01未来起点 | C01/COS01/LOC01/P01/P02获准用途、CG01 | 无 / PLANNED |
| S001-SH01-F02 | END_KEYFRAME，约12秒 | 文字对照抬眼后状态与推近终点；非强制视频尾图输入 | F01与身份/空间回锚；CG01终点对照 | 无 / PLANNED |

不加中间帧：当前仅一条简单布料与视线链，中间接触/运动须Motion及真实Take验证；若后续证据表明需要再补。

## Composition Guide Plan

CG ID：S001-SH01-CG01，v1.0；Type：GRAYSCALE_LAYOUT；Status：PLANNED。合同见[CG01](composition-guides/S001-SH01-CG01/guide-contract.md)。

关键起始帧含前景遮挡和深度关系，因此不能标NOT_NEEDED。拟用低细节几何示意检查左人右帘、书的可见性、窗外负空间、K0/K1机位，不承担脸、服装、光色或道具版本。实际图像不存在、未COMPOSITION_APPROVED；阻断正式Frame生成，不阻断本次文字。

## DEPENDENCY & VALIDATION ORDER

先必要身份/服装/拓扑/道具用途，再CG01构图，F01起始，F02仅在需要静态状态对照或入口要求尾图时制作。F01为主要输入检查点；任何状态推断不写Actual Observation。两个计划Frame不等于两个Shot。

## APPROVED CALIBRATIONS

NONE。没有批准的资产或帧，未冻结虚假版本。

## SEQUENCE REVIEW

- 多镜Sequence Review：NOT_APPLICABLE，只有S001-SH01；Frame Review与同镜State Pair Check仍需真实图片。
- State Pair Check（文本）：F01低头、K0、书摊开；F02望窗、K1、同一人同一书；P02回到窗侧。静态像素与中间运动NOT_EVALUATED。
- Animatic Applicability：NOT_APPLICABLE（无镜头间顺序/切点）；[节奏计划](animatic/animatic-plan.md)仅承接文字节奏，不制作空预览、不冒称播放验证。
- Planned Duration：12秒估算；Observed Duration：NOT_EVALUATED；Full Playback：NONE。
- Actual Correctness / Expression / Sound / Variant Review：NOT_EVALUATED。

## BLOCKING ISSUES

真实P0用途、CG01与F01未批准，生产级G3/G4保持待验证；当前文字覆盖无冲突。

## NEXT STAGE

Motion Design的MOTION EXPLORATION文字稿，不能标READY FOR MOTION DESIGN。
