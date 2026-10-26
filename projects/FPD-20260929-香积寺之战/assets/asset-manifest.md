# ASSET MANIFEST

## 用户接手回执｜2026-10-05

- 最新范围：报告现有完成情况，交接剩余静态资产生图提示词；执行改为USER_GENERATE，本次无新增媒体，不自动批准或晋升现有候选。
- 实际存档108张PNG，包含失败、拼版与历史图；真实状态见 `asset-status-20261005.md`。不得视为108张合格图或19类已完成。
- 最新执行包：`prompts/USER-HANDOFF-20261005/index.md`，102张卡（95张候选/返工，7张条件/版式）；旧全剩余V1只留档。
- 既有李嗣业全身角度与郭子仪衣甲不重复生成；骑乘动态结果归COST-PUGU一处并交叉覆盖人物/马具；清洁空气可复用合格B0；最终中文独立排字。

## P0骑乘交叉登记｜2026-10-05

CHAR-PUGU-001及COST-PUGU-001复用 `assets/props/PROP-HORSE-TACK-001/rider-contact-left-v001.png` 为P0观察/静态坐姿基准；静态左侧比例与近侧接触通过，不代表双侧或动态审核。A031两次连接失败，无新增图片。

## A030 补充登记｜2026-10-05

COST-PUGU-001新增 `assets/costumes/COST-PUGU-001/combined-look-45-right-v001.png`，SELF-REVIEWED_PASS_FOR_DIRECTION；替代A028错误方向版用于同向45°派生。骑乘联合审核未完成。

## A029 补充登记｜2026-10-04

LOC-BATTLEFIELD-001的 `assets/locations/LOC-BATTLEFIELD-001/state-b0-prebattle-v001.png`、`state-b0-prebattle-v002.png`、`state-b0-prebattle-v003.png` 均留档，HOLD_GROUND_TEXTURE，不计合格B0。宏观地形保持，重复微纹理未解决；原拓扑仍为唯一空间父图。

## A028 恢复核验｜2026-10-04

COST-PUGU-001 `assets/costumes/COST-PUGU-001/combined-look-45-left-v001.png` 已留档，HOLD_HEAD_BODY_DIRECTION。头朝左、身体偏右，不计合格45°，不进入下游。原运行句柄已失效。

## A028 补充登记｜2026-10-04

COST-PUGU-001新增 `assets/costumes/COST-PUGU-001/combined-look-side-right-v001.png`，SELF-REVIEWED_CANDIDATE；朝左45°尚在生成，不计入入库数量。

## A027 补充登记｜2026-10-04

COST-PUGU-001新增 `assets/costumes/COST-PUGU-001/combined-look-side-left-v001.png` 与 `assets/costumes/COST-PUGU-001/combined-look-back-v001.png`，SELF-REVIEWED_CANDIDATE；骑装另一侧/45°及骑乘联合审核待完成。

## A026 补充登记｜2026-10-04

CHAR-PUGU-001新增 `assets/characters/CHAR-PUGU-001/body-profile-facing-left-v001.png`、`assets/characters/CHAR-PUGU-001/body-45-facing-left-v001.png`、`assets/characters/CHAR-PUGU-001/body-45-facing-right-v001.png`，SELF-REVIEWED_CANDIDATE；全身六方向候选齐备，骑乘与头部验收未完成。

## A025 补充登记｜2026-10-04

CHAR-PUGU-001新增 `assets/characters/CHAR-PUGU-001/body-profile-facing-right-v001.png` 与 `assets/characters/CHAR-PUGU-001/body-back-v001.png`，SELF-REVIEWED_CANDIDATE；其余角度与骑乘联合审核待完成。

## A024 补充登记｜2026-10-04

COST-GUOZIYI-001新增 `assets/costumes/COST-GUOZIYI-001/test-command-flag-hierarchy-v001.png`，SELF-REVIEWED_PASS_FOR_HIERARCHY；PROP-FLAGS-001交叉引用，只证明同框可读性，木底座为展示工具，不进入战场。

## A023 补充登记｜2026-10-04

COST-GUOZIYI-001：`assets/costumes/COST-GUOZIYI-001/combined-look-side-left-v002.png` 为侧腰修订自审通过版，取代V1用于后续派生，原版留档；`assets/costumes/COST-GUOZIYI-001/detail-protection-fastening-v001.png` 为结构细节候选，不能证明完整五指或史实甲型。

## A022 补充登记｜2026-10-04

COST-GUOZIYI-001新增 `assets/costumes/COST-GUOZIYI-001/combined-look-side-left-v001.png`（HOLD_SASH_POSITION）与 `assets/costumes/COST-GUOZIYI-001/combined-look-45-right-v001.png`（SELF-REVIEWED_CANDIDATE）。不替换正面基准，联合审核未完成。

