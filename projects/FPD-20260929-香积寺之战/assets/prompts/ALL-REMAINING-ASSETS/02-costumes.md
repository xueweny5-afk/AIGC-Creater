# 02｜服装与衣甲资产

每次输入对应人物的 Canon Face、Body Identity 和现有服装正面；新角度只转动人物，衣甲片数、缝线、扣带、肩部修补位置不得重造。中性灰背景、全身入画，单张一角。文件存入 `assets/costumes/<Asset ID>/`。

## COST-ANXI-FRONT-001｜主角前军衣甲

输入：`CHAR-ANXI-001/canon-face-front-v002.png`、`COST-ANXI-FRONT-001/combined-look-front-v001.png`、`combined-look-back-v001.png`、材料金属/织物板。主提示词：`同一无名军士穿同一套灰褐交领内层、深灰低光泽铁片札甲、实用腰带裤靴。人物左肩固定低对比织物修补，解剖左右不可镜像。保留前后甲片、肩带、系带、后裙甲和绑腿结构；甲可抬臂双手握长刀。真实重量，灰背景，均匀自然光。无日本武士甲、欧洲板甲、金边、礼仪装饰。`

| 本次变化 | 建议文件名 |
|---|---|
| 全身左侧；看见左肩修补与甲下布层。 | `combined-look-left-profile-v001.png` |
| 全身右侧；右肩无误加修补。 | `combined-look-right-profile-v001.png` |
| 左前 45°，胸甲、腰带和左肩修补连续。 | `combined-look-left45-v001.png` |
| 右前 45°，锁定同一脸和衣甲。 | `combined-look-right45-v001.png` |
| Dusty：暴露甲面、下摆和靴边局部积干土，头身仍清楚；不加破损。 | `state-dusty-v001.png` |
| Damaged：从 Dusty 派生，仅一两处织物撕口或扣带松动、小甲片擦损，仍可行动。 | `state-damaged-v001.png` |
| Aftermath：从 Damaged 派生，尘汗与小损伤保留，站姿疲惫，没有新伤或自动清洁。 | `state-aftermath-v001.png` |
| 双手握 B 型长刀（参考 `candidate-comparison-v002.png` 中间 B）：柄与手不穿插，肩肘可用力；仅验证衣甲活动范围。 | `action-two-hand-hold-b-v001.png` |

## COST-LISIYE-001｜李嗣业衣甲

输入：李嗣业脸/身体、`state-l0-complete-front-v001.png`、`state-l1-open-front-v001.png`、B 型刀母图。主提示词：`同一李嗣业、同一套重实战衣甲；L0 完整，L1 只沿真实扣带路径敞开外层，露出的肩胸保留自然体脂和汗尘，不变成健美造型。甲有重量，动作受力可信，不凭空脱落甲片。灰背景自然光。`

| 本次变化 | 建议文件名 |
|---|---|
| L0 背面，全身，展示扣带与甲片从正面延续。 | `state-l0-complete-back-v001.png` |
| L0 左侧，全身，外甲仍完整。 | `state-l0-complete-left-profile-v001.png` |
| L1 左侧，全身，外层敞开，位置与正面 L1 对应。 | `state-l1-open-left-profile-v001.png` |
| L1 背面，开合后衣甲由腰带与剩余扣带承重。 | `state-l1-open-back-v001.png` |
| 扣带近景，L0 与 L1 同一结构的扣合/解开关系，真实连接，不加文字。 | `detail-l0-l1-fastening-v001.png` |
| L2 推进后，从 L1 派生，只增局部汗尘和擦损，敞开位置不复原；全身正斜角。 | `state-l2-advance-v001.png` |
| L1 双手横持 B 型刀止退的受力参考，腕肘肩与柄接触，不英雄飞砍。 | `action-l1-blocking-hold-v001.png` |

## COST-GUOZIYI-001｜郭子仪中军衣甲

输入：郭子仪脸/身体、`combined-look-front-v001.png`、中军暗红旗母图。主提示词：`郭子仪在同一套中军指挥衣甲中，层级高于普通军士但仍是实战衣甲；低光泽暗铁、灰褐布与实用带具，完整维护、无帝王服装、无金色礼仪甲。脸、身形、甲片、扣带一致。灰背景自然光。`

| 本次变化 | 建议文件名 |
|---|---|
| 全身背面，披挂和扣带承重合理。 | `combined-look-back-v001.png` |
| 全身左侧，甲胄层级与正面一致。 | `combined-look-left-profile-v001.png` |
| 全身左前 45°，便于中景身份识别。 | `combined-look-left45-v001.png` |
| G1 轻尘，前军方向远尘只在衣甲外露面少量附着，人物周围空气仍清。 | `state-g1-light-dust-v001.png` |
| 小幅抬手制止旗手后撤；主旗在侧后背景仅作尺寸层级，不遮郭子仪手势。 | `action-center-flag-hold-v001.png` |

## COST-PUGU-001｜仆固怀恩骑装

输入：仆固怀恩脸/身体、`combined-look-front-v001.png`、主坐骑 V2 与静态骑乘接触图。主提示词：`同一仆固怀恩的实用骑乘衣甲，暗色低光泽甲片、灰褐衣层，腰膝可在鞍上弯折；衣摆不过长，不拖入镫和马腹。保持脸、衣甲、带具和坐骑身份；避免夸张异域装饰、披风和现代骑装。灰背景自然光。`

| 本次变化 | 建议文件名 |
|---|---|
| 全身背面，骑装后摆与腰带结构清楚。 | `combined-look-back-v001.png` |
| 全身右侧，膝部、靴和衣摆适合骑姿。 | `combined-look-right-profile-v001.png` |
| 全身左前 45°，锁人物身份和衣甲。 | `combined-look-left45-v001.png` |
| P0 同一主坐骑静态骑姿，近远侧手缰脚镫均有可信接触。 | `mounted-p0-wait-v001.png` |
| P1 转东骑姿，躯干随马转向、外侧膝稳定、衣摆顺重力，装备不改。 | `mounted-p1-turn-v001.png` |
| P2 加速后局部汗尘，沿衣摆、马腹邻近区和带件积累；人物身份不变。 | `mounted-p2-dust-v001.png` |
