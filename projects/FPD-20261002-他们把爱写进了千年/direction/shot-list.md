# SHOT LIST｜v4｜G2 沈陈动作修订 / G4 用户认可静帧

## 基准

- **Project ID：** FPD-20261002-他们把爱写进了千年
- **日期 / 阶段：** 2026-10-11 / Stage 10 Shot Design
- **事实源：** `../screenplay/screenplay.fountain` v3；`scene-design-pack.md` v5；`../visual-development/world-visual-bible.md` v3；`../assets/asset-manifest.md` v9；`../qc/g3-asset-review-2026-10-11.md`
- **状态：** `SHOT_DESIGN_CURRENT / G4 PASS WITH USER-APPROVED COMPOSITION VARIATION`。SH07 依用户批准静帧修订为沈给陈递菜。当前八张 `../storyboard/frames/*/Sxx-key-v2.png` 均已入库并获用户认可；前三组前后景别有差异，实际生成以获批帧为准，不宣称像素级匹配。
- **形式：** 9:16 竖屏；沿用已认可的画面中部横向叙事区。四组各以双人镜头突然硬切至**同位置同角度**的一人镜头；绝不在同一镜头里使另一人消失，也不同时上下并置两时态。
- **时长：** 8 镜 × 暂定 3 秒 = 24 秒。具体对白、停顿与切点由 Stage 11 Animatic 检验；若声音/动作放不下，先调整时长，不删除剧本动作。
- **镜头策略：** 每组一个固定主机位，前后沿用相同画面边界、桌/路径轴线、物件方位和人物屏幕位置。只选择四处场景已入库主视所证明的可见区域；当前不使用 LOC03 左 30°、LOC04 右 30° 或任何未生成的背墙。

## 机位与关系轴

| 场景组 | 固定画面锚点与主体位置 | 关系轴 / 前后匹配 | 未知边界 |
|---|---|---|---|
| F01 / LOC01 | 正对横向书案，书架在后左、格窗及灯在后右；李在画面左，赵在右；碑拓位于两人可触及的案面中区 | 机位保持书案前侧，前后都不跨越“李—纸角—赵”轴；赵缺席后原右位清楚可见 | 不拍未证实的书房背墙 |
| F02 / LOC02 | 正对书桌，两把座椅在桌后；苏在左、王在右；书在桌面中区、王位靠画面右 | 机位保持桌前，前后右侧空椅不换边；书的右页中部同一竖列为指位 | 不显示真实可读书文或桌背未知区域 |
| F03 / LOC03 | 从石径前景望向后方圆门；桃枝左上、假山左侧；陆在前景偏左，唐在其身后偏右 | 两镜都在同一路段、同一观望方向；陆回身朝画面右后方伸手；后镜唐原位空 | 不绕至园门外或未知左侧路径 |
| F04 / LOC04 | 正对横向饭桌，格窗在后；沈坐画面左、陈坐右；左碗为沈碗、右碗为陈碗 | 机位保持桌前，双碗左右和两坐席前后不变；后镜陈右席及右碗空 | 不拍未证实的居所背墙 |

灯光在 Stage 11 按 `LLS-LOC01–04-TOGETHER/ALONE-v1` 实现：三处室内的夜景必须从图中已有的灯位出发；后镜可降低环境活跃度，但不得换房、换灯位或在切口中让光源瞬变。园路保持自然天光，空气均为 `NONE / CLEAN AIR`。

## 锁定资产引用字典

下表镜头行使用这里的短 ID；每项绑定的是项目 `assets/` 下的**确切文件版本**。当前八镜均从已有场景主视的正面方向取景；Stage 11 若改用侧面或反打，先回 Stage 10 更改机位与对应同角度组合图，再核对场景角度是否存在。