## A021 补充登记｜2026-10-04

- CHAR-GUOZIYI-001：新增 `assets/characters/CHAR-GUOZIYI-001/body-profile-facing-left-v001.png`、`assets/characters/CHAR-GUOZIYI-001/body-45-facing-right-v001.png`，SELF-REVIEWED_CANDIDATE。
- COST-GUOZIYI-001：新增 `assets/costumes/COST-GUOZIYI-001/state-g1-light-dust-v001.png`，角色动作状态交叉引用；SELF-REVIEWED_CANDIDATE，联合审核待完成。

- **Adopted Method IDs / Versions / Asset Scope：** World & Visual Bible V1；Asset Requirements V1；Atmosphere State Register V1；本轮仅处理第一批 P0 基础资产。

## PROJECT

- **Project ID：** FPD-20260929-香积寺之战
- **Visual Bible Version：** V1
- **Manifest Version：** V1.16
- **Mode：** REVIEW

## ASSETS

| Asset ID | Type | Working Name | Version | Depends On | Priority | Required Views / Detail Plates | Status | Contract Path | File Paths | Approval |
|---|---|---|---|---|---|---|---|---|---|---|
| LOC-BATTLEFIELD-001 | LOCATION | 香积寺附近连续战场 | V1.2 | World & Visual Bible V1 | P0 | 战场拓扑、前后关系、东翼关系、战前/战后同空间状态、地表细节 | READY_FOR_DERIVATION | `assets/locations/LOC-BATTLEFIELD-001/asset-contract.md` | `assets/locations/LOC-BATTLEFIELD-001/topology-plan-v002.png`；`topology-zones-v001.svg`；`topology-zones-v001.png` | TOPOLOGY + A—G OVERLAY PASS |
| MAT-BATTLEFIELD-001 | MATERIAL | 战场地表与军事材质校准组 | V1.2 | LOC-BATTLEFIELD-001 | P0 | 土地、暗色金属、军用织物、皮革、木柄状态板 | BASE_PLATES_DERIVING | `assets/locations/MAT-BATTLEFIELD-001/asset-contract.md` | `assets/locations/MAT-BATTLEFIELD-001/material-ground-v002.png`；`material-dark-metal-v001.png`；`material-military-textile-v001.png`；`material-military-textile-v002.png`；`material-leather-v001.png`；`material-leather-v002.png`；`material-wood-grip-v001.png` | GROUND PASS / METAL + WOOD + LEATHER V2 CANDIDATES / TEXTILE V2 CONDITIONAL |
| PROP-LONGBLADE-001 | PROP | 前军步兵长刀候选系统 | V1.2 | Research CLM-003/007/013/016 | P0 | 2—3 个证据受控候选、持握比例、连接和材料细节 | SELECTED_FOR_DEVELOPMENT | `assets/props/PROP-LONGBLADE-001/asset-contract.md` | `assets/props/PROP-LONGBLADE-001/candidate-comparison-v002.png`；`human-scale-hold-b-v001.png`；`formation-spacing-b-v001.png` | B SELECTED / ERGONOMICS PASS |
| CHAR-ANXI-001 | CHARACTER | 无名安西军士 | V1.6 | Character System V1；COST-ANXI-FRONT-001 | P0 | Canon Face、头部五视图、身体六视图、C1/C3/C4 与细节 | CANON_APPROVED_DERIVING | `assets/characters/CHAR-ANXI-001/asset-contract.md` | `canon-face-front-v002.png`；`head-left45-v001.png`；`head-left-profile-v001.png`；`head-right-profile-v001.png`；`head-right45-v001.png`；`body-identity-front-v001.png`；`body-left45-v001.png`；`body-left-profile-v001.png`；`body-back-v001.png`；`body-right-profile-v001.png`；`body-right45-v001.png`；`expression-c1-alert-v001.png`；`expression-c3-exhausted-v001.png`；`expression-c4-aftermath-v001.png`（返工留档）；`expression-c4-aftermath-v002.png`；`detail-skin-hair-hands-v001.png` | CANON USER APPROVED / BODY ANGLES PASS / C1+C3+DETAIL CANDIDATE / C4 V2 CONTINUITY PASS CANDIDATE |
| CHAR-LISIYE-001 | CHARACTER | 李嗣业（非肖像式历史重构） | V1.3 | Character System V1 | P0 | Canon Face、Body Identity、后续角度与 L0/L1/L2 | IDENTITY_ANGLES_PARTIAL | `assets/characters/CHAR-LISIYE-001/asset-contract.md` | `canon-face-front-v001.png`；`body-identity-front-v001.png`；`body-left45-v001.png`；`body-right45-v001.png`；`body-back-v001.png`；`body-profile-facing-right-v001.png`；两张参考拼版 | SELF-REVIEWED_CANDIDATE |
| COST-ANXI-FRONT-001 | COSTUME | 前军基础衣甲系统 | V1.1 | CHAR-ANXI-001；MAT-BATTLEFIELD-001 | P0 | 正背侧、六视图、四种污染/损伤状态、长刀持握 | BASE_FRONT_BACK_GENERATED | `assets/costumes/COST-ANXI-FRONT-001/asset-contract.md` | `combined-look-front-v001.png`；`combined-look-back-v001.png` | SELF-REVIEWED_CANDIDATE |
| COST-LISIYE-001 | COSTUME | 李嗣业衣甲状态系统 | V1.3 | CHAR-LISIYE-001；COST-ANXI-FRONT-001；PROP-LONGBLADE-001 | P0 | L0 正背、L1 正侧、扣带路径、L2、长刀受力 | REQUIRED_PLATES_GENERATED_PENDING_REVIEW | `assets/costumes/COST-LISIYE-001/asset-contract.md` | `state-l0-complete-front-v001.png`；`state-l0-complete-back-v001.png`；`state-l1-open-front-v001.png`；`state-l1-open-side-v001.png`；`state-l2-dust-front-v001.png`；`detail-fastening-path-v001.png`；`contact-longblade-l1-v001.png`；三张参考图（非验收） | CANDIDATES / HOLD BLADE GEOMETRY REWORK |
| CHAR-GUOZIYI-001 | CHARACTER | 郭子仪（非肖像式历史重构） | V1.2 | Character System V1 | P0 | Canon Face、Body Identity、必要角度、观察/抬手状态 | BODY_ANGLES_AND_G0_DERIVING | `assets/characters/CHAR-GUOZIYI-001/asset-contract.md` | `canon-face-front-v001.png`；`body-identity-front-v001.png`；`body-profile-facing-right-v001.png`；`body-back-v001.png`；`body-45-facing-left-v001.png`；`action-g0-raise-hand-v001.png` | SELF-REVIEWED_CANDIDATE |
| CHAR-PUGU-001 | CHARACTER | 仆固怀恩（非肖像式历史重构） | V1.1 | Character System V1 | P0 | Canon Face、Body Identity、必要角度、骑乘三状态 | IDENTITY_BASE_GENERATED | `assets/characters/CHAR-PUGU-001/asset-contract.md` | `canon-face-front-v001.png`；`body-identity-front-v001.png` | SELF-REVIEWED_PASS_FOR_DERIVATION / RIDING REVIEW PENDING |
| COST-GUOZIYI-001 | COSTUME | 郭子仪中军指挥衣甲 | V1.2 | CHAR-GUOZIYI-001；PROP-FLAGS-001 | P1 | 正背侧、轻尘、抬手与旗号层级测试 | FRONT_BACK_SIDE_GENERATED | `assets/costumes/COST-GUOZIYI-001/asset-contract.md` | `combined-look-front-v001.png`；`combined-look-back-v001.png`；`combined-look-side-right-v001.png`；角色G0抬手交叉引用 | SELF-REVIEWED_CANDIDATE |
| COST-PUGU-001 | COSTUME | 仆固怀恩骑乘服装 | V1.1 | CHAR-PUGU-001；PROP-HORSE-TACK-001；GROUP-UYGHUR-CAV-001 | P0 | 正背侧、骑姿、转向/加速/汗尘 | FRONT_BASE_GENERATED | `assets/costumes/COST-PUGU-001/asset-contract.md` | `combined-look-front-v001.png` | SELF-REVIEWED_CANDIDATE / JOINT REVIEW REQUIRED |
| PROP-HORSE-TACK-001 | PROP | 骑兵坐骑与马具系统 | V1.2 | CHAR-PUGU-001；COST-PUGU-001；GROUP-UYGHUR-CAV-001 | P0 | 主坐骑多角度、马具拆分、H0—H3、接触验证 | STATIC_RIDER_CONTACT_PASS | `assets/props/PROP-HORSE-TACK-001/asset-contract.md` | `horse-tack-left-profile-v001.png`；`horse-tack-left-profile-v002.png`；`rider-contact-left-v001.png` | V2 + STATIC CONTACT PASS / V1 REWORK_ARCHIVED |
| GROUP-UYGHUR-CAV-001 | GROUP | 回纥骑兵组织资产 | V1.1 | CHAR-PUGU-001；COST-PUGU-001；PROP-HORSE-TACK-001 | P0 | 三向组织、4—6轮廓、U0—U3 | THREE_RIDER_BASE_GENERATED | `assets/groups/GROUP-UYGHUR-CAV-001/asset-contract.md` | `formation-three-riders-v001.png` | SELF-REVIEWED_BASE_PASS |

