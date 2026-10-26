# ASSET GENERATION LOG

## HANDOFF-USER-ASSETS-V2｜2026-10-05（非生成记录）

- 用户最新要求：报告完成情况并整理剩余提示词，由用户操作生成；停止提交新的图片/视频任务。本次新增媒体：0。
- 完成目录核对：108张PNG为总存档（含旧版、拼版、失败图）；19类仍有派生或审核缺口，不将总文件数当合格数。
- 交接：`assets/prompts/USER-HANDOFF-20261005/index.md`及六册102张卡，其中95张待生成/返工、7张条件/版式。确切现有参考均已存在；未来参考明确指向前置卡，目标均为未占用文件名。
- 进度回执：`assets/asset-status-20261005.md`；asset-completion-plan更新为V1.4，project-brief分别记录资产/分镜/视频执行方式。
- 本记录仅证明提示词编译与接手，不证明已生成、已验收或全片G3通过；目标图片仍需用户真实回传。

## GENERATION-A031-PUGU-STATE-ATTEMPTS｜2026-10-05

- P1抬手信号准备：两次内置生图均connection failed，无生成结果、无运行句柄；不计已生成，不创建虚构图片路径。不自动切换需要额外授权的CLI/API。
- 提示词 `assets/prompts/BATCH-A031-prompt-package.md` 已保存。P1只是信号准备，仍需群体响应和转向关系，不能以单人抬手冒充骑队转向完成。
- 已重新检查并交叉登记P0母态 `props/PROP-HORSE-TACK-001/rider-contact-left-v001.png`：角色骑乘比例、服装坐姿与近侧接触有静态证据，图片无需复制或再生成；双侧和动态未证明。

## GENERATION-A030-PUGU-DIRECTION-REPAIR｜2026-10-05

- `costumes/COST-PUGU-001/combined-look-45-right-v001.png`：仅针对A028错误方向校准头部/头盔，头身均朝右；衣甲、手位、站姿和灰背景基本保持，SELF-REVIEWED_PASS_FOR_DIRECTION。不能由此推出骑乘联合审核通过。
- 复制SHA256一致；原件及旧方向版保留。精确提示词 `assets/prompts/BATCH-A030-prompt-package.md`。

## GENERATION-A029-B0-RETRY-AND-REVIEW｜2026-10-04

- 原句柄81失效且无输出后重试；新增 `locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v001.png` 至 `state-b0-prebattle-v003.png`，三份复制SHA256一致，原件保留。
- V1改变天光并要求稀疏旧痕；出现过密重复卷曲纹理。V2仅要求移除纹理，失败。V3从原拓扑仅修改天光，重复纹理仍出现。三版均HOLD_GROUND_TEXTURE，未计合格B0。
- 精确提示词 `assets/prompts/BATCH-A029-prompt-package.md`；宏观锚点连续不支持地表状态全项通过。停止同问题无界重试，继续其他缺失资产。

## A028/A029 RECOVERY AUDIT｜2026-10-04

- 运行句柄73和81均返回not found；不是观察超时，已失去可续等句柄。
- 在默认输出目录找到 `exec-bf4ae843-c909-43b5-93e3-22e31c93ab90.png`，对应骑装45°外观。归档 `costumes/COST-PUGU-001/combined-look-45-left-v001.png`，复制SHA256一致；头身方向不一致，HOLD_HEAD_BODY_DIRECTION，未放行。
- 未找到B0地形输出；旧任务不再被记录为实时运行。允许重新提交此缺失项，不以旧状态说明代替结果。

## GENERATION-A028-PUGU-COSTUME-SUPPLEMENT｜2026-10-04

- `costumes/COST-PUGU-001/combined-look-side-right-v001.png`：已归档SHA256校验一致，SELF-REVIEWED_CANDIDATE；原件保留。
- 朝左45°提交后仍在运行（functions.exec cell 73），尚无完成结果，不计入资产数量，不重启任务。
- 提示词 `assets/prompts/BATCH-A028-prompt-package.md`；全资产目标仍在推进。

## GENERATION-A027-PUGU-COSTUME-ANGLES｜2026-10-04

- 新增 `costumes/COST-PUGU-001/combined-look-side-left-v001.png` 与 `costumes/COST-PUGU-001/combined-look-back-v001.png`。
- 衣甲家族、短甲裙/暗蓝灰下缘、护腕及绑腿基本连续；侧扣、背甲与盔后护片属于重构，SELF-REVIEWED_CANDIDATE，不宣称史实确证或骑乘验证通过。
- 两图原件保留，复制SHA256一致；精确提示词 `assets/prompts/BATCH-A027-prompt-package.md`。

## GENERATION-A026-PUGU-BODY-SIX-VIEWS｜2026-10-04