| 短 ID | 确切文件 |
|---|---|
| CH01/CST01 | `characters/CH01/canon-face-front-v2.png`；`characters/CH01/combined-CST01-front-v1.png`；`costumes/CST01/front-v1.png` |
| CH02/CST02 | `characters/CH02/canon-face-front-v2.png`；`characters/CH02/combined-CST02-front-v1.png`；`costumes/CST02/front-v1.png` |
| CH03/CST03 | `characters/CH03/canon-face-front-v2.png`；`characters/CH03/combined-CST03-front-v1.png`；`costumes/CST03/front-v1.png` |
| CH04/CST04 | `characters/CH04/canon-face-front-v2.png`；`characters/CH04/combined-CST04-front-v1.png`；`costumes/CST04/front-v1.png` |
| CH05/CST05 | `characters/CH05/canon-face-front-v1.png`；`characters/CH05/combined-CST05-front-v1.png`；`costumes/CST05/front-v1.png` |
| CH06/CST06 | `characters/CH06/canon-face-front-v1.png`；`characters/CH06/combined-CST06-front-v1.png`；`costumes/CST06/front-v1.png` |
| CH07/CST07 | `characters/CH07/canon-face-front-v1.png`；`characters/CH07/combined-CST07-front-v1.png`；`costumes/CST07/front-v1.png` |
| CH08/CST08 | `characters/CH08/canon-face-front-v1.png`；`characters/CH08/combined-CST08-front-v1.png`；`costumes/CST08/front-v1.png` |
| LOC01 | `locations/LOC01/topology-main-v1.png` |
| LOC02 | `locations/LOC02/topology-main-v1.png` |
| LOC03 | `locations/LOC03/topology-main-v1.png` |
| LOC04 | `locations/LOC04/topology-main-v1.png` |
| PROP01-CURLED / FLAT | `props/PROP01/corner-curled-v1.png` / `props/PROP01/flat-v1.png` |
| PROP02-OPEN | `props/PROP02/open-page-v1.png` |
| PROP03-FOLDED | `props/PROP03/folded-v1.png` |
| PROP04-BASE / EMPTY | `props/PROP04/two-bowls-v1.png` / `props/PROP04/opposite-empty-v1.png` |

PROP04 母图展示一双筷子的材质和形制。当前 SH07/08 已认可静帧里仅沈的一双筷子可见，归沈右手；陈以目光回应，不要求她在此刻持筷。后镜仍只保留沈的一双可见。

## 八镜执行合同