## BLOCKING DECISIONS

## ADDITIONAL GENERATED ASSETS｜2026-10-02

| Asset ID | Version | Status | Contract | Images |
|---|---|---|---|---|
| GROUP-TANG-FRONT-001 | V1.1 | IDENTITY_AND_MARKERS_DERIVING | `assets/groups/GROUP-TANG-FRONT-001/asset-contract.md` | `lineup-six-soldiers-v002.png`；`soldier-a-front-v001.png`；`soldier-a-left-side-v001.png`；`soldier-b-front-v001.png`；`soldier-b-right-side-v001.png`；`soldier-c-front-v001.png`；`soldier-c-left-side-v001.png` |
| PROP-CONTINUITY-MARKERS-001 | V1.1 | M0_M3_CANDIDATES_GENERATED | `assets/props/PROP-CONTINUITY-MARKERS-001/asset-contract.md` | `marker-a-helmet-m3-v001.png`；`marker-b-cloth-m3-v002.png`；`marker-c-blade-m3-v001.png` |
| PROP-FLAGS-001 | V1.1 | BASE_AND_FRONT_STATES_GENERATED | `assets/props/PROP-FLAGS-001/asset-contract.md` | `flags-comparison-front-v001.png`；`flags-comparison-reverse-v001.png`；`front-flag-f1-tilted-v001.png`；`front-flag-f4-broken-v001.png` |
| GROUP-YAN-001 | V1.0 | INFANTRY_AND_CAVALRY_BASE_GENERATED | `assets/groups/GROUP-YAN-001/asset-contract.md` | `infantry-five-base-v001.png`；`cavalry-three-base-v001.png` |

