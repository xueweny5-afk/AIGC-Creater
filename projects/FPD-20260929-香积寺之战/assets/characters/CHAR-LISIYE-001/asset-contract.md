# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CHAR-LISIYE-001
- **Type：** CHARACTER
- **Working Name：** 李嗣业（非肖像式历史重构）
- **Version：** V1.3
- **Status：** IDENTITY_ANGLES_PARTIAL
- **Purpose：** 为 S004—S005 建立可识别的前军止退者和推进方向；不以个人武力替代军阵。
- **Evidence Status：** HISTORICAL PERSON / APPEARANCE UNKNOWN / NON-PORTRAIT RECONSTRUCTION

## LOCKED FEATURES

- 明显高于普通军士、厚实力量型但不健美化。
- 约 40—50 岁的成熟边军将领视觉带；精确年龄不作史实断言。
- 面部粗粝、疲惫、克制，不使用明星脸或影视角色相似性。
- 行动先于演说；中性身份板不出现咆哮、杀气表演或战斗背景。
- 头发实用收束，发髻低至中位；无武侠长发和日本武士轮廓。
- 正式衣甲、敞开状态和长刀分别由 COST-LISIYE-001 与 PROP-LONGBLADE-001 管理。

## VARIABLE STATES

- L0：完整战斗状态。
- L1：外层衣甲按扣合结构敞开，肩胸汗尘可见。
- L2：推进后的积尘、擦损和疲劳。

## REQUIRED VIEWS

1. `canon-face-front-v001.png`
2. `body-identity-front-v001.png`
3. 左右 45°、左右侧面与身体六视图。
4. L0 / L1 / L2 组合状态。

## NEGATIVE CONSTRAINTS

- 无单人杀穿、飞跃斩杀、夸张怒吼和英雄光。
- 无关刀、幻想巨刃、金色礼仪甲和无结构瞬间脱甲。
- 无白净偶像脸、健美油亮皮肤、显眼传奇伤疤或现代发型。
- 不宣称生成面貌是历史真实肖像。

## DERIVATION RULE

- 先锁定 Canon Face，再派生 Body Identity 和角度。
- 衣甲状态只增加批准服装，不改变脸、体态和身高比例。
- 动作图必须以群体止退和推进为语境，不生成独立英雄海报。

## REVIEW GATE

- 身份必须与 CHR-001 明显可区分，同时属于同一时代和边军世界。
- 高大来自头身和肩背比例，不依靠超现实身高。
- 通过身份、体态和衣甲扣合三项后才可进入场景关键帧。

## FILES AND REVIEW

- `canon-face-front-v001.png`，1312×1199：正面中性身份基准；非肖像式历史重构。
- `body-identity-front-v001.png`，1024×1536：厚实、长期负重可成立的功能性体态；未健美化。
- `body-left45-v001.png`、`body-back-v001.png`、`body-profile-facing-right-v001.png`，各 1024×1536：用户提供的单幅全身角度候选。侧面图按画面朝向命名，避免左右语义混淆。
- `body-right45-v001.png`，1024×1536：用户提供的反向全身 45° 候选；躯干及站姿转向与左前 45°相反，头部仍较正面，不能替代独立头部 45°身份板。
- `reference-contact-sheet-user-v001.png`：多角度参考已入库，上排第二格明确提供面部朝画面左侧的全身侧面。该角度已有设计参考；拼版分辨率限制记录为单幅原图整理事项，不再列为待重新生成。
- `reference-expression-diptych-user-v001.png`：表情比对资料；拼版不等同于独立表情原图。
- **Self-review：** 年龄带、粗粝面部、克制神情与体态区分均通过；与 CHAR-ANXI-001 可清楚区分。
- **Remaining：** 全身角度参考已覆盖；朝左侧面的单幅高分辨率原图尚未独立归档，但不安排重复生图。必要头部角度与 L0/L1/L2 近景身份、衣甲连续性仍需按镜头需求审核；近景身份以 Canon Face 为父资产。
- **Decision：** SELF-REVIEWED_PASS_FOR_DERIVATION；不宣称为历史真实肖像。

## CHANGE LOG

- V1 / 2026-10-01：建立生成合同。
- V1.1 / 2026-10-01：完成 Canon Face 与 Body Identity 正面，自审通过并解除衣甲组合阻断。
- V1.2 / 2026-10-03：入库三张单幅全身角度；两张拼版只留档参考，不计入角度完成数。
- V1.3 / 2026-10-03：入库反向全身 45° 候选；躯干角度可用，头部仍偏正面，后续头部角度单独验证。
- V1.3 intake correction / 2026-10-04：重新核对桌面文件夹，8/8 原图均已归档且哈希一致；确认朝左侧面已包含在多角度拼版中，撤销重复生图要求。