- 新增 `characters/CHAR-PUGU-001/body-profile-facing-left-v001.png`、`body-45-facing-left-v001.png`、`body-45-facing-right-v001.png`。
- 三图为独立角度候选，非镜像复制；头身转向一致，短须/灰褐衣层/短腰带尾/绑腿基本连续。SELF-REVIEWED_CANDIDATE，骑乘和必要头部视角未通过。
- 原件保留，三张归档复制SHA256一致；精确提示词 `assets/prompts/BATCH-A026-prompt-package.md`。

## GENERATION-A025-PUGU-BODY-ANGLES｜2026-10-04

- `characters/CHAR-PUGU-001/body-profile-facing-right-v001.png`：纯侧面方向可读，短须/发髻/体态与内层衣物基本连续，SELF-REVIEWED_CANDIDATE。
- `characters/CHAR-PUGU-001/body-back-v001.png`：正背体态、衣长和绑腿连续，SELF-REVIEWED_CANDIDATE；不用于面部身份审核。
- 两图原件保留，复制SHA256一致。提示词 `assets/prompts/BATCH-A025-prompt-package.md`。骑乘状态与其余角度未完成。

## GENERATION-A024-COMMAND-HIERARCHY｜2026-10-04

- `costumes/COST-GUOZIYI-001/test-command-flag-hierarchy-v001.png`：人物/衣甲/中军旗同框层级参考。面部及五指动作无遮挡，中军旗尺寸和无补缀识别可读；自审层级通过。
- 木底座仅为展示支撑，不纳入战场资产；本图不验证旗手受力、旗区密度或F2中军战场状态。
- 复制SHA256校验一致，原文件保留；精确提示词 `assets/prompts/BATCH-A024-prompt-package.md`。全资产目标仍未完成。

## GENERATION-A023-GUOZIYI-LOCAL-REPAIR｜2026-10-04

- `costumes/COST-GUOZIYI-001/combined-look-side-left-v002.png`：仅针对侧腰带位置修订；腰结移回侧腰，尾垂于外侧大腿，局部自审通过，V1留档。
- `costumes/COST-GUOZIYI-001/detail-protection-fastening-v001.png`：四格头盔/肩扣/腰带/手腕候选；可读材料和连接家族。手指遮挡，不作完整五指证据，也不是考古确证。
- 两图复制SHA256校验一致，原件保留；精确提示词见 `assets/prompts/BATCH-A023-prompt-package.md`。中军旗测试及联合审核未完成。

## GENERATION-A022-GUOZIYI-COSTUME-ANGLES｜2026-10-04

- `costumes/COST-GUOZIYI-001/combined-look-side-left-v001.png`：朝左纯侧面，身份和甲片家族基本连续；腰带尾偏前，HOLD_SASH_POSITION，后续只校准此处。
- `costumes/COST-GUOZIYI-001/combined-look-45-right-v001.png`：朝右45°全身，腰带侧别、甲裙和头盔基本连续，SELF-REVIEWED_CANDIDATE。
- 两张原件保留，归档复制SHA256一致。精确提示词 `assets/prompts/BATCH-A022-prompt-package.md`。未生成视频、未放行资产阶段。

## GENERATION-A021-GUOZIYI-SUPPLEMENT｜2026-10-04

- `characters/CHAR-GUOZIYI-001/body-profile-facing-left-v001.png`：新增全身朝左侧面，身份和衣层基本连续；袖口内层暴露范围有轻微差异，候选。
- `characters/CHAR-GUOZIYI-001/body-45-facing-right-v001.png`：新增反向45°，头身朝向一致，候选。
- `costumes/COST-GUOZIYI-001/state-g1-light-dust-v001.png`：此前生成的G1完成检查归档，姿态和甲胄连续，尘土以靴尖、下摆及甲缝为主；角色状态交叉引用，不复制。
- 三张均验证复制前后SHA256一致；原文件保留。提示词见 `assets/prompts/BATCH-A021-prompt-package.md`。本批不含视频，不代表资产阶段全部通过。

## BATCH-A001-FOUNDATION｜2026-10-01

- **Source：** USER_GENERATE；用户上传四张图片。
- **Review Method：** 原始像素人工视觉审核，依据 Asset Contract V1/V1.1。
- **Batch Result：** 1 项技术通过待用户锁定；3 项 REWORK；0 项最终 APPROVED。

