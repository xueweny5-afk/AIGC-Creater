# ASSET CONTRACT

## IDENTITY

- **Asset ID：** COST-PUGU-001
- **Type：** COSTUME
- **Working Name：** 仆固怀恩骑乘服装
- **Version：** V1.1
- **Status：** FRONT_BASE_GENERATED
- **Evidence Status：** VISUAL RECONSTRUCTION / RIDING FUNCTION FIRST / CULTURAL REVIEW REQUIRED

## LOCKED FEATURES

- 适合长时间骑乘、快速转向和抬手指挥：袖部、髋部、下摆和靴部不得妨碍动作。
- 与唐军同代军械世界相关联，但通过结构组合、维护方式和回纥骑队装备家族形成合理差异。
- 低饱和灰褐、深铁与少量暗蓝/暗红褐织物；装饰服从结构和身份，不作异域奇观。
- 骑装的最终判断必须和 PROP-HORSE-TACK-001、坐姿及 GROUP-UYGHUR-CAV-001 联合完成。

## REQUIRED VIEWS / STATES

1. 正面、背面、左右侧与 45°。
2. 骑乘坐姿、抬手转向、加速受力。
3. P0 完整；P1 转向；P2 接敌后汗尘。
4. 腰带、下摆、靴、马具接触区细节。

## NEGATIVE CONSTRAINTS

- 无夸张皮草、羽饰、兽牙、纹面、现代民族服装拼贴或幻想游牧甲。
- 无英雄披风、无功能飘带、巨型肩甲、金色奇观装饰。
- 无日本武士甲、蒙古帝国时期模板或晚近清代元素。

## DERIVATION RULE

- 以 CHAR-PUGU-001 身份和体态为父资产；不得以服装遮挡身份漂移。
- 所有状态保留同一扣合、下摆长度、腰带和靴型。
- 汗尘先出现在马腿邻近下摆、靴、坐具接触区和皮革受力点。

## FILES AND REVIEW

- `combined-look-front-v001.png`，1024×1536：骑乘衣甲正面候选。
- **Self-review pass：** 紧凑胸甲、窄袖、髋部开口、骑裤和靴的动作空间成立；无皮草、羽饰或奇观化族群符号。
- **Known risk：** 当前仍是结构重构，文化辨识不足且头盔/甲片偏通用；必须通过坐姿、马具和骑队组合证明功能，不能仅凭单张正面锁定。
- **A027 supplement：** `combined-look-side-left-v001.png`、`combined-look-back-v001.png` 已生成入库；紧凑胸甲、窄袖护腕、短分片甲裙与暗蓝灰下缘延续正面。侧扣、背甲与盔后护片为结构重构候选，不是史实确证；SELF-REVIEWED_CANDIDATE。
- **A028 supplement：** `combined-look-side-right-v001.png` 已归档；身份、紧凑胸甲、短甲裙、护腕与靴型基本连续，SELF-REVIEWED_CANDIDATE。`combined-look-45-left-v001.png` 已恢复输出并留档；头朝左而躯干偏右，HOLD_HEAD_BODY_DIRECTION，不计合格同向45°完成。
- **A030 supplement：** `combined-look-45-right-v001.png`，2026-10-05头身方向修订通过，衣甲/体态基本连续；原A028错误方向版只作历史留档。
- **P0 joint reference / 2026-10-05：** 复用 `assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png`；短甲裙在鞍上分开，骨盆、近侧膝/靴/镫和手缰接触可读，静态左侧服装功能可成立；不证明高速/转向或远侧受力。
- **Remaining：** 抬手/加速、P2 汗尘与双侧/动态马具接触联合验证。P0静态坐姿参考已有，不再重复生成。
- **Decision：** SELF-REVIEWED_CANDIDATE / JOINT RIDING REVIEW REQUIRED。
