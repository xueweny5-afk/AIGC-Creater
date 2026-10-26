# ASSET MANIFEST

## PROJECT

- **Project ID：** FPD-20261002-他们把爱写进了千年
- **Visual Bible：** `../visual-development/world-visual-bible.md` v3
- **Manifest Version：** v10，2026-10-12；新增四位留下者的后来年龄状态照
- **当前执行方式：** 用户自行生成资产图；缺图交接见 `prompts/remaining-assets-handoff-v1.md`
- **范围：** G2 已通过的 S001–S008。用户确认当前上传的资产视觉方向；PROP01 卷角与 PROP04 空碗状态图经图像复核后，G3 按本片当前可见范围通过，详见 `../qc/g3-asset-review-2026-10-11.md`。

## 当前进度

| 分类 | 已生成的有效目标图 | 计划目标图 | 仍缺 |
|---|---:|---:|---:|
| 八位人物身份照、头部角度、全身六视图 | 88 | 88 | 0 |
| 八套独立衣装四图及穿着组合六视图 | 80 | 80 | 0 |
| 四处场景主视、左右约 30°、材料细节 | 10 | 16 | 6 |
| 四组道具基础、状态及材料细节 | 6 | 11 | 5 |
| **合计** | **184** | **195** | **11** |

候选/返工图不计入有效目标图：CH01/CH02 的 `head-right45-v1.png` 已由 v2 替代，CH03/CH04 的旧正脸候选已由 v2 替代，LOC04 的 `topology-main-v1-candidate.png` 已由正式版替代。不要把这些候选图用作后续母图。

另有 4/4 张**新增的后来年龄状态照**，不计入原 195 张资产目标：`characters/CH01/later-face-front-v1.png`、`CH03/later-face-front-v1.png`、`CH05/later-face-front-v1.png`、`CH07/later-face-front-v1.png`。它们只锁后镜脸部与发丝的年龄状态；四张图中的衣服均发生变化，**不作为衣装参考**，衣装仍以各角色 `combined-CSTxx-front-v1.png` 与 CST 资产为准。视觉复核见 `../qc/later-age-state-review-2026-10-12.md`。

## ASSETS

状态：`USER_APPROVED_EXISTING` 表示用户确认当前入库的图；`REVIEWED_STATE` 表示新增关键状态已按视觉连续性复核；`PARTIAL` 表示只完成部分计划角度/细节。G3 仅覆盖本片当前可见需求，不表示未生成的 11 张计划图存在。独立合同在各资产目录的 `asset-contract.md`，有旧的计划状态时以本次盘点和实际图片为准。

| Asset ID | Type | Working Name | Priority | 现状与准确母图 |
|---|---|---|---|---|
| CH01 | CHARACTER | 李清照 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH01/canon-face-front-v2.png`，右前 45° 头部用 `head-right45-v2.png`；后来脸部状态 `later-face-front-v1.png`；组合六视图已入库 |
| CH02 | CHARACTER | 赵明诚 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH02/canon-face-front-v2.png`，右前 45° 头部用 `head-right45-v2.png`；组合六视图已入库 |
| CH03 | CHARACTER | 苏轼 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH03/canon-face-front-v2.png`；后来脸部状态 `later-face-front-v1.png`；组合六视图已入库 |
| CH04 | CHARACTER | 王弗 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH04/canon-face-front-v2.png`；组合六视图已入库 |
| CH05 | CHARACTER | 陆游 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH05/canon-face-front-v1.png`；后来脸部状态 `later-face-front-v1.png`；组合六视图已入库 |
| CH06 | CHARACTER | 唐氏 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH06/canon-face-front-v1.png`；组合六视图已入库 |
| CH07 | CHARACTER | 沈复 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH07/canon-face-front-v1.png`；后来脸部状态 `later-face-front-v1.png`；组合六视图已入库 |
| CH08 | CHARACTER | 陈芸 | P0 | `USER_APPROVED_EXISTING`；11/11；正脸 `characters/CH08/canon-face-front-v1.png`；组合六视图已入库 |
| CST01–CST08 | COSTUME | 八人衣装 | P0 | `USER_APPROVED_EXISTING`；独立正/侧/背/织物细节 32/32，穿着组合六视图 48/48 |
| LOC01 | LOCATION | 李赵书房 | P0 | `PARTIAL`；主、左 30°、右 30° 已有；缺 `detail-surface-v1.png` |
| LOC02 | LOCATION | 苏王书房 | P0 | `PARTIAL`；主、左 30°、右 30° 已有；缺 `detail-surface-v1.png` |
| LOC03 | LOCATION | 春园石径 | P0 | `PARTIAL`；主、右 30° 已有；缺 `topology-left30-v1.png`、`detail-surface-v1.png` |
| LOC04 | LOCATION | 沈陈居所 | P0 | `PARTIAL`；正式主视、左 30° 已有；缺 `topology-right30-v1.png`、`detail-surface-v1.png` |
| PROP01 | PROP | 碑拓 | P0 | `REVIEWED_STATE`；`flat-v1.png` 与 `corner-curled-v1.png` 已有；右上角卷起、主体墨拓延续；缺未入镜的纸材细节 |
| PROP02 | PROP | 摊开的书 | P0 | `PARTIAL`；`open-page-v1.png` 已有；缺指定行状态、纸页细节 |
| PROP03 | PROP | 折信 | P0 | `PARTIAL`；`folded-v1.png` 已有；缺折痕细节 |
| PROP04 | PROP | 双碗、筷与菜 | P0 | `REVIEWED_STATE`；`two-bowls-v1.png` 与 `opposite-empty-v1.png` 已有；左碗留饭菜、右碗清空，双碗位置延续；缺未入镜的陶瓷细节 |

人物图单独归 `characters/`；服装独立图归 `costumes/`；穿着组合图归对应 `characters/CHxx/`；场景和道具按 ID 归各自目录。服装仅为有时代语境的创作设计，不能宣称为考据复原。

## NEXT STAGE

按 `../qc/g3-asset-review-2026-10-11.md` 的当前可见范围 G3 结论，Stage 10 镜头设计和 Stage 11 静态分镜已完成当前版，Stage 12 运动规格见 `../motion/motion-spec.md`。LOC03 左角度、LOC04 右角度、材料细节及书页定位图不在当前机位引用范围，按需再补。已有角色、空间和道具状态母图保持版本，不重抽已通过内容。
