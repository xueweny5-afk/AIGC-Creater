# ASSET CONTRACT

## IDENTITY

- **Asset ID：** CHR-002
- **Type：** CHARACTER
- **Working Name：** 陶渊明身份资产
- **Version：** v2.4
- **Status：** APPROVED
- **Purpose：** 稳定陶渊明在彭泽任职、离任和归家三种状态，避免“县令”和“隐士”被设计成两个人。
- **Source Visual Bible Version：** `visual-development/world-visual-bible.md` v1
- **Evidence Status：** DOCUMENTED APPROXIMATE LIFE STAGE + CREATIVE APPEARANCE + RESEARCH-INFERRED COSTUME

## LOCKED FEATURES

- 中国东晋末期士人、彭泽令与归田者的同一身份；不是脱离生计的仙人。
- 剧情发生于约四十岁的人生阶段，呈现成熟成年人而非白发高龄隐士。
- 基础面貌原创、非特定真人；不复制后世陶渊明画像中的固定脸谱。
- 三种状态保持相同骨相、眉眼比例、鼻口关系、耳形、发际线和惯用手。
- 体态具长期读写和现实劳顿感，但不因清贫而被设计成病弱、污损或佝偻。
- 行为印象是克制、清楚、完成手中事务后离开；不锁定为永远微笑或超然闭目。

## VARIABLE STATES

- **State A｜彭泽令：** 官职所需衣层完整、整洁而不过度华贵；可有久坐工作造成的自然衣褶。
- **State B｜离任行旅：** 减少制度性外层，加入行旅折痕和少量尘土；仍保持个人整洁。
- **State C｜归家生活：** 日常衣层、重复使用痕迹和劳动适配性增强；不得演变成乞丐化或仙风道骨化。
- 胡须、细纹、体型和肤色可在候选阶段比较，主参考批准后锁定。

## PRESENTATION CHOICES

- 中性身份参考采用自然站立、低表情、无遮挡和无情境装饰的干净呈现。
- 暂按写实历史电影质感表现四十岁左右的真实皮肤、手部与织物，不做古装偶像式磨皮。
- 状态差异优先由服装层级、行囊和使用痕迹表达，不用强烈明暗或诗意植物替代身份设计。

## UNKNOWN / OPEN FIELDS

- 可靠体貌、身高、体型、脸型、胡须长度和发式细节。
- 彭泽令服饰制度、日常衣层、颜色、腰间制度物、鞋履和行囊形制。
- 归家状态是否需要固定劳动配件；当前剧本没有要求，应默认不增加。
- 用户是否确认写实历史电影质感作为实际生成媒介。

## REQUIRED VIEWS / PLATES

1. **Base Identity Plate：** 正、侧、背三向，同一基础衣层和自然站姿。
2. **Face Identity Plate：** 正面与四分之三面部，低表情，检查年龄与骨相。
3. **State Comparison Plate：** 彭泽令、离任行旅、归家生活三状态，面貌和体态保持一致。
4. **Hand / Use Note：** 正常手部比例与持文书、提行囊所需的基础可用性，不单独生成动作场面。

## NEGATIVE CONSTRAINTS

- 不使用特定演员、网红或现有影视陶渊明形象。
- 不把人物做成白发长须老人、仙人、醉汉、乞者或不食人间烟火的隐士。
- 不将菊花、酒壶、锄头、松树直接固定在中性身份图上。
- 不使用唐宋明清官服、戏服式宽袍、奢华纹样或无依据冠帽。
- 不通过脏脸、破洞、过度消瘦或金色怀旧滤镜表现清贫。
- 不出现文字、水印、品牌或复杂背景。

## FILES AND PATHS

- **Contract：** `assets/characters/CHR-002/asset-contract.md`
- **Generated Images：** `assets/characters/CHR-002/tao-yuanming-identity-candidate-v1.png`（REJECTED FOR DOWNSTREAM）；`assets/characters/CHR-002/tao-yuanming-identity-candidate-v2.png`（APPROVED IDENTITY）；`assets/characters/CHR-002/tao-yuanming-turnaround-v1.png`（APPROVED TURNAROUND）；`assets/characters/CHR-002/tao-yuanming-state-comparison-v1.png`（STATE CANDIDATE）
- **Primary Reference：** `tao-yuanming-identity-candidate-v2.png` / USER-APPROVED IDENTITY

## REVIEW RESULTS

- **Review Evidence：** USER-APPROVED（identity + turnaround + states）
- **Files Inspected：** `tao-yuanming-identity-candidate-v1.png`, `tao-yuanming-identity-candidate-v2.png`, `tao-yuanming-turnaround-v1.png`
- **Passed：** 三视图保持长窄高额脸、长鼻线、清瘦高挑体态和稀疏颏须；正侧背比例一致；无官阶物、标签道具或华贵装饰，宽衫与素色织物形成清楚的归田士人轮廓。
- **Failed：** 头巾仍属于低巾式视觉候选，具体包裹方法不能宣称精确复原；三视图尚未由用户复核。
- **Decision：** 面貌、年龄带、体态、三视图和彭泽令/离任/归家状态批准用于 Scene Design；巾式与服制继续保留研究推定标记。

## DOWNSTREAM USE

- 主参考用于彭泽县衙、归家和后续跨状态人物连续性。
- State A/B/C 必须从同一基础身份派生；植物、孩子和家门属于场景资产，不进入人物身份。
- CHR-002 与 CST-002 未有实际图像并通过审核前，不得用于 Scene Design。

## CHANGE LOG

- **v1｜2026-09-21：** 建立约四十岁身份范围、三状态与反隐士脸谱规则；未生成图片。
- **v1.1｜2026-09-21：** 生成并自审首张正面全身身份候选；保存至项目，等待用户确认。
- **v1.2｜2026-09-21：** 用户审核判定与张翰候选相似、服饰时代特征不足；状态改为 REWORK，v1 保留但不再用于下游。
- **v2｜2026-09-21：** 按长窄高额脸、清瘦体态与东晋归家幅巾宽衫方向重做；辨识度自审通过，面貌待用户确认，服装结构待考据。
- **v2.1｜2026-09-22：** 用户接受 v2 人物方向；锁定面貌、年龄带和体态，服装及侧背仍待完成。
- **v2.2｜2026-09-22：** 从批准主参考派生正、左侧、背面三视图；同脸与体态自审通过，巾式保持研究推定，等待用户复核。
- **v2.3｜2026-09-22：** 用户接受三视图；生成彭泽令、离任、归家三状态板，同脸与体态自审通过，状态差异等待用户复核。
- **v2.4｜2026-09-22：** 用户接受状态板；人物资产升级为 APPROVED，可进入 Scene Design，历史服制精确度不随视觉批准而升级。