| Unit | Asset ID | Archived File | Dimensions | Review Evidence | Result | Summary |
|---|---|---|---|---|---|---|
| A001-01 | LOC-BATTLEFIELD-001 | `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v001.png` | 1672×941 | SELF-REVIEWED | REWORK | 开阔尺度可用，但属于斜向航拍环境概念，七区拓扑、方位和时代车辆不够可靠 |
| A001-02 | MAT-BATTLEFIELD-001 | `assets/locations/MAT-BATTLEFIELD-001/material-ground-v001.png` | 1672×941 | SELF-REVIEWED | REWORK | 前两栏可用；第三栏为偶蹄印，第四栏不足以表达战后沉降 |
| A001-03 | PROP-LONGBLADE-001 | `assets/props/PROP-LONGBLADE-001/candidate-comparison-v001.png` | 1672×941 | SELF-REVIEWED | REWORK | 三候选几乎同形且关刀化，不得进入下游 |
| A001-04 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/canon-face-front-v001.png` | 1536×1024 | SELF-REVIEWED | GENERATED_PENDING_REVIEW | 身份、年龄、肤质与中性资产条件通过；发髻和神情待用户确认 |

## NEXT ACTION

先由用户决定是否接受 CHAR-ANXI-001 Canon Face。若接受，锁定为人物身份母图并只派生头部角度；其余三项按合同失败字段定点返工，不使用当前图作为批准父资产。

## BATCH-A001-REWORK｜2026-10-01

- **Source：** AI_EDIT；以归档 V1 为编辑母图，按失败字段定点返工，V1 全部保留。
- **Prompt Package：** `assets/prompts/BATCH-A001-rework/prompt-package.md`
- **Review Method：** 原始像素人工视觉审核；不因生成成功自动升级为最终 APPROVED。
- **Batch Result：** 4 项完成结构性修正；2 项等待用户锁定，2 项仍需下游验证板。

| Unit | Asset ID | Edited File | Dimensions | Review Evidence | Result | Summary |
|---|---|---|---|---|---|---|
| A001-R01 | LOC-BATTLEFIELD-001 | `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png` | 1672×941 | SELF-REVIEWED | GENERATED_PENDING_REVIEW | 中央主战轴与东侧机动通道清楚，现代拖车感与随机杂物显著减少；仍需七区覆盖图锁定空间语义 |
| A001-R02 | MAT-BATTLEFIELD-001 | `assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png` | 1672×941 | SELF-REVIEWED | GROUND_PLATE_PASS | 偶蹄印已改为单蹄马印，前两栏材料语言保留；第四栏仅作为扰动地表参考，不作精确考古复原 |
| A001-R03 | PROP-LONGBLADE-001 | `assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png` | 1672×941 | SELF-REVIEWED | CANDIDATE_SELECTION_PENDING | 关刀化已消除，三候选刃宽、长度和重心拉开；推荐 B 型进入双手持握验证 |
| A001-R04 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/canon-face-front-v002.png` | 1536×1024 | SELF-REVIEWED | GENERATED_PENDING_REVIEW | 保持同一身份，收紧散发并缓和表情；等待用户锁定为 Canon Face |

## CURRENT NEXT ACTION

锁定 CHAR-ANXI-001 V2 与 PROP-LONGBLADE-001 候选后，优先制作人物头部角度、Body Identity、长刀双手持握验证和 LOC-BATTLEFIELD-001 七区覆盖图。

## BATCH-A002-PROP-VALIDATION｜2026-10-01

- **Decision：** 用户接受 CHAR-ANXI-001 V2，并同意按推荐推进 PROP-LONGBLADE-001 B 型。
- **Source：** AI_GENERATE_WITH_REFERENCE；结构参考为 `candidate-comparison-v002.png`。
- **Prompt Package：** `assets/prompts/BATCH-A002-prop-validation/prompt-package.md`
- **Batch Result：** Canon Face V2 APPROVED；长刀 B 型单人持握与三人列阵间距通过，进入结构细化阶段。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A002-01 | PROP-LONGBLADE-001 | `assets/props/PROP-LONGBLADE-001/human-scale-hold-b-v001.png` | 1672×941 | SELF-REVIEWED_PASS | 两手间距、人体重心、全长和回收空间可解释；动作图不替代结构母图 |
| A002-02 | PROP-LONGBLADE-001 | `assets/props/PROP-LONGBLADE-001/formation-spacing-b-v001.png` | 1672×941 | SELF-REVIEWED_PASS | 三人同列可维持平行刀向和可用横向间距，无兵器相交 |

## CURRENT NEXT ACTION V2

从已批准 Canon Face V2 派生左右 45°/侧面与 Body Identity；同时为战场拓扑 V2 制作 A—G 七区覆盖图。长刀后续结构图必须回看候选板 B 型，避免沿用动作验证图的轻微刀尖弧度漂移。

