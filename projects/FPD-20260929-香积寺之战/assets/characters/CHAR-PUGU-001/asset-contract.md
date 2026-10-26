# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CHAR-PUGU-001
- **Type：** CHARACTER
- **Working Name：** 仆固怀恩（非肖像式历史重构）
- **Version：** V1.1
- **Status：** IDENTITY_BASE_GENERATED
- **Purpose：** 以观察尘线、抬手转向和率回纥骑兵接敌表现东翼反伏击行动。
- **Evidence Status：** HISTORICAL PERSON / RESEARCHED FUNCTION / APPEARANCE UNKNOWN / NON-PORTRAIT RECONSTRUCTION

## LOCKED FEATURES

- 成熟的边地骑将，精干、重心稳定，适合长期骑乘；不做孤骑英雄或野蛮化形象。
- 面貌是个体化非肖像重构，不用夸张族群特征承担识别。
- 身份来自骑乘姿态、指挥响应和与回纥骑兵的组织关系，而不是皮草、羽毛或异域奇观装饰。
- Canon Face 使用实用收束发式、自然肤质和中性内层衣物；具体骑装由 COST-PUGU-001 管理。

## VARIABLE STATES

- P0：接敌前观察尘线。
- P1：抬手转向，骑队同步响应。
- P2：接敌后，马匹和下摆出现汗尘。

## REQUIRED VIEWS

1. Canon Face 正面。
2. Body Identity 正面与骑乘比例。
3. 左右 45°、左右侧面和身体六视图。
4. 观察、抬手、骑乘迎敌三个状态。

## NEGATIVE CONSTRAINTS

- 无“蛮族”脸谱、夸张皮草、兽牙、羽饰、纹面、重型胡须奇观或现代民族服装拼贴。
- 无孤骑冲阵、英雄披风、健美体态和幻想骑装。
- 无明星脸、影视角色复刻或把生成面貌宣称为真实肖像。

## DERIVATION RULE

- 先锁定 Canon Face 与 Body Identity，再联合 COST-PUGU-001、PROP-HORSE-TACK-001 和主坐骑派生骑乘状态。
- 骑乘状态只改变姿态、服装受力、汗尘与视线，不改变身份或马具系统。
- 群体资产通过装备家族与指挥响应建立关系，不复制仆固怀恩的脸。

## REVIEW GATE

- 文化表达必须克制、个体化且不异域奇观化。
- 身体比例、髋膝角度和手—缰接触必须支持真实骑乘。
- 与服装、马具和回纥骑兵群体联合审核通过后才进入场景关键帧。

## FILES AND REVIEW

- `canon-face-front-v001.png`，1312×1199：成熟骑将的中性身份母图。
- `body-identity-front-v001.png`，1024×1536：紧凑耐久、下肢稳定的正面体态基准。
- **Self-review pass：** 个体面貌、骑将警觉性和非健美体态成立；无皮草、羽饰、纹面或“蛮族”奇观化符号。
- **Known risk：** 当前身份图故意不依赖族群脸谱，正式文化辨识必须由经研究的骑装、马具和组织关系补充；不得以面部推断族属。
- **A025 supplement：** `body-profile-facing-right-v001.png`、`body-back-v001.png`：朝右侧面和正背面全身候选已入库；发髻、短须、紧凑体态、灰褐衣层、短腰带尾和绑腿基本连续。背面不证明面部身份，仅补体态与衣物背面参考。
- **A026 supplement：** `body-profile-facing-left-v001.png`、`body-45-facing-left-v001.png`、`body-45-facing-right-v001.png` 已入库；头身方向一致，短须、体态、衣长和腰带基本连续。六个身体方向均有独立候选，不等同于头部近景或骑乘验收。
- **P0 joint reference / 2026-10-05：** `assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png` 已有同身份静态骑乘，可复用为P0观察母态。骨盆位于鞍桥之间、左侧脚镫与手缰接触可读；只证明静态左侧组合，不能证明双侧脚镫、转向或加速。图片主要归于马具接触，不复制。
- **Remaining：** 必要头部角度、P1/P2动作状态与正式骑装/马具动态联合审核；P0静态左侧比例已有证据，不重复生成。
- **Decision：** SELF-REVIEWED_PASS_FOR_DERIVATION；需等待骑乘组合联合审核。

## CHANGE LOG

- V1 / 2026-10-01：建立非肖像式重构合同。
- V1.1 / 2026-10-01：完成 Canon Face 与 Body Identity 正面。
