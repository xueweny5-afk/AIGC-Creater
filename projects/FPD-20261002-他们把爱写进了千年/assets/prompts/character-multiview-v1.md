# CH-MV-01｜八位人物多角度身份图交接包

**模式：USER_GENERATE / 多角度待生成。** 用户指定人物多角度一致性为核心要求。CH01/CH02 正脸 v2 已通过 AI 自审；其余正脸仍待回传审核。首张正面脸提示词在 `face-anchor-batch-01.md`；此文件是其后的**逐张编辑派生**指令。每个角度各存独立 PNG，不用一次生成多格设定板。

## 必须遵守的顺序

1. 用 `face-anchor-batch-01.md` 生成各人正脸，回传审核。CH01/CH02 已批准修复版 `canon-face-front-v2.png` 为唯一 `IDENTITY` 母图；其他人物仍须先审核各自正脸。
2. 从该正脸分别派生左右 45°；侧面用正脸 + 同侧已批准 45° 辅助。每张都要核对鼻梁、下颌、发际、耳朵、眼距和肤色。
3. 从正脸派生中性全身正面 `body-front-v1.png`。正面体态通过后，用正脸 + 正面全身派生另外五个角度。
4. 所有多角度图保持同一成年人物身份、骨架比例、发型轮廓和中性内层；**仅改变观察角度**。正式戏服另由 COSTUME 资产建立，不能在这些图中随机换衣。
5. 每次编辑在同一模型会话上传列出的母图。若工具没有“参考图编辑/图生图”能力，先停止该角度，不用纯文字新抽图替代。

**共用负面约束（以下每一条提示词均附加）：** 不要换脸、改变年龄层、身高或肩宽，不要换发型/发际线，不要把面部左右结构随机镜像；不要戏服、道具、场景、强表情、说话口型、戏剧光线、透视变形、多余人物或肢体、拼图、文字、水印。只保留单人，中性均匀光与简单背景。角色身份为本项目视觉重构，不宣称历史肖像。

## CH01｜李清照

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH01-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的李清照身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH01/head-left45-v1.png`；附加共用负面约束。
- **CH01-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的李清照身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH01/head-left-profile-v1.png`；附加共用负面约束。
- **CH01-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的李清照身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH01/head-right45-v1.png`；附加共用负面约束。
- **CH01-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的李清照身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH01/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH01-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）。编辑提示词：「以已批准的李清照正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH01/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH01-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一李清照人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH01/body-left45-v1.png`；附加共用负面约束。
- **CH01-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一李清照人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH01/body-left-v1.png`；附加共用负面约束。
- **CH01-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一李清照人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH01/body-back-v1.png`；附加共用负面约束。
- **CH01-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一李清照人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH01/body-right-v1.png`；附加共用负面约束。
- **CH01-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一李清照人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH01/body-right45-v1.png`；附加共用负面约束。

**CH01 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH02｜赵明诚

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH02-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的赵明诚身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH02/head-left45-v1.png`；附加共用负面约束。
- **CH02-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的赵明诚身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH02/head-left-profile-v1.png`；附加共用负面约束。
- **CH02-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的赵明诚身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH02/head-right45-v1.png`；附加共用负面约束。
- **CH02-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的赵明诚身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH02/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH02-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）。编辑提示词：「以已批准的赵明诚正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH02/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH02-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一赵明诚人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH02/body-left45-v1.png`；附加共用负面约束。
- **CH02-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一赵明诚人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH02/body-left-v1.png`；附加共用负面约束。
- **CH02-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一赵明诚人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH02/body-back-v1.png`；附加共用负面约束。
- **CH02-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一赵明诚人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH02/body-right-v1.png`；附加共用负面约束。
- **CH02-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一赵明诚人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH02/body-right45-v1.png`；附加共用负面约束。