## BATCH-A003-IDENTITY-TOPOLOGY｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE + DETERMINISTIC_SVG_OVERLAY。
- **Prompt Package：** `assets/prompts/BATCH-A003-identity-topology/prompt-package.md`
- **Batch Result：** 主角左前 45°与 Body Identity 正面通过自审；战场 A—G 制作覆盖图完成并可编辑。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A003-01 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/head-left45-v001.png` | 1536×1024 | SELF-REVIEWED_PASS | 五官、耳形和肤质连续；发髻体积略增，已加入后续限制 |
| A003-02 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/body-identity-front-v001.png` | 1024×1536 | SELF-REVIEWED_PASS | 耐力型体态、完整手脚与基础衣层成立；Canon Face 仍为近景身份最高优先级 |
| A003-03 | LOC-BATTLEFIELD-001 | `assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.svg` | 1672×941 viewBox | SELF-REVIEWED_PASS | 可编辑 A—G 七区、方向与动线覆盖图 |
| A003-04 | LOC-BATTLEFIELD-001 | `assets/locations/LOC-BATTLEFIELD-001/topology-zones-v001.png` | 1672×941 | SELF-REVIEWED_PASS | 覆盖图渲染预览，文字与区域可读 |

## CURRENT NEXT ACTION V3

补齐主角左侧、右侧和右前 45°头部角度，再以批准 Body Identity 为父资产制作身体侧面/背面；并建立 COST-ANXI-FRONT-001 基础服装与甲胄合同。

## BATCH-A004-CHARACTER-COSTUME｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE；人物角度以批准身份图派生，服装状态以既有身份和基础衣甲约束生成。
- **Prompt Package：** `assets/prompts/BATCH-A004-character-costume/prompt-package.md`
- **Batch Result：** 主角头部五视图补齐；李嗣业身份母资产与 L0/L1 正面建立；前军基础衣甲正背面建立。均为资产阶段候选，未进入分镜。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A004-01 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/head-left-profile-v001.png` | 1536×1024 | SELF-REVIEWED_PASS | 左侧身份、耳形和发髻连续 |
| A004-02 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/head-right-profile-v001.png` | 1536×1024 | SELF-REVIEWED_PASS | 右侧独立派生，未镜像替代 |
| A004-03 | CHAR-ANXI-001 | `assets/characters/CHAR-ANXI-001/head-right45-v001.png` | 1536×1024 | SELF-REVIEWED_PASS | 五官比例和年龄连续 |
| A004-04 | CHAR-LISIYE-001 | `assets/characters/CHAR-LISIYE-001/canon-face-front-v001.png` | 1312×1199 | SELF-REVIEWED_PASS_FOR_DERIVATION | 非肖像式历史重构，成熟边军将领身份成立 |
| A004-05 | CHAR-LISIYE-001 | `assets/characters/CHAR-LISIYE-001/body-identity-front-v001.png` | 1024×1536 | SELF-REVIEWED_PASS_FOR_DERIVATION | 厚实功能体态成立，避免健美化 |
| A004-06 | COST-ANXI-FRONT-001 | `assets/costumes/COST-ANXI-FRONT-001/combined-look-front-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 正面基础衣甲与固定肩部补丁成立 |
| A004-07 | COST-ANXI-FRONT-001 | `assets/costumes/COST-ANXI-FRONT-001/combined-look-back-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 背面扣合与层次成立 |
| A004-08 | COST-LISIYE-001 | `assets/costumes/COST-LISIYE-001/state-l0-complete-front-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 完整披甲状态成立 |
| A004-09 | COST-LISIYE-001 | `assets/costumes/COST-LISIYE-001/state-l1-open-front-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 解甲后状态保持体脂和装备受力逻辑，不作健美英雄展示 |

## CURRENT NEXT ACTION V4

资产库优先：建立 CHAR-GUOZIYI-001 与 CHAR-PUGU-001 的非肖像式身份母资产；随后补齐服装、骑乘、群体、旗号、连续性道具、材质和空气状态。导演方案、分镜与视频提示词保持冻结，直至资产完成表通过。

## BATCH-A005-HISTORICAL-IDENTITIES｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE；两位历史人物均按“史实职能可靠、具体面貌未知”的非肖像式重构执行。
- **Prompt Package：** `assets/prompts/BATCH-A005-historical-identities/prompt-package.md`
- **Batch Result：** 郭子仪与仆固怀恩均建立 Canon Face 与 Body Identity 正面；可继续派生，但不作为真实肖像或确证族群外貌。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A005-01 | CHAR-GUOZIYI-001 | `assets/characters/CHAR-GUOZIYI-001/canon-face-front-v001.png` | 1312×1199 | SELF-REVIEWED_PASS_FOR_DERIVATION | 成熟中军将领身份成立，无帝王化和白发神仙模板 |
| A005-02 | CHAR-GUOZIYI-001 | `assets/characters/CHAR-GUOZIYI-001/body-identity-front-v001.png` | 1024×1536 | SELF-REVIEWED_PASS_FOR_DERIVATION | 稳定耐久体态与低装饰内层成立 |
| A005-03 | CHAR-PUGU-001 | `assets/characters/CHAR-PUGU-001/canon-face-front-v001.png` | 1312×1199 | SELF-REVIEWED_PASS_FOR_DERIVATION | 成熟骑将身份成立，不以族群脸谱奇观化 |
| A005-04 | CHAR-PUGU-001 | `assets/characters/CHAR-PUGU-001/body-identity-front-v001.png` | 1024×1536 | SELF-REVIEWED_PASS_FOR_DERIVATION | 紧凑耐久体态成立，骑乘组合仍待验证 |

