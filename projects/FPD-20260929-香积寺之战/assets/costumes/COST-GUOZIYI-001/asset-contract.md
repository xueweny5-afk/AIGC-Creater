# ASSET CONTRACT

## IDENTITY

- **Asset ID：** COST-GUOZIYI-001
- **Type：** COSTUME
- **Working Name：** 郭子仪中军指挥衣甲
- **Version：** V1.2
- **Status：** FRONT_BACK_SIDE_GENERATED
- **Evidence Status：** RESEARCH-INFERRED / APPEARANCE OPEN / NON-PORTRAIT RECONSTRUCTION

## LOCKED FEATURES

- 与唐军前军属于同一时代军械世界，工艺、完整度和维护度略高，但仍是正在使用的战地装备。
- 指挥层级通过合身度、结构完整、有限暗红褐织物和随员/旗号关系表达，不使用帝王或礼仪符号。
- 肩臂可完成观察、转身、抬手制止和接收回报动作。
- 金属低光泽，只有受磨边缘产生窄高光；轻尘不遮挡身份和结构。

## REQUIRED VIEWS / STATES

1. 正面、背面、左右侧与 45°。
2. G0 完整使用；G1 前景轻尘。
3. 头部防护、扣带、工艺与手部细节。
4. 与中军旗并置的层级测试。

## NEGATIVE CONSTRAINTS

- 无金甲、明光镜面、龙纹、王冠、披风、礼仪袍和帝王配色。
- 无日本武士轮廓、明代模板、欧洲板甲、幻想肩甲。
- 无全新影楼服装、塑料表面或过量金属装饰。

## DERIVATION RULE

- 以 CHAR-GUOZIYI-001 身份和体态为父资产。
- G1 只增加有来源的轻尘和使用痕迹，不改变甲型、颜色或扣带。
- 旗号属于 PROP-FLAGS-001，服装本身不绘制未经研究的军旗图案。

## FILES AND REVIEW

- `combined-look-front-v001.png`，1024×1536：中军完整衣甲正面候选。
- `combined-look-back-v001.png`、`combined-look-side-right-v001.png`：同衣甲的背面、朝画面右侧面候选；暗铁甲片、暗红褐窄边、腰甲及绑腿延续正面。背面连接为结构重构，细节仍待联合审核。
- `../../characters/CHAR-GUOZIYI-001/action-g0-raise-hand-v001.png`：交叉引用角色抬手图，肩甲随上臂抬升、袖层压缩可读；不复制存储。
- **Self-review pass：** 身份连续、维护度高于普通军士、暗红褐只作有限结构边缘、无金甲和帝王符号。
- **Known risk：** 护肩、盔侧护片和密集系带仍有泛东亚/武士甲误读风险；后续侧背派生必须进一步压低肩甲外扩与装饰性系绳。
- **A021/A022 supplement：** `state-g1-light-dust-v001.png`、`combined-look-side-left-v001.png`、`combined-look-45-right-v001.png` 已入库。45°衣甲与腰带侧别基本连续；朝左侧面整体结构可读，但腰带尾位置偏向前侧，标为 HOLD_SASH_POSITION，不升级为身份基准。G1为轻尘表面候选。
- **A023 supplement：** `combined-look-side-left-v002.png` 将腰带结与尾移回侧腰/外侧大腿，局部修订自审通过，后续侧面使用V2，V1保留历史。`detail-protection-fastening-v001.png` 提供头盔、肩胸连接、腰带与腕部细节；结构为重构候选，手指有遮挡，不作完整五指验收证据。
- **A024 hierarchy test：** `test-command-flag-hierarchy-v001.png`：人物与较大无补缀中军旗同框；面部、抬手与旗布互不遮挡，暗铁衣甲和暗红旗号区分可读。木底座仅为灰背景展示支持，不是战场道具，不用于证明旗手持旗或F2战场稳定状态。SELF-REVIEWED_PASS_FOR_HIERARCHY。
- **Remaining：** 已有正背侧、45°、细节与抬手/轻尘图仍需联合审核。手部五指可读性沿用角色G0抬手图，不由遮挡细节板证明；展示底座禁止带入战场派生。
- **Decision：** SELF-REVIEWED_CANDIDATE；非确证甲型。

## CHANGE LOG

- V1.2 / 2026-10-04：补背面与侧面，角色目录的抬手状态交叉引用为服装活动性候选证据。
