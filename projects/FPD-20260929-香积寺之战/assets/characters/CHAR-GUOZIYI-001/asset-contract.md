# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CHAR-GUOZIYI-001
- **Type：** CHARACTER
- **Working Name：** 郭子仪（非肖像式历史重构）
- **Version：** V1.2
- **Status：** BODY_ANGLES_AND_G0_DERIVING
- **Purpose：** 以稳定的中军观察与调度状态证明整体指挥仍在运转，不承担全知统帅神化。
- **Evidence Status：** HISTORICAL PERSON / RESEARCHED FUNCTION / APPEARANCE UNKNOWN / NON-PORTRAIT RECONSTRUCTION

## LOCKED FEATURES

- 成熟至年长的职业将领视觉带，体态稳定、负重和久战可成立；具体年龄外观不作史实肖像断言。
- 神情沉着、读取战场信息，不表现帝王威仪或神机妙算。
- 身份来自中军位置、传令与装备维护度，而不是金色、龙纹、王冠或礼仪华服。
- 中性身份图只穿低装饰内层衣物，不持兵器，不出现旗号或战场。

## VARIABLE STATES

- G0：中军稳定，站立观察。
- G1：背景轻尘，抬手制止或维持旗号方向。

## REQUIRED VIEWS

1. Canon Face 正面。
2. Body Identity 正面。
3. 左右 45°、左右侧面和身体六视图。
4. 站立观察与抬手制止两个动作状态。

## NEGATIVE CONSTRAINTS

- 无帝王脸谱、金冠、龙纹、金甲、白发神仙、长须飘逸和高台演说。
- 无明星脸、影视郭子仪角色复刻、过度磨皮或传奇伤疤。
- 无战场烟尘、盔甲、旗号或戏剧光进入 Canon Face。

## DERIVATION RULE

- 先锁定 Canon Face，再派生 Body Identity 和角度。
- 衣甲由 COST-GUOZIYI-001 管理，不用服装细节掩盖身份漂移。
- 所有场景状态保留同一面孔、体态和手部身份。

## REVIEW GATE

- 必须与李嗣业的厚重前军体态、仆固怀恩的骑将轮廓和无名军士清楚区分。
- 成熟和权威来自姿态与注意力，不来自华丽符号。
- 通过身份、体态和中军服装层级后才进入场景关键帧。

## FILES AND REVIEW

- `canon-face-front-v001.png`，1312×1199：成熟至年长将领的中性身份母图。
- `body-identity-front-v001.png`，1024×1536：稳定、耐久而不健美化的正面体态基准。
- `body-profile-facing-right-v001.png`、`body-back-v001.png`、`body-45-facing-left-v001.png`：独立全身角度，非镜像；年龄、须发、棕褐衣层与体态基本连续，SELF-REVIEWED_CANDIDATE。袖口内层可见范围有轻微差异，近景继续以母图为准。
- `action-g0-raise-hand-v001.png`：完整披甲的小幅抬右手制止状态；五指、肘弯和肩甲抬升可读，身体稳定。主要用途为表演状态，衣甲用途由 COST-GUOZIYI-001 交叉引用，不复制图片。
- **Self-review pass：** 自然年龄、沉着观察感、低装饰内层与普通军士/李嗣业的区分成立；未使用帝王、金色或白发神仙模板。
- **Known risk：** 发髻与交领衣物仍属通用重构，不得被当作郭子仪真实肖像或确证服饰。
- **Supplement A021：** `body-profile-facing-left-v001.png` 与 `body-45-facing-right-v001.png` 已生成入库，全身六个方向现有独立候选；G1全身轻尘引用 `assets/costumes/COST-GUOZIYI-001/state-g1-light-dust-v001.png`，不复制归档。
- **Remaining：** 必要头部角度、G0/G1 与正式中军衣甲联合审核。袖口内层暴露有轻微差异，近景以母图为准；G1全身图不能代替独立头部表情板。静止观察母态复用披甲正面。
- **Decision：** SELF-REVIEWED_PASS_FOR_DERIVATION。

## CHANGE LOG

- V1 / 2026-10-01：建立非肖像式重构合同。
- V1.1 / 2026-10-01：完成 Canon Face 与 Body Identity 正面。
- V1.2 / 2026-10-04：生成三张独立身体角度与一张 G0 抬手状态，候选入库；未宣称六视图或角色全状态已完成。