**CH02 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH03｜苏轼

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH03-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的苏轼身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH03/head-left45-v1.png`；附加共用负面约束。
- **CH03-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的苏轼身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH03/head-left-profile-v1.png`；附加共用负面约束。
- **CH03-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的苏轼身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH03/head-right45-v1.png`；附加共用负面约束。
- **CH03-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的苏轼身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH03/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH03-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的苏轼正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH03/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH03-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一苏轼人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH03/body-left45-v1.png`；附加共用负面约束。
- **CH03-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一苏轼人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH03/body-left-v1.png`；附加共用负面约束。
- **CH03-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一苏轼人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH03/body-back-v1.png`；附加共用负面约束。
- **CH03-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一苏轼人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH03/body-right-v1.png`；附加共用负面约束。
- **CH03-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一苏轼人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH03/body-right45-v1.png`；附加共用负面约束。

**CH03 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH04｜王弗

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH04-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的王弗身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH04/head-left45-v1.png`；附加共用负面约束。
- **CH04-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的王弗身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH04/head-left-profile-v1.png`；附加共用负面约束。
- **CH04-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的王弗身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH04/head-right45-v1.png`；附加共用负面约束。
- **CH04-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的王弗身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH04/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH04-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的王弗正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH04/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH04-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一王弗人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH04/body-left45-v1.png`；附加共用负面约束。
- **CH04-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一王弗人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH04/body-left-v1.png`；附加共用负面约束。
- **CH04-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一王弗人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH04/body-back-v1.png`；附加共用负面约束。
- **CH04-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一王弗人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH04/body-right-v1.png`；附加共用负面约束。
- **CH04-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一王弗人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH04/body-right45-v1.png`；附加共用负面约束。

**CH04 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH05｜陆游

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH05-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的陆游身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH05/head-left45-v1.png`；附加共用负面约束。
- **CH05-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的陆游身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH05/head-left-profile-v1.png`；附加共用负面约束。
- **CH05-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的陆游身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH05/head-right45-v1.png`；附加共用负面约束。
- **CH05-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的陆游身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH05/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH05-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的陆游正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH05/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH05-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陆游人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH05/body-left45-v1.png`；附加共用负面约束。
- **CH05-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陆游人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH05/body-left-v1.png`；附加共用负面约束。
- **CH05-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陆游人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH05/body-back-v1.png`；附加共用负面约束。
- **CH05-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陆游人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH05/body-right-v1.png`；附加共用负面约束。
- **CH05-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陆游人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH05/body-right45-v1.png`；附加共用负面约束。

**CH05 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH06｜唐氏

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH06-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的唐氏身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH06/head-left45-v1.png`；附加共用负面约束。
- **CH06-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的唐氏身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH06/head-left-profile-v1.png`；附加共用负面约束。
- **CH06-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的唐氏身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH06/head-right45-v1.png`；附加共用负面约束。
- **CH06-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的唐氏身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH06/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH06-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的唐氏正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH06/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH06-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一唐氏人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH06/body-left45-v1.png`；附加共用负面约束。
- **CH06-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一唐氏人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH06/body-left-v1.png`；附加共用负面约束。
- **CH06-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一唐氏人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH06/body-back-v1.png`；附加共用负面约束。
- **CH06-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一唐氏人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH06/body-right-v1.png`；附加共用负面约束。
- **CH06-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一唐氏人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH06/body-right45-v1.png`；附加共用负面约束。

**CH06 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH07｜沈复

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH07-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的沈复身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH07/head-left45-v1.png`；附加共用负面约束。
- **CH07-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的沈复身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH07/head-left-profile-v1.png`；附加共用负面约束。
- **CH07-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的沈复身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH07/head-right45-v1.png`；附加共用负面约束。
- **CH07-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的沈复身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH07/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH07-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的沈复正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH07/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH07-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一沈复人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH07/body-left45-v1.png`；附加共用负面约束。
- **CH07-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一沈复人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH07/body-left-v1.png`；附加共用负面约束。
- **CH07-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一沈复人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH07/body-back-v1.png`；附加共用负面约束。
- **CH07-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一沈复人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH07/body-right-v1.png`；附加共用负面约束。
- **CH07-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一沈复人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH07/body-right45-v1.png`；附加共用负面约束。

