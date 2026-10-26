# Asset Contract

## Asset states

- `PLANNED`: 合同和任务存在，尚未生成。
- `GENERATED_PENDING_REVIEW`: 文件存在，尚未完成真实视觉审核。
- `REWORK`: 已审核但至少一个阻断问题未通过。
- `APPROVED`: 实际资产通过身份、结构、连续性和范围审核。
- `REJECTED`: 不再继续使用，保留记录防止下游误用。

文本完整、文件存在和视觉通过是三种不同证据。不得自动把前两者升级为 APPROVED。

## Required fields

- `Asset ID`, `Type`, `Version`, `Status`, `Purpose`
- `Source Visual Bible Version`
- `Visual Rule / State IDs`、`Presentation Mode / Artistic Rule IDs`、`Observable Acceptance`、`Source Versions & Scope`
- `Evidence Status`
- `Locked Features`
- `Variable States`
- `Presentation Choices`
- `Unknown / Open Fields`
- `Required Views / Plates`
- `Canonical Face / Body Anchor`
- `View Matrix and File-per-view Status`
- `Material Detail Plates`
- `Combined Look Dependencies`（Character / Costume / Makeup-Hair versions）
- `Reference Role Map`
- `Derivation Parent / Edit Target`
- `Change / Preserve / Constraints`（编辑或派生时）
- `Negative Constraints`
- `Files and Paths`
- `Review Results`
- `Approval Scope`、`Unverified / Deferred Use`
- `Downstream Use`
- `Change Log`

## Reference roles

每个参考文件只能使用登记过的角色：`IDENTITY / WARDROBE / POSE / TOPOLOGY / MATERIAL / STYLE / COMPOSITION / EDIT TARGET`。同一文件可以承担多个不冲突角色，但必须逐项写明；模型不能从风格参考自行推断人物身份、服装史实或场景拓扑。

## View and use coverage

View Matrix 记录 View / Plate、Need / Source、Required（REQUIRED / DEFERRED / NOT_REQUIRED）、Derivation Parent、File Path、Status 与 Review Notes。Need / Source 回指 Scene、动作、预计观看范围或连续性风险；不要求先锁 Shot List，不按主角身份默认六视图。DEFERRED / NOT_REQUIRED 是需求标记，不是新增资产批准状态。

Canonical Anchor 按辨识用途选正脸、体态或轮廓；需要露脸时必须有已批准面部依据，纯背影锚点不能证明未知面部。派生 Parent / Edit Target 须写确切文件、版本和允许引用的批准范围；六视图仅在实际需要时建立，原有批准不随新需求无关重做。

## Review dimensions

### Shared

- 正确资产类型与范围
- identity anchors 不漂移
- 几何、比例、材料与静态使用关系符合用途和批准呈现规则；非写实层按 Artistic Rule IDs 审核，不一律用摄影写实裁决
- 没有多余肢体、物件、文字、水印或背景竞争
- 图像文件可用且路径准确

### Character

- 脸、年龄范围、体态、发际线/发型、服装层与配饰一致
- 当前必要视图是同一身份且各有独立原图；未要求的角度可延期，未验证面部不能供露脸使用
- 手脚和非人结构数量正确
- 状态差异没有改变身份

### Location

- 正反视图拓扑一致
- 出入口、固定标志、尺度与光源方向可解释
- 物体不会在视图之间凭空消失或镜像翻转

### Prop / costume

- 尺度、可见面、材料、开合/穿戴/持用逻辑一致
- 新旧、损坏或污染状态可从同一基础身份派生
- 独立服装合同与 Combined Look 中的版型、层次、材料、配饰和穿戴方式一致

### Use and artistic coverage

Review Results 分别记 Usability Review 与 Artistic Rule Review（PASS / REVISE / NOT_EVALUATED）及可见证据、适用范围；用户已批准而未逐项评估的维度保持 NOT_EVALUATED。按具体用途检查人物比例、衣层合体、道具尺度/持用、场景出入口与锚点。单资产不能证明完整多人互动、镜头表达或动态效果，写入 Unverified / Deferred Use 与后续验证阶段，不越界生成分镜。

PHYSICAL / STYLIZED / MIXED 沿用视觉合同。有意艺术形变与随机错误根据规则和状态区分；物理空气有来源，非物理纹理/象征形态独立标 CREATIVE，不伪造现实原因。

## Approval evidence

在 contract 记录：审核者/方式、审核日期、确切文件与版本、批准范围和状态决定。AI 自审可标为 `SELF-REVIEWED`，用户明确说审核通过可标为 `USER-APPROVED`；后者足以将对应图片版本标为 `APPROVED` 并入库，不要求 AI 再做视觉审核，也不能虚构 AI 通过项。两种来源不可混写。

APPROVED 只表示 Approval Scope 中列明的文件、用途、视图与状态通过；它不自动覆盖 Unverified / Deferred Use。manifest 的 Approved Use / Unverified Use 只汇总合同，不另创批准。新增使用方向建立待验证扩展版本/视图并保留已批准版本；当前 P0 的必需用途未覆盖时不得生产放行，但可交付明确待验证的文本草稿。