## CURRENT NEXT ACTION V5

建立 COST-GUOZIYI-001、COST-PUGU-001 与 PROP-HORSE-TACK-001 的基础结构候选，并继续派生人物必要角度；在马具和骑装通过前，不制作正式东翼场景。

## BATCH-A006-COMMAND-RIDING-BASE｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE + AI_EDIT；郭子仪、仆固怀恩以各自身份母图派生；马具 V2 在首图失败字段上定点返工。
- **Prompt Package：** `assets/prompts/BATCH-A006-command-riding-base/prompt-package.md`
- **Evidence Check：** 中国国家博物馆唐三彩马藏品说明，用于鞍织物、鞍鞯/障泥与革带关系的结构方向；不复制宫廷装饰。
- **Batch Result：** 两套衣甲正面候选建立；主坐骑与马具 V2 进入骑乘验证，V1 归档为返工版本。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A006-01 | COST-GUOZIYI-001 | `assets/costumes/COST-GUOZIYI-001/combined-look-front-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 中军层级、暗色维护度和身份连续成立；需继续压武士甲误读 |
| A006-02 | COST-PUGU-001 | `assets/costumes/COST-PUGU-001/combined-look-front-v001.png` | 1024×1536 | SELF-REVIEWED_CANDIDATE | 骑乘功能轮廓成立；需坐姿与文化联合审核 |
| A006-03 | PROP-HORSE-TACK-001 | `assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v001.png` | 1536×1024 | REWORK_ARCHIVED | 马体可用，鞍与宽镫带偏现代工作鞍 |
| A006-04 | PROP-HORSE-TACK-001 | `assets/props/PROP-HORSE-TACK-001/horse-tack-left-profile-v002.png` | 1536×1024 | SELECTED_FOR_RIDING_VALIDATION | 改为前后鞍桥、织物包覆、鞍鞯/障泥、窄镫带和完整胸后带关系 |

## CURRENT NEXT ACTION V6

优先制作仆固怀恩骑乘接触验证与回纥骑兵组合方向；并行补齐旗号、三名同列标志物和其余材料板。正式场景和镜头仍冻结。

## BATCH-A007-RIDER-CONTACT｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE；联合 COST-PUGU-001 正面候选与 PROP-HORSE-TACK-001 V2 左侧母图。
- **Prompt Package：** `assets/prompts/BATCH-A007-rider-contact/prompt-package.md`
- **Batch Result：** 静态左侧骑乘关系通过，可作为回纥骑兵组合的结构父资产；动态状态仍未批准。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A007-01 | PROP-HORSE-TACK-001 / COST-PUGU-001 | `assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png` | 1536×1024 | STATIC_RIDER_CONTACT_PASS | 骨盆—鞍、近侧脚—镫、手—缰和衣摆—坐具关系成立；远侧脚镫待其他角度验证 |

## CURRENT NEXT ACTION V7

以静态骑乘父资产建立 GROUP-UYGHUR-CAV-001 的三骑组织关系与受控差异；不得复制仆固怀恩面孔到普通骑手。

## BATCH-A008-UYGHUR-CAVALRY-BASE｜2026-10-01

- **Source：** AI_GENERATE_WITH_REFERENCE；以静态骑乘接触图为结构父资产。
- **Prompt Package：** `assets/prompts/BATCH-A008-uyghur-cavalry-base/prompt-package.md`
- **Batch Result：** 三骑正斜向组织、普通骑手差异和马匹变体通过基础自审；仍需扩大装备差异与生成动态状态。

| Unit | Asset ID | File | Dimensions | Result | Summary |
|---|---|---|---|---|---|
| A008-01 | GROUP-UYGHUR-CAV-001 | `assets/groups/GROUP-UYGHUR-CAV-001/formation-three-riders-v001.png` | 1536×1024 | SELF-REVIEWED_BASE_PASS | 三脸三马受控差异、脚镫与缰绳接触、队列间距成立 |

## CURRENT NEXT ACTION V8

建立唐军前列 4—6 个轮廓与三名可追踪同列；其状态变化承担高伤亡暗示，不使用未经核实的伤亡数字。

## BATCH-A009-TANG-CONTINUITY｜2026-10-02

内置图像生成/编辑；提示规格见 `assets/prompts/BATCH-A009-tang-continuity/prompt-package.md`。

- `assets/groups/GROUP-TANG-FRONT-001/lineup-six-soldiers-v001.png`：上一轮生成，补丁与裹臂错位，REWORK_ARCHIVED。
- 同目录 `lineup-six-soldiers-v002.png`：修正补丁归属与右臂裹布，BASE_CANDIDATE；主角近景仍以已批准 Canon Face 为准。
- 同目录 `soldier-a-front-v001.png`、`soldier-a-left-side-v001.png`：A身份/缺左护耳参考，自审通过基础识别。
- 同目录 `soldier-b-front-v001.png`、`soldier-b-right-side-v001.png`：B身份/右裹臂参考，自审通过基础识别。
- 同目录 `soldier-c-front-v001.png`、`soldier-c-left-side-v001.png`：C身份/B刀组合参考，自审通过基础识别。
- `assets/props/PROP-CONTINUITY-MARKERS-001/marker-a-helmet-m3-v001.png`：整顶缺左护耳头盔落地候选。
- 同目录 `marker-b-cloth-m3-v001.png`：硬套筒轮廓，REWORK_ARCHIVED；`marker-b-cloth-m3-v002.png`：松脱重力修订候选。
- 同目录 `marker-c-blade-m3-v001.png`：同家族遗刀落地候选。

审查限制：独立图与群像甲片排数/织物仍有小幅变化；三人受力动作、五群体状态、M1/M2转移与精确道具细节未齐。未批准为资产阶段完成。将战后遗物从“缺失护耳再次出现”统一为整顶缺左护耳头盔，剧本、登记和冻结镜头草稿已同步。

## BATCH-A010-FLAGS｜2026-10-02

内置图像生成/编辑；执行规格见 `assets/prompts/BATCH-A010-flags/prompt-package.md`。

| File under assets/props/PROP-FLAGS-001/ | Result |
|---|---|
| `flags-comparison-front-v001.png` | 基础三旗自审通过 |
| `flags-comparison-reverse-v001.png` | 反向轮廓候选，反面缝合仍需细节证据 |
| `front-flag-f1-tilted-v001.png` | 倾斜轻损候选，须旗手组合验证持旗受力 |
| `front-flag-f4-broken-v001.png` | 两段折杆/布旗落地接触候选 |

旗号为原创识别设计；系统未完成。下一批补燕军群体、旗手组合及F3方向因果；其余人物/服装/环境状态继续按完成表补齐。

## BATCH-A011-YAN-GROUP｜2026-10-02

内置图像生成；提示规格见 `assets/prompts/BATCH-A011-yan-group/prompt-package.md`。

| Unit | Asset ID | File | Result | Review |
|---|---|---|---|---|
| A011-01 | GROUP-YAN-001 | `assets/groups/GROUP-YAN-001/infantry-five-base-v001.png` | BASE_CANDIDATE | 五人区别成立；旗面破损过重，不能用于 Y0 |
| A011-02 | GROUP-YAN-001 | `assets/groups/GROUP-YAN-001/cavalry-three-base-v001.png` | BASE_CANDIDATE | 三骑静态关系成立；动态与阵营同框辨识待验 |

两张母图只供静态资产派生；Y0—Y4、动作受力和旗号因果仍缺。下一批继续补资产状态与材料板。

## BATCH-A012-MATERIALS｜2026-10-02

内置图像生成；提示规格见 `assets/prompts/BATCH-A012-materials/prompt-package.md`。

| Unit | File under `assets/locations/MAT-BATTLEFIELD-001/` | Result | Review |
|---|---|---|---|
| A012-01 | `material-dark-metal-v001.png` | BASE_CANDIDATE | M0—M2 材质状态可读；刀身只作材质参照 |
| A012-02 | `material-military-textile-v001.png` | PARTIAL_REWORK | T1 汗湿不明显；T0/T2/T3 候选保留 |
| A012-03 | `material-leather-v001.png` | PARTIAL_REWORK | L1 光泽扩散过宽，超出局部接触区 |
| A012-04 | `material-wood-grip-v001.png` | BASE_CANDIDATE | W0/W1 对照可读；待与 B 型长刀联合验收 |
| A012-05 | `material-leather-v002.png` | REVISED_CANDIDATE | L1 大面积光泽已压低；其他栏纹理轻微漂移，整图作为新版本审核 |
| A012-06 | `material-military-textile-v002.png` | CONDITIONAL_CANDIDATE | T1 汗湿差异较 V1 增强，但仍偏细微，仅供近景参考 |

材料系统仍缺三种光线响应和尘土交互；织物 V2 的 T1 镜头可读性需再验。

## INTAKE-A013-ANXI-USER-IMAGES｜2026-10-02

用户提供 `C:\Users\大文\Desktop\picture` 下 9 张 1024×1536 PNG；逐张视觉审核后复制到 `assets/characters/CHAR-ANXI-001/`，桌面原件保留。未将这些图片记作本工具生成。

| Source file | Saved file | Review |
|---|---|---|
| `灰背景下的古装武士肖像.png` | `body-left45-v001.png` | 全身左前45°候选，通过基础自审 |
| `灰背景下的东亚古装男子侧身肖像.png` | `body-left-profile-v001.png` | 全身左侧候选，通过基础自审 |
| `ChatGPT 图像 2026年10月2日 20_38_32-1.png` | `body-back-v001.png` | 全身背面候选，通过基础自审 |
| `ChatGPT 图像 2026年10月2日 20_38_33-2.png` | `body-right-profile-v001.png` | 全身右侧候选，通过基础自审 |
| `ChatGPT 图像 2026年10月2日 20_38_34-3.png` | `body-right45-v001.png` | 全身右前45°候选，通过基础自审 |
| `ChatGPT 图像 2026年10月2日 20_39_20-1.png` | `expression-c1-alert-v001.png` | 戒备眼神候选 |
| `ChatGPT 图像 2026年10月2日 20_39_22-2.png` | `expression-c3-exhausted-v001.png` | 疲劳汗尘与额头/面颊小擦伤候选 |
| `ChatGPT 图像 2026年10月2日 20_39_23-3.png` | `expression-c4-aftermath-v001.png` | REWORK_ARCHIVED：C3 的擦伤和尘汗在 C4 消失 |
| `ChatGPT 图像 2026年10月2日 20_39_24-4.png` | `detail-skin-hair-hands-v001.png` | 细节板候选；皮肤微纹偏强化，Canon V2 仍是肤质优先参考 |

当批下一动作原为修订 C4；后续已在 INTAKE-A015 收到 V2，当前结论以 A015 和资产合同为准。其余资产仍按完成表推进。

## INTAKE-A014-LISIYE-USER-IMAGES｜2026-10-03

用户提供 `C:\Users\大文\Desktop\picture\新建文件夹` 下 8 张 PNG；原件保留，复制到对应角色/衣甲资产目录。未将这些图片记作本工具生成。

| Source file | Saved file | Review |
|---|---|---|
| `ChatGPT 图像 2026年10月2日 21_11_40-1.png` | `characters/CHAR-LISIYE-001/body-left45-v001.png` | 单幅全身左前45°候选；身份与衣着延续 |
| `ChatGPT 图像 2026年10月2日 21_11_47-2.png` | `characters/CHAR-LISIYE-001/body-back-v001.png` | 单幅全身背面候选 |
| `ChatGPT 图像 2026年10月2日 21_11_51-3.png` | `characters/CHAR-LISIYE-001/body-profile-facing-right-v001.png` | 单幅全身侧面候选，画面中面部朝右 |
| `武士角色多角度设定图.png` | `characters/CHAR-LISIYE-001/reference-contact-sheet-user-v001.png` | REFERENCE_ONLY；拼版不充当独立原图 |
| `战士肖像：坚毅与疲惫-3.png` | `characters/CHAR-LISIYE-001/reference-expression-diptych-user-v001.png` | REFERENCE_ONLY；双联图不充当单独表情状态 |
| `ChatGPT 图像 2026年10月2日 21_11_54-4.png` | `costumes/COST-LISIYE-001/reference-armored-portrait-clean-user-v001.png` | REFERENCE_ONLY；完整胸甲与已定 L1 敞开结构不一致 |
| `ChatGPT 图像 2026年10月2日 21_11_55-5.png` | `costumes/COST-LISIYE-001/reference-armored-portrait-dusty-user-v001.png` | REFERENCE_ONLY；尘土增加，但仍非 L2 敞开衣甲 |
| `战损古代武士双人肖像-1.png` | `costumes/COST-LISIYE-001/reference-battlewear-diptych-user-v001.png` | REFERENCE_ONLY；只作损伤氛围比较 |

本批只补齐三张可单独使用的身份角度候选；不改变 L0/L1/L2 衣甲状态的既有完成判定。

## INTAKE-A015-ANXI-C4-REWORK｜2026-10-03

用户在对话中提供 C4 修订图，复制到 `assets/characters/CHAR-ANXI-001/expression-c4-aftermath-v002.png`；原始临时附件与 C4 V1 均未覆盖。

- 对照 C3：画面左侧额角、双颊擦伤位置与汗尘延续，修正了 V1 的连续性失败。
- 表情：眉眼与嘴部略放松，但 C3/C4 差别偏小；标为 CONTINUITY_PASS_CANDIDATE，待跨状态并排审核情绪辨识。
- 不视为 CHAR-ANXI-001 全资产放行，也不据此跳至分镜或视频生成。

## INTAKE-A016-LISIYE-RIGHT45｜2026-10-03

用户在对话中提供李嗣业单幅全身图，复制到 `assets/characters/CHAR-LISIYE-001/body-right45-v001.png`；原始附件未覆盖。

- 对照 Canon Face、Body Identity 正面及已有左前 45°：身份、发髻、灰褐内层衣、体态和鞋靴基本连续；躯干与站姿朝向相反，可作为反向全身 45° 候选。
- 头部仍偏正面，不能计为独立头部右前 45°验证图；腰带垂带落点因转向有轻微变化，后续联合审核继续观察。
- 下一独立角度：全身纯侧面，面部朝画面左侧；不得镜像已有面部朝右的侧面图。

## INTAKE-A017-LISIYE-FOLDER-RECONCILIATION｜2026-10-04

按用户要求重新核对 `C:\Users\大文\Desktop\picture\新建文件夹`。文件夹共 8 张 PNG，全部已在角色及衣甲资产目录入库，逐一验证源文件与归档文件哈希一致，原件保留。映射沿用 A014，无重复复制。

确认多角度拼版上排第二格已提供朝画面左侧的全身侧面。此前将“缺独立原图”表述为“缺角度、需重新生成”不准确，现撤销 A016 的该项生成安排并同步更新完成表、角色合同与提示词包。拼版仍按实际分辨率作参考，未冒充独立高分辨率原图；衣甲状态的连续性审核结论保持记录。

## GENERATION-A018-LISIYE-COSTUME｜2026-10-04

- 工具：内置 imagegen；实际生成两张图片，原结果复制进入项目。
- `costumes/COST-LISIYE-001/state-l2-dust-front-v001.png`：编辑父图为 L1 正面；提示意图为保持身份、构图、敞开衣甲与装备，仅增加推进后局部黄灰尘土、汗、轻微磨损和克制疲劳。检查：胸甲未恢复、衣层与身份连续；候选通过。
- `costumes/COST-LISIYE-001/state-l0-complete-back-v001.png`：父参考为 L0 正面；提示意图为同一人物完整衣甲的全身正背视图，灰背景、自然光、同甲片与腰甲结构，无披风、武器或新污染。检查：正背制造家族连续、身体厚度合理；扣带路径仍为重构候选，待细节联合审核。
- 原生成路径：`C:/Users/大文/.codex/generated_images/01a0e6ba-8ade-75b0-b0d0-58e2e27368d4/exec-a4e08d6f-ea1f-41d4-b390-f3cc61651101.png` 与 `exec-d703ee2b-73c1-48ca-98d7-e67fec6168b2.png`。
- 全部资产目标保持进行中；本批未放行资产阶段，下一项为 L1 侧面与扣带结构。

## GENERATION-A019-LISIYE-DETAIL-AND-B-PROP｜2026-10-04

内置 imagegen 生成 4 张实际图片，复制归档后逐张验证哈希一致；详细提示见 `assets/prompts/BATCH-A019-prompt-package.md`。

| File under assets/ | Parent | Review |
|---|---|---|
| `costumes/COST-LISIYE-001/state-l1-open-side-v001.png` | L1 front | 候选通过；侧面裸露范围与衣甲连续，非解甲动作证明 |
| `costumes/COST-LISIYE-001/detail-fastening-path-v001.png` | L0 + L1 front | 局部连接候选；四处细节可读，带件解开顺序仍需动作设计解释 |
| `props/PROP-LONGBLADE-001/structure-b-detail-v001.png` | candidate comparison V2 middle B | 全形、刃背厚度、套筒和柄尾候选；未晋升为最终几何母图 |
| `costumes/COST-LISIYE-001/contact-longblade-l1-v001.png` | L1 + new B structure | 静态手柄接触与重心候选；刀尖曲率轻微漂移，需校准后才能作为完整武器身份锚点 |

全资产目标保持进行中。未将候选生成等同于资产阶段通过。

## GENERATION-A020-GUOZIYI-ANGLES-AND-COMMAND｜2026-10-04

内置 imagegen 生成 6 张单幅资产，归档后源/目标哈希逐一一致。完整逐张提示见 `assets/prompts/BATCH-A020-prompt-package.md`。

| File under assets/ | Review |
|---|---|
| `characters/CHAR-GUOZIYI-001/body-profile-facing-right-v001.png` | 全身侧面、同身份及衣层候选；袖口内层露出稍增加 |
| `characters/CHAR-GUOZIYI-001/body-back-v001.png` | 同肩宽、发髻、衣层及绑腿背面候选 |
| `characters/CHAR-GUOZIYI-001/body-45-facing-left-v001.png` | 头身同向45°、年龄与须发连续候选 |
| `costumes/COST-GUOZIYI-001/combined-look-back-v001.png` | 同制造家族正背候选；背面带件路径待细节校准 |
| `costumes/COST-GUOZIYI-001/combined-look-side-right-v001.png` | 侧面低光泽甲片与窄红褐边延续；肩甲贴身、无披风 |
| `characters/CHAR-GUOZIYI-001/action-g0-raise-hand-v001.png` | 五指、屈肘、稳定站姿可读；服装在COST合同交叉引用 |

全部为像素自审候选；郭子仪仍缺反向角度、轻尘与旗号同框核对，未放行整类资产。