**CH07 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## CH08｜陈芸

**身份母图（必须先审核）：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`。文件不存在或未通过审核时，本节后续条目暂停。

### 头部角度

- **CH08-head-left45-v1.png｜左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的陈芸身份，只改变头部朝向为左前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH08/head-left45-v1.png`；附加共用负面约束。
- **CH08-head-left-profile-v1.png｜左侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\head-left45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的陈芸身份，只改变头部朝向为左侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH08/head-left-profile-v1.png`；附加共用负面约束。
- **CH08-head-right45-v1.png｜右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）。编辑提示词：「以母图为唯一的陈芸身份，只改变头部朝向为右前四十五度，双眼仍清楚可见。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH08/head-right45-v1.png`；附加共用负面约束。
- **CH08-head-right-profile-v1.png｜右侧面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY / EDIT TARGET）；`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\head-right45-v1.png`（同侧已批准角度，仅辅助鼻颌轮廓）。编辑提示词：「以母图为唯一的陈芸身份，只改变头部朝向为右侧九十度，保留同一鼻梁、下颌和发际轮廓。保持脸宽、眼距、眉眼鼻口关系、发际线、耳形、肤色和年龄层与正面完全一致；中性表情、平视、均匀光、简单背景，输出单张可审核头部图。」目标 `assets/characters/CH08/head-right-profile-v1.png`；附加共用负面约束。

### 全身正面

- **CH08-body-front-v1.png：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）。编辑提示词：「以已批准的陈芸正面脸为唯一身份，补足同一成年人物的中性全身正面站姿；脸、头发与颈肩关系保持一致，手脚完整、自然比例、双臂自然垂放。只穿不带特定朝代纹样的素色基础内层，服装不定义正式造型；均匀中性光、简单背景，人物从头到脚完整入画。」目标 `assets/characters/CH08/body-front-v1.png`；附加共用负面约束。审核通过后才派生下列五视图。

### 全身其他视图

- **CH08-body-left45-v1.png｜左前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陈芸人物和体态基础上，人物与身体整体向左转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH08/body-left45-v1.png`；附加共用负面约束。
- **CH08-body-left-v1.png｜左侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陈芸人物和体态基础上，人物与身体整体向左转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH08/body-left-v1.png`；附加共用负面约束。
- **CH08-body-back-v1.png｜背面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陈芸人物和体态基础上，人物背向观察者，保持身高、肩宽、体态和发型背部轮廓；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH08/body-back-v1.png`；附加共用负面约束。
- **CH08-body-right-v1.png｜右侧面：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陈芸人物和体态基础上，人物与身体整体向右转九十度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH08/body-right-v1.png`；附加共用负面约束。
- **CH08-body-right45-v1.png｜右前45°：** 同时上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）与 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY / EDIT TARGET）。编辑提示词：「在同一陈芸人物和体态基础上，人物与身体整体向右转四十五度；脸部可见时必须延续正面母图，身体比例、肩宽、四肢长度、手脚数量、素色内层和发型轮廓保持完全一致。只改变视角与自然遮挡，不改变人物身份或服装结构；全身完整，均匀中性光、简单背景。」目标 `assets/characters/CH08/body-right45-v1.png`；附加共用负面约束。

**CH08 审核：** 十一张原图按文件名核对同一身份；尤其左右侧面不应成为两个人，背面体态需与正面尺寸一致。失败角度只重做该角度，保留已通过母图。

## 回传与下一步

每张保存到相应 `assets/characters/<Asset ID>/`，或上传时按 `<Asset ID>-<file-name>` 命名。先回传八张正面脸供审核；审核通过后可依本包继续各自的头部和全身视图。任何 Contact Sheet 只作顺序比较，不能代替独立原图。正式服装及组合定妆见总交接目录，不由本包临时发挥。