上述图片各位于对应合同同目录；候选自审不等于用户最终批准，具体失败版及缺口见合同。人物M0使用态复用群体目录，不复制到道具目录。

## EVIDENCE LIMITS

### A019 结构候选补充｜2026-10-04

`assets/props/PROP-LONGBLADE-001/structure-b-detail-v001.png` 已生成并归档，涵盖 B 型全形、刃背厚度、套筒与柄尾；SELF-REVIEWED_CANDIDATE。候选比较 V2 中 B 型仍为几何优先参考，待多图联合审核后再晋升。

- **CHAR-ANXI-001：** 用户于 2026-10-01 接受 V2；该图锁定为 Canon Face 身份母图，不从外部演员或影视角色复制。
- **PROP-LONGBLADE-001：** 陌刀形制存在争议。实际资产不得以单一候选冒充确证形制；第一批只允许生成并列候选，批准时标注“视觉重构”。
- **LOC-BATTLEFIELD-001：** 真实作战轴与正东的精确夹角未知。拓扑图使用“画面示意上方=燕军方向、右侧=真实东翼”的工作坐标，仅为制作关系图，不宣称历史方位测绘。

## DEFERRED ASSETS

- **人物：** 四名核心人物均已有身份母资产；CHAR-ANXI-001 头部五视图与全身六视图已入库，C4 V2伤痕连续性修复、情绪联合审核待完成；其余三名必要头部角度与状态进入派生阶段，已有全身角度不重复做。
- **群体：** 唐军已有六轮廓/三同列正侧面、回纥已有三骑基础、燕军已有步兵五人与骑兵三骑基础；三组剧情状态均待补齐。
- **服装：** 四套均有基础候选；李嗣业L0正背/L1正侧/L2、郭子仪正背双侧与轻尘、仆固怀恩多角度/P0静态均已存在，详见各合同。主角尚需侧/45°和战损，骑将需动态，其他主要为局部校准与联合审核，不重复整套生成。
- **道具：** 旗号基础及前军F1/F4、三标志物M0/M3、马具静态接触已有候选，其余视图与中间状态仍需派生。
- **环境与图形：** ENV-ATMOSPHERE-001、GRAPHIC-HISTORICAL-ID-001。
- 延后理由：先锁定空间、材质、兵器候选和主角身份，再建立依赖它们的组合造型与群体资产；避免一次生成过多互相矛盾的版本。

## NEXT STAGE

- **Primary Recommendation：** Complete All Static Assets Before Direction
- **Reason：** 先完成镜头必要静态资产与验收；最新用户选择自行生成，使用2026-10-05交接包。导演方案、分镜和视频提示词尚未因该交接自动放行，视频由用户操作。