| Shot / Scene | 暂定时间 | MAIN / SUPPORT / HOLD | 画面任务、动作与切点 | 当前确切资产与光态 | 声音 / 下一镜 |
|---|---|---|---|---|---|
| SH01 / S001 | 0–3s | MAIN：两人共同按纸；SUPPORT：卷角 | 中景双人同案。李右手按碑拓中部，把右上卷角推给右侧赵，说「帮我按住」；赵伸手按住同一角，李继续看纸。回应刚完成即硬切。 | CH01/CST01、CH02/CST02、LOC01、PROP01-CURLED→FLAT；LLS-LOC01-TOGETHER-v1 | 一句对白、纸声；切口抽掉回应的人声 |
| SH02 / S002 | 3–6s | MAIN：李独自按同角；HOLD：赵原位空 | 与 SH01 同机位同桌。右侧赵位已空；同一右上角再次卷起，李望向右侧空位，自己伸手按住；短暂留住空位。 | CH01/CST01、LOC01、PROP01-CURLED→FLAT；LLS-LOC01-ALONE-v1 | 纸角回弹后纸声止；静默切 F02 |
| SH03 / S003 | 6–9s | MAIN：王指书、苏找到位置；SUPPORT：目光回应 | 中景同桌双人。王在右，指向打开书右页中部固定竖列，说「在这一页」；苏在左，先看指位再抬眼看她。对视未拉长即硬切。 | CH03/CST03、CH04/CST04、LOC02、PROP02-OPEN；LLS-LOC02-TOGETHER-v1 | 一句对白、轻触纸声；切口去人声 |
| SH04 / S004 | 9–12s | MAIN：苏的手停在同列；HOLD：王右侧空椅 | 与 SH03 同机位同页。苏的指尖停在右页中部同一竖列，抬眼看右侧空椅；不翻页、不托腮。引文「十年生死两茫茫」只由后期叠加。 | CH03/CST03、LOC02、PROP02-OPEN；LLS-LOC02-ALONE-v1 | 书页轻响后静默；视线停住切 F03 |
| SH05 / S005 | 12–15s | MAIN：唐呼唤、陆回身伸手 | 石径中景双人。陆在前景偏左，唐落后半步在右后方；唐停下说「等等我」，陆朝她回身伸手，她向他靠近；手将接近时硬切。 | CH05/CST05、CH06/CST06、LOC03；LLS-LOC03-TOGETHER-v1 | 一句对白、双人脚步；硬切后只余一组脚步 |
| SH06 / S006 | 15–18s | MAIN：陆重复伸手又收回；HOLD：唐原位空 | 与 SH05 同路同机位。陆朝画面右后方回身伸出同一只手；唐不在，停一瞬后收手，低头看另一手里未展开的折信。引文「山盟虽在，锦书难托」由后期叠加。 | CH05/CST05、LOC03、PROP03-FOLDED；LLS-LOC03-ALONE-v1 | 单人脚步、自然风；收手后静默切 F04 |
| SH07 / S007 | 18–21s | MAIN：沈把菜夹入陈的右碗；SUPPORT：陈抬眼回应 | 饭桌中景双人。沈在左，用自己的一双筷子从左碗夹起一口青菜送入陈的右碗，说「尝尝这个」；陈在右抬眼看他，菜落入右碗后硬切。两碗始终可见。 | CH07/CST07、CH08/CST08、LOC04、PROP04-BASE；LLS-LOC04-TOGETHER-v1 | 沈的一句对白、筷碰碗轻响；切口停住人声 |
| SH08 / S008 | 21–24s | MAIN：沈向空碗夹菜又停；HOLD：右碗空 | 与 SH07 同机位同桌。陈右席空，右碗仍在原位且完全空；沈从左碗夹起一口青菜，筷子移向右碗前停住，放下筷子。结束留住空碗，不托腮、不出现陈的幻影。 | CH07/CST07、LOC04、PROP04-EMPTY；LLS-LOC04-ALONE-v1 | 熟悉的筷碗声落空，安静结束 |

## 手部与接触锁定

| 镜头对 | 同一动作的手部方向 | 接触点 |
|---|---|---|
| SH01/02 | 李用右手触纸；SH01 赵用靠近纸角的左手接住，SH02 李的右手独自伸至同角 | PROP01 画面右上角，只允许这一角卷起和按平 |
| SH03/04 | SH03 王用靠近书页的左手指位；SH04 苏用右手停在同一位置 | PROP02 右页中部同一竖列，不翻页 |
| SH05/06 | 陆用右手向画面右后方伸出；SH06 左手持未展折信 | 唐原来站在陆右后方，后镜此处为空 |
| SH07/08 | 沈两镜都用右手持同一双筷子，从自己左碗夹菜向陈右碗递；SH07 陈以目光回应 | SH07 菜落陈右碗；SH08 筷在同一右空碗前停住，不把菜放进去 |

## Stage 11 交接

- 每组先做一张前后**同机位构图指南**，标出人物/空位、核心物件、画面边界、关系轴和文字安全区；再从当前资产生成新的动作关键帧。旧 `S01–S08-start-v1.png` 不直接充当新动作帧。
- SH01/02 先核对“右上角卷起 → 同角按平”；SH03/04 核对“右页同一竖列”；SH05/06 核对“回身同方向、折信在另一手”；SH07/08 核对“左沈右陈、两碗位置、右碗空”。
- 先按 `shot-continuity-ledger.md` v3 检查八张新关键帧，再做整段顺序预览与节奏审核。没有实际新帧和 Animatic 前，G4 保持 `PENDING`。
