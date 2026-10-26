# Stage 08｜全部独立资产生图提示词（用户生成合订本）

**状态：USER_GENERATE / NOT GENERATED。** 本文件按下列六份源提示词自动汇总，方便在一个文件里顺序复制；若源文件后续修订，应重新汇总，不在这里单独改写。历史人物外貌与具体场面属于视觉重构。

**先做：** 八张人物正脸与四张无人场景主视图；回传审核通过后，再按母图派生人物、场景、服装和道具视图。每张图保留 Asset ID 和指定文件名。此合订本只包含 Stage 08 静态资产词，不包含尚未通过 G3/G4 的分镜或图生视频执行词。

---

<!-- SOURCE: user-generation-handoff-v1.md -->

# Stage 08｜用户自行生图总交接 v1

**Project ID：** FPD-20261002-他们把爱写进了千年  
**模式：** USER_GENERATE（用户 2026-10-03 已选择）  
**范围：** G2 已通过的爱情短片八场，**只生成独立静态资产**。此包没有镜头图、分镜图或视频生成指令。  
**当前状态：** 所有独立资产 `PLANNED / NOT GENERATED`；G3 未通过。

## 你要打开的提示词包

| 顺序 | 文件 | 内容 | 先决母图 |
|---|---|---|---|
| 1 | [FA-01 正面身份锚点](face-anchor-batch-01.md) | CH01–08 各一张独立正脸 | 旧分镜仅作人物外观方向 |
| 1 | [LOC-MV-01 场景多角度](location-multiview-v1.md) | LOC01–04 各一张无人主视图，再左/右约 30° 与细节板 | 先旧分镜可见结构；左右角度必须上传通过审核的主视图 |
| 2 | [CH-MV-01 人物多角度](character-multiview-v1.md) | 八人头部五角度、全身六视图，每角度独立 PNG | 各人的已审核正脸与全身正面 |
| 2 | [PROP-01 道具状态](prop-state-v1.md) | 碑拓、书、折信、双碗与其必要状态 | 各道具基础图通过后再编辑派生状态 |
| 3 | [CST-LOOK-01 服装与组合多角度](costume-combined-multiview-v1.md) | 八套独立服装正/侧/背；八人穿着组合六视图 | 各人的脸/体态和对应独立服装先通过 |

## 生成顺序与停点

1. **第一轮原计划 12 张母图：** CH01/CH02 的 `canon-face-front-v2.png` 已通过正脸审核；CH03/CH04 正脸候选需按 `CH03-CH04-face-framing-repair-v1.md` 扩图；CH05–CH08 正脸四张与 LOC01–LOC04 无人主视四张仍待回传。CH01/CH02 可从 v2 派生头部角度，其他人物和场景仍按各自母图审核结果推进。
2. **我审核真实原图：** 看脸是否对应旧视觉方向、人物是否可区分；看每处空间固定锚点的位置和可见拓扑。只要有一张失败，就只改那张，不把整批重抽。
3. **第二轮再派生：** 人物左右 45°/侧面、全身正面及五视图；场景左右约 30°与材料板；独立道具基础/状态。**每个角度都上传同一人的已批准身份图或同一处的已批准空间主图。**
4. **第三轮再组合服装：** 独立服装三视图通过后，上传角色脸、体态与服装，派生穿着组合六视图。组合图不能反向修改人物和服装源图。
5. **回传审核：** 发送图片时保留 Asset ID 和视角/状态名。所有 P0 的独立原图逐张通过后才可以登记 G3；其后才更新新剧本动作对应的正式分镜。

## 每个资产的文件归属

| 类型 | 目标目录与命名例子 | 关键一致性 |
|---|---|---|
| 人物 | `assets/characters/CH01/canon-face-front-v2.png`、`head-left45-v1.png`、`body-right-v1.png`、`combined-CST01-left45-v1.png` | 正脸为唯一身份母图；全身正面为体态母图；服装不得改脸 |
| 服装 | `assets/costumes/CST01/front-v1.png`、`side-v1.png`、`back-v1.png` | 层数、领袖、系结、色彩与材料一致 |
| 场景 | `assets/locations/LOC01/topology-main-v1.png`、`view-left30-v1.png`、`view-right30-v1.png` | 三维固定锚点不移动、不镜像；不从纯文字重抽另一间房 |
| 道具 | `assets/props/PROP01/flat-v1.png`、`corner-curled-v1.png` | 基础身份、尺寸、材料和变化位置稳定 |

如果在外部网页工具中生成，使用相同会话上传对应母图，选择**参考图编辑/图生图**，每个视角单独导出。可直接把图片上传到本聊天；我会按文件名归档并做真实像素审核。若自行放入目录，务必使用表中的准确 Asset ID 和文件名。生成工具若只支持纯文字出图，就先完成第一轮母图；后续多角度一致性需要能上传母图编辑的入口。

## 审核时比对的内容

- **人物：** 正、左右角度的眼距、鼻梁、下颌、耳朵、发际与体态；是否是同一个人。左右不能简单镜像成结构错误；所有人物手脚数量正常。
- **服装：** 正侧背的层数、袖口、衣摆、系结、织物和颜色；与组合图一致。
- **场景：** 主/左/右三个角度的书案、椅子、窗、灯、石径、园门和饭桌固定位置；透视变化可解释，无突然出现的门或换房。
- **道具：** 同一纸角、同一书页、同一折信、同一双碗；数量和持用尺度正确。
- **历史边界：** 这些图是以史料人物为题的视觉重构，不作为真人肖像、真实故居或考据服饰的证据。

## 状态

现有旧分镜获认可的是整体画面方向。CH01/CH02 的正脸 v2 已通过 AI 自审，但整项人物资产及 G3 仍待完成。后续图片按 `../asset-manifest.md` 和各 Asset ID 合同逐张审核、登记，再继续多角度派生。视频仍不在本次范围。


---


<!-- SOURCE: face-anchor-batch-01.md -->

# FA-01｜八位人物正面身份锚点候选图提示词

- **状态：** USER_GENERATE / HANDOFF READY / NOT GENERATED。用户于 2026-10-03 选择自行生图；Stage 08 首批只做独立人物正脸候选。
- **源合同：** `../asset-manifest.md` v3、`../../visual-development/world-visual-bible.md` v3、G2 通过的 `../../screenplay/screenplay.fountain` v3。
- **批次目标：** 八张单人、正面、平视、无表情的身份图；一张一人，不要合照或九宫格。真实历史外貌无证据，图像只用于本片戏剧化重构。
- **参考语义：** 各自旧分镜帧仅承担 `IDENTITY` 临时外观线索，**不**承担戏服、历史真实性、场景、灯光或动作；生成出的候选仍须逐张审核才能成为 Canon Face。
- **执行顺序：** CH01–08 可分别创建候选；任何头部角度、全身图和组合定妆，须等相应正脸候选通过后再派生。
- **共同验收：** 脸部无遮挡、面容唯一、正面比例自然；无多余人物、异常眼耳牙、文字和水印；与参考中指定人物的外观方向可辨，但不复制参考构图。

## CH01｜李清照

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH01/canon-face-front-v2.png`（回传时用 `CH01-canon-face-front-v1.png`）
- **参考图 R-CH01：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao/S01-start-v1.png`；仅参考**左侧女子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的李清照（成年女性）建立一张独立人物身份候选图。参考 R-CH01 中左侧女子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为李清照；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH01 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH02｜赵明诚

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH02/canon-face-front-v2.png`（回传时用 `CH02-canon-face-front-v1.png`）
- **参考图 R-CH02：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao/S01-start-v1.png`；仅参考**右侧男子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的赵明诚（成年男性）建立一张独立人物身份候选图。参考 R-CH02 中右侧男子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为赵明诚；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH02 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH03｜苏轼

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH03/canon-face-front-v1.png`（回传时用 `CH03-canon-face-front-v1.png`）
- **参考图 R-CH03：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang/S03-start-v1.png`；仅参考**左侧男子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的苏轼（成年男性）建立一张独立人物身份候选图。参考 R-CH03 中左侧男子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为苏轼；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH03 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH04｜王弗

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH04/canon-face-front-v1.png`（回传时用 `CH04-canon-face-front-v1.png`）
- **参考图 R-CH04：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang/S03-start-v1.png`；仅参考**右侧女子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的王弗（成年女性）建立一张独立人物身份候选图。参考 R-CH04 中右侧女子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为王弗；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH04 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH05｜陆游

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH05/canon-face-front-v1.png`（回传时用 `CH05-canon-face-front-v1.png`）
- **参考图 R-CH05：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang/S05-start-v1.png`；仅参考**右侧男子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的陆游（成年男性）建立一张独立人物身份候选图。参考 R-CH05 中右侧男子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为陆游；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH05 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH06｜唐氏

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH06/canon-face-front-v1.png`（回传时用 `CH06-canon-face-front-v1.png`）
- **参考图 R-CH06：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang/S05-start-v1.png`；仅参考**左侧女子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的唐氏（成年女性）建立一张独立人物身份候选图。参考 R-CH06 中左侧女子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为唐氏；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH06 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH07｜沈复

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH07/canon-face-front-v1.png`（回传时用 `CH07-canon-face-front-v1.png`）
- **参考图 R-CH07：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen/S07-start-v1.png`；仅参考**左侧男子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的沈复（成年男性）建立一张独立人物身份候选图。参考 R-CH07 中左侧男子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为沈复；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH07 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## CH08｜陈芸

- **操作：** CREATE NEW
- **目标文件名：** `assets/characters/CH08/canon-face-front-v1.png`（回传时用 `CH08-canon-face-front-v1.png`）
- **参考图 R-CH08：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen/S07-start-v1.png`；仅参考**右侧女子**的面部整体感觉，角色为 `IDENTITY / provisional`。忽略图中另一人、姿势、服装、房间、光线与叙事动作。
- **正向提示词：** 为短片《他们把爱，写进了千年》的陈芸（成年女性）建立一张独立人物身份候选图。参考 R-CH08 中右侧女子的面部比例、发际轮廓和眉眼鼻口关系，转为清楚可审核的单人正面脸部近照。人物平视、头部端正、表情中性、嘴闭合、五官无遮挡；皮肤保留自然局部差异，头发真实有层次。均匀中性照明，纯净低干扰背景，普通素色内层衣领只作为边缘，不定义正式戏服。画面只出现这一人，面容完整，方便之后从这张身份图派生其他视角。这是创作角色视觉设计，不宣称历史真人肖像。
- **负面约束：** 不要第二个人、合照、九宫格、镜头表演、说话口型、笑或哭、歪头、侧脸、遮脸、强烈暖冷戏剧灯、浅景深遮五官、复杂背景、书案道具、可读文字、水印、塑料皮肤、异常眼耳牙、额外肢体；不要从参考图复制服装或历史准确性声明。
- **保持不变：** 角色身份为陈芸；只继承指定人物的外观方向和单人面部关系。**变动：** 从旧分镜的双人叙事图改为中性正面身份候选。
- **验收点：** 可与 R-CH08 的指定人物对应；脸部无遮挡且比例自然；可作为后续同一人物头部角度的唯一派生母图。

## 交接方式

用户已选择 `USER_GENERATE`：按以上编号在外部工具生成，先上传八张正面脸或放入对应 `assets/characters/<Asset ID>/` 目录。收到后逐张审核真实像素、更新合同与 manifest；只有通过的正脸才用于 `character-multiview-v1.md` 的角度派生。未通过的只返工失败项。


---


<!-- SOURCE: location-multiview-v1.md -->

# LOC-MV-01｜四处场景多角度空间图交接包

**模式：USER_GENERATE / NOT GENERATED。** 场景三角度必须源自同一张已审核的无人主视图，不能对同一文字提示词独立抽三次。每张保存为独立原图，不用一张合成九宫格充数。

## 顺序和参考职责

1. 先使用各组旧分镜帧作为 `TOPOLOGY / provisional`，**编辑去除人物和可移动道具**，生成无人空间 `topology-main-v1.png`。旧图只是前方可见范围的方向参考；本项目空间为创作设计，不宣称真实故居。
2. 逐张核对书案/椅/园门/桌子的固定位置。通过后，上传同一张 `topology-main-v1.png`，派生同一侧观察区域的左约 30°、右约 30°。两张角度图不得镜像翻转、移动窗门或换房。
3. 不生成凭空想象的完整背向视图。若 Stage 09–10 真要拍反打，再补完整空间拓扑后生成；当前三角度已覆盖用户要求的多角度一致性。
4. 当前空间图均无人物、服装、核心可移动道具、字幕和可读文字。角色与道具在批准独立源图后再组合。
5. 如模型不能带母图编辑改变观察角度，请先回传主视图让我检查结构；不要用纯文本重抽“同一个”场景。

**共同负面约束（各条均附加）：** 不要人物、手、碗、书页、信、碑拓、字幕、可读汉字、水印、品牌、雾、烟、无来源花瓣、戏剧光晕；不要镜像翻转、改变固定家具和窗门位置、凭空添加门廊或额外房间、把木/石材质做成塑料、把所有表面均匀做旧。

## LOC01｜李赵书房

**空间锚点（创作设计，待主视图审核）：** 主视图中书案横置中部，后方左侧为书架，后方右侧为格窗，桌侧固定一盏灯；李清照原位在主视图左，赵明诚原位在右，后场右侧位置必须空出来。
**固定要素：** 书案长轴、书架、格窗、灯位和桌面磨痕。
**材料验收：** 木案边缘因手臂摩擦略有局部光泽，窗棂接缝可见；不平均做旧。

### LOC01-A｜无人主视图

- **操作：** EDIT FROM 旧分镜参考；**输入 R-LOC01：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao/S01-start-v1.png`，角色仅为 `TOPOLOGY / provisional`，不可从其中继承人物、服装或历史真实性。
- **目标：** `assets/locations/LOC01/topology-main-v1.png`（回传名 `LOC01-topology-main-v1.png`）。
- **正向提示词：** 「把参考图 R-LOC01 改成可供多角度派生的李赵书房无人空间主视图。主视图中书案横置中部，后方左侧为书架，后方右侧为格窗，桌侧固定一盏灯；李清照原位在主视图左，赵明诚原位在右，后场右侧位置必须空出来。 保留书案长轴、书架、格窗、灯位和桌面磨痕的相对位置、尺度和朝向，移除人物以及书页、信件、碗等可移动道具。空间材料真实可辨：木案边缘因手臂摩擦略有局部光泽，窗棂接缝可见；不平均做旧 使用均匀、可辨结构的中性基础光，不加入后来场景的情绪调色。只呈现当前可见空间，不发明未见的背墙或门外路径。」
- **负面约束：** 附加共同负面约束。
- **验收：** 与旧图的固定空间锚点同源；无人无核心道具；可作为左右角度唯一空间母图。

### LOC01-B/C｜由主视图派生左右角度

- **LOC01-B left30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC01\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC01 仅作为原始空间方向证据。目标 `assets/locations/LOC01/view-left30-v1.png`。编辑提示词：「在同一个李赵书房内，从主视图位置向左沿同一侧移动约三十度观察；主视图中书案横置中部，后方左侧为书架，后方右侧为格窗，桌侧固定一盏灯；李清照原位在主视图左，赵明诚原位在右，后场右侧位置必须空出来。 保持书案长轴、书架、格窗、灯位和桌面磨痕在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木案边缘因手臂摩擦略有局部光泽，窗棂接缝可见；不平均做旧」附加共同负面约束。
- **LOC01-C right30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC01\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC01 仅作为原始空间方向证据。目标 `assets/locations/LOC01/view-right30-v1.png`。编辑提示词：「在同一个李赵书房内，从主视图位置向右沿同一侧移动约三十度观察；主视图中书案横置中部，后方左侧为书架，后方右侧为格窗，桌侧固定一盏灯；李清照原位在主视图左，赵明诚原位在右，后场右侧位置必须空出来。 保持书案长轴、书架、格窗、灯位和桌面磨痕在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木案边缘因手臂摩擦略有局部光泽，窗棂接缝可见；不平均做旧」附加共同负面约束。

### LOC01-D｜结构/材料细节板

- **目标：** `assets/locations/LOC01/detail-surface-v1.png`；上传已审核主视图（`MATERIAL / TOPOLOGY`）。
- **正向提示词：** 「从同一李赵书房的主视图中提取固定结构近观察距离的材料细节，保持书案长轴、书架、格窗、灯位和桌面磨痕相符；重点展示：木案边缘因手臂摩擦略有局部光泽，窗棂接缝可见；不平均做旧 不加入人物、可移动道具、泛化纹样或新的结构。」附加共同负面约束。
- **验收：** 材料纹理和固定锚点与三张空间图一致。

**LOC01 顺序审核：** 并排比较主、左、右三张：桌/路径轴线、窗/门、灯/假山、固定磨痕应能解释为同一空间的视差；若错误，只重做失败视角，不替换已批准主视图。

## LOC02｜苏王书房

**空间锚点（创作设计，待主视图审核）：** 主视图中桌面横置，苏轼位于主视图左，王弗的椅位在右；后方可辨书架和右侧格窗，桌右侧为固定灯位。书页将来铺在桌中央，但当前无人物无书。
**固定要素：** 桌子、王弗椅位、书架、格窗和灯位。
**材料验收：** 木桌边缘、椅脚和窗棂有使用差异；纸物不在空间原图内。

### LOC02-A｜无人主视图

- **操作：** EDIT FROM 旧分镜参考；**输入 R-LOC02：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang/S03-start-v1.png`，角色仅为 `TOPOLOGY / provisional`，不可从其中继承人物、服装或历史真实性。
- **目标：** `assets/locations/LOC02/topology-main-v1.png`（回传名 `LOC02-topology-main-v1.png`）。
- **正向提示词：** 「把参考图 R-LOC02 改成可供多角度派生的苏王书房无人空间主视图。主视图中桌面横置，苏轼位于主视图左，王弗的椅位在右；后方可辨书架和右侧格窗，桌右侧为固定灯位。书页将来铺在桌中央，但当前无人物无书。 保留桌子、王弗椅位、书架、格窗和灯位的相对位置、尺度和朝向，移除人物以及书页、信件、碗等可移动道具。空间材料真实可辨：木桌边缘、椅脚和窗棂有使用差异；纸物不在空间原图内 使用均匀、可辨结构的中性基础光，不加入后来场景的情绪调色。只呈现当前可见空间，不发明未见的背墙或门外路径。」
- **负面约束：** 附加共同负面约束。
- **验收：** 与旧图的固定空间锚点同源；无人无核心道具；可作为左右角度唯一空间母图。

### LOC02-B/C｜由主视图派生左右角度

- **LOC02-B left30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC02\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC02 仅作为原始空间方向证据。目标 `assets/locations/LOC02/view-left30-v1.png`。编辑提示词：「在同一个苏王书房内，从主视图位置向左沿同一侧移动约三十度观察；主视图中桌面横置，苏轼位于主视图左，王弗的椅位在右；后方可辨书架和右侧格窗，桌右侧为固定灯位。书页将来铺在桌中央，但当前无人物无书。 保持桌子、王弗椅位、书架、格窗和灯位在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木桌边缘、椅脚和窗棂有使用差异；纸物不在空间原图内」附加共同负面约束。
- **LOC02-C right30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC02\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC02 仅作为原始空间方向证据。目标 `assets/locations/LOC02/view-right30-v1.png`。编辑提示词：「在同一个苏王书房内，从主视图位置向右沿同一侧移动约三十度观察；主视图中桌面横置，苏轼位于主视图左，王弗的椅位在右；后方可辨书架和右侧格窗，桌右侧为固定灯位。书页将来铺在桌中央，但当前无人物无书。 保持桌子、王弗椅位、书架、格窗和灯位在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木桌边缘、椅脚和窗棂有使用差异；纸物不在空间原图内」附加共同负面约束。

### LOC02-D｜结构/材料细节板

- **目标：** `assets/locations/LOC02/detail-surface-v1.png`；上传已审核主视图（`MATERIAL / TOPOLOGY`）。
- **正向提示词：** 「从同一苏王书房的主视图中提取固定结构近观察距离的材料细节，保持桌子、王弗椅位、书架、格窗和灯位相符；重点展示：木桌边缘、椅脚和窗棂有使用差异；纸物不在空间原图内 不加入人物、可移动道具、泛化纹样或新的结构。」附加共同负面约束。
- **验收：** 材料纹理和固定锚点与三张空间图一致。

**LOC02 顺序审核：** 并排比较主、左、右三张：桌/路径轴线、窗/门、灯/假山、固定磨痕应能解释为同一空间的视差；若错误，只重做失败视角，不替换已批准主视图。

## LOC03｜春园石径

**空间锚点（创作设计，待主视图审核）：** 主视图中石径从前方向后方园门延伸，假山石位于路径左侧，桃枝从上方偏左伸入；同一路段有足够空间让陆游回身伸手。
**固定要素：** 石径走向、石缝、左侧假山石、远处园门和桃枝主干。
**材料验收：** 石径接缝与行走磨损有局部差异，枝叶自然生长；没有均匀铺满的花瓣。

### LOC03-A｜无人主视图

- **操作：** EDIT FROM 旧分镜参考；**输入 R-LOC03：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang/S05-start-v1.png`，角色仅为 `TOPOLOGY / provisional`，不可从其中继承人物、服装或历史真实性。
- **目标：** `assets/locations/LOC03/topology-main-v1.png`（回传名 `LOC03-topology-main-v1.png`）。
- **正向提示词：** 「把参考图 R-LOC03 改成可供多角度派生的春园石径无人空间主视图。主视图中石径从前方向后方园门延伸，假山石位于路径左侧，桃枝从上方偏左伸入；同一路段有足够空间让陆游回身伸手。 保留石径走向、石缝、左侧假山石、远处园门和桃枝主干的相对位置、尺度和朝向，移除人物以及书页、信件、碗等可移动道具。空间材料真实可辨：石径接缝与行走磨损有局部差异，枝叶自然生长；没有均匀铺满的花瓣 使用均匀、可辨结构的中性基础光，不加入后来场景的情绪调色。只呈现当前可见空间，不发明未见的背墙或门外路径。」
- **负面约束：** 附加共同负面约束。
- **验收：** 与旧图的固定空间锚点同源；无人无核心道具；可作为左右角度唯一空间母图。

### LOC03-B/C｜由主视图派生左右角度

- **LOC03-B left30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC03\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC03 仅作为原始空间方向证据。目标 `assets/locations/LOC03/view-left30-v1.png`。编辑提示词：「在同一个春园石径内，从主视图位置向左沿同一侧移动约三十度观察；主视图中石径从前方向后方园门延伸，假山石位于路径左侧，桃枝从上方偏左伸入；同一路段有足够空间让陆游回身伸手。 保持石径走向、石缝、左侧假山石、远处园门和桃枝主干在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。石径接缝与行走磨损有局部差异，枝叶自然生长；没有均匀铺满的花瓣」附加共同负面约束。
- **LOC03-C right30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC03\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC03 仅作为原始空间方向证据。目标 `assets/locations/LOC03/view-right30-v1.png`。编辑提示词：「在同一个春园石径内，从主视图位置向右沿同一侧移动约三十度观察；主视图中石径从前方向后方园门延伸，假山石位于路径左侧，桃枝从上方偏左伸入；同一路段有足够空间让陆游回身伸手。 保持石径走向、石缝、左侧假山石、远处园门和桃枝主干在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。石径接缝与行走磨损有局部差异，枝叶自然生长；没有均匀铺满的花瓣」附加共同负面约束。

### LOC03-D｜结构/材料细节板

- **目标：** `assets/locations/LOC03/detail-surface-v1.png`；上传已审核主视图（`MATERIAL / TOPOLOGY`）。
- **正向提示词：** 「从同一春园石径的主视图中提取固定结构近观察距离的材料细节，保持石径走向、石缝、左侧假山石、远处园门和桃枝主干相符；重点展示：石径接缝与行走磨损有局部差异，枝叶自然生长；没有均匀铺满的花瓣 不加入人物、可移动道具、泛化纹样或新的结构。」附加共同负面约束。
- **验收：** 材料纹理和固定锚点与三张空间图一致。

**LOC03 顺序审核：** 并排比较主、左、右三张：桌/路径轴线、窗/门、灯/假山、固定磨痕应能解释为同一空间的视差；若错误，只重做失败视角，不替换已批准主视图。

## LOC04｜沈陈居所

**空间锚点（创作设计，待主视图审核）：** 主视图中木饭桌横贯中部，沈复坐席在左、陈芸坐席在右；后方格窗、固定灯位和桌边木纹保持一致。桌面将来放双碗，但当前无人无碗。
**固定要素：** 桌长轴、左右坐席、背后格窗、灯位和桌面局部磨痕。
**材料验收：** 木桌板缝、常碰触的近侧桌缘局部更亮，陶碗由独立道具资产提供。

### LOC04-A｜无人主视图

- **操作：** EDIT FROM 旧分镜参考；**输入 R-LOC04：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen/S07-start-v1.png`，角色仅为 `TOPOLOGY / provisional`，不可从其中继承人物、服装或历史真实性。
- **目标：** `assets/locations/LOC04/topology-main-v1.png`（回传名 `LOC04-topology-main-v1.png`）。
- **正向提示词：** 「把参考图 R-LOC04 改成可供多角度派生的沈陈居所无人空间主视图。主视图中木饭桌横贯中部，沈复坐席在左、陈芸坐席在右；后方格窗、固定灯位和桌边木纹保持一致。桌面将来放双碗，但当前无人无碗。 保留桌长轴、左右坐席、背后格窗、灯位和桌面局部磨痕的相对位置、尺度和朝向，移除人物以及书页、信件、碗等可移动道具。空间材料真实可辨：木桌板缝、常碰触的近侧桌缘局部更亮，陶碗由独立道具资产提供 使用均匀、可辨结构的中性基础光，不加入后来场景的情绪调色。只呈现当前可见空间，不发明未见的背墙或门外路径。」
- **负面约束：** 附加共同负面约束。
- **验收：** 与旧图的固定空间锚点同源；无人无核心道具；可作为左右角度唯一空间母图。

### LOC04-B/C｜由主视图派生左右角度

- **LOC04-B left30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC04\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC04 仅作为原始空间方向证据。目标 `assets/locations/LOC04/view-left30-v1.png`。编辑提示词：「在同一个沈陈居所内，从主视图位置向左沿同一侧移动约三十度观察；主视图中木饭桌横贯中部，沈复坐席在左、陈芸坐席在右；后方格窗、固定灯位和桌边木纹保持一致。桌面将来放双碗，但当前无人无碗。 保持桌长轴、左右坐席、背后格窗、灯位和桌面局部磨痕在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木桌板缝、常碰触的近侧桌缘局部更亮，陶碗由独立道具资产提供」附加共同负面约束。
- **LOC04-C right30：** 上传已审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\locations\LOC04\topology-main-v1.png`（`TOPOLOGY / EDIT TARGET`），必要时附 R-LOC04 仅作为原始空间方向证据。目标 `assets/locations/LOC04/view-right30-v1.png`。编辑提示词：「在同一个沈陈居所内，从主视图位置向右沿同一侧移动约三十度观察；主视图中木饭桌横贯中部，沈复坐席在左、陈芸坐席在右；后方格窗、固定灯位和桌边木纹保持一致。桌面将来放双碗，但当前无人无碗。 保持桌长轴、左右坐席、背后格窗、灯位和桌面局部磨痕在三维空间中的固定相互位置，透视和遮挡随视点真实变化，但不镜像、不搬动桌椅、窗门、假山或灯位。仍是无人物、无核心可移动道具、中性基础光的同一场景。木桌板缝、常碰触的近侧桌缘局部更亮，陶碗由独立道具资产提供」附加共同负面约束。

### LOC04-D｜结构/材料细节板

- **目标：** `assets/locations/LOC04/detail-surface-v1.png`；上传已审核主视图（`MATERIAL / TOPOLOGY`）。
- **正向提示词：** 「从同一沈陈居所的主视图中提取固定结构近观察距离的材料细节，保持桌长轴、左右坐席、背后格窗、灯位和桌面局部磨痕相符；重点展示：木桌板缝、常碰触的近侧桌缘局部更亮，陶碗由独立道具资产提供 不加入人物、可移动道具、泛化纹样或新的结构。」附加共同负面约束。
- **验收：** 材料纹理和固定锚点与三张空间图一致。

**LOC04 顺序审核：** 并排比较主、左、右三张：桌/路径轴线、窗/门、灯/假山、固定磨痕应能解释为同一空间的视差；若错误，只重做失败视角，不替换已批准主视图。

## 回传

先回传四张 `topology-main-v1.png`。我查看真实图片并登记通过/返工后，你再据此生成左右角度和细节板。即使你在一个模型会话里工作，每个场景的母图也要独立命名；不要混用 LOC01 和 LOC02 两间书房。



---


<!-- SOURCE: character-multiview-v1.md -->

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



---


<!-- SOURCE: prop-state-v1.md -->

# PROP-01｜四组关键道具与状态图

**模式：USER_GENERATE / NOT GENERATED。** 这些是独立道具图，不是镜头图。先批准每件基础道具，再用原图编辑派生状态。道具位置和手部接触在后续分镜阶段组合检查。

**共同负面约束（每条附加）：** 不要人物、手、完整房间、镜头级构图、可读汉字、现代印刷字体、品牌、水印、塑料材质、多出一件道具、无因磨损或夸张光晕。中性光、纯净背景；保持实物可制造的尺度。

**旧图参考文件（只提供材料或尺度线索，不是道具 Canon）：**

| 道具 | 需要上传的旧图绝对路径 |
|---|---|
| PROP01 | `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao\S01-start-v1.png` |
| PROP02 | `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang\S03-start-v1.png` |
| PROP03 | `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang\S06-start-v1.png` |
| PROP04 | `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen\S07-start-v1.png` |

## PROP01｜碑拓

- **基础图 CREATE NEW：** 目标 `assets/props/PROP01/flat-v1.png`。参考 `../../storyboard/frames/F01-li-zhao/S01-start-v1.png` 仅为 `MATERIAL / SCALE provisional`，忽略人物和书房。提示词：「独立的纸质碑拓资产，平铺在中性背景的平面上；纸有厚度、纤维、真实边缘和轻微自然旧痕，约可由两人同桌查看的尺度。表面仅有不可辨的墨色拓印纹理，不生成可读汉字或完整碑文。均匀中性光，无人物、无书案。」附加共同负面约束。
- **卷角态 EDIT FROM：** 上传已批准 `assets/props/PROP01/flat-v1.png`（`EDIT TARGET / MATERIAL`），目标 `assets/props/PROP01/corner-curled-v1.png`。提示词：「同一张碑拓纸，只让主视图固定的右侧同一纸角自然向上卷起，纸面其余尺寸、纹理和墨痕位置不变；卷曲具有纸张回弹，适合手指按平。无手和人物。」附加共同负面约束。
- **验收：** 平展与卷角必须是同一张纸，同角位置一致；S001/S002 的手可以触到该角。

## PROP02｜摊开的书

- **基础图 CREATE NEW：** 目标 `assets/props/PROP02/open-page-v1.png`。参考 `../../storyboard/frames/F02-su-wang/S03-start-v1.png` 仅为 `MATERIAL / SCALE provisional`。提示词：「独立的摊开书册资产，放在中性平面上；保持一组固定的左右书页和书脊，纸张有厚度、自然微弯与局部翻阅痕迹。右页中部留出可供手指指向的固定区域，用不构成可读文字的淡墨纹理表示书写质感；均匀中性光，无人物、无桌边杂物。」附加共同负面约束。
- **指定行状态 EDIT FROM：** 上传已批准 `assets/props/PROP02/open-page-v1.png`（`EDIT TARGET`），目标 `assets/props/PROP02/line-marker-v1.png`。提示词：「同一本打开的书，页面、书脊、边角完全不变；只用极轻的无字位置标记表明右页中部同一行供后续指尖定位，标记不作为最终画面可见文字。无手和人物。」附加共同负面约束。
- **验收：** 书页方向和指定区域前后不换页，不出现虚构可读原文。

## PROP03｜折信

- **基础图 CREATE NEW：** 目标 `assets/props/PROP03/folded-v1.png`。参考 `../../storyboard/frames/F03-lu-tang/S06-start-v1.png` 仅为 `SCALE provisional`。提示词：「独立的未展开折叠纸信，一人单手可持的尺度；折线、纸厚、边缘和局部持握压痕可信，表面没有可读文字、封印或专属历史事件暗示。中性光、简单背景，不出现手、人物或园路。」附加共同负面约束。
- **验收：** 只有一封折信；陆游可一手持有，另一只手可回身伸出；不得宣传为真实未寄信。

## PROP04｜双碗、筷与菜

- **基础图 CREATE NEW：** 目标 `assets/props/PROP04/two-bowls-v1.png`。参考 `../../storyboard/frames/F04-shen-chen/S07-start-v1.png` 仅为 `SCALE / MATERIAL provisional`。提示词：「独立的日常饭桌道具组：两只材质、口沿和尺寸一致的陶瓷饭碗，配一双筷子和少量普通菜食；两只碗在固定的左右位置，左碗可承接一口菜，右碗可被清空。陶瓷有重量与柔和局部反射，筷子能夹住食物；中性背景，不出现人物或整间屋。」附加共同负面约束。
- **空碗状态 EDIT FROM：** 上传已批准 `assets/props/PROP04/two-bowls-v1.png`（`EDIT TARGET / MATERIAL`），目标 `assets/props/PROP04/opposite-empty-v1.png`。提示词：「保持同一双碗的材质、口沿、尺寸与左右摆位；让主视图右侧对面碗为空，左碗仍有少量菜，筷子位置可为后续沈复持起留出空间。不得移动碗、更换材质或减少碗数。」附加共同负面约束。
- **验收：** S007/S008 始终两碗；右侧对面碗空；筷子与菜的尺度可供夹取。最终左右归属以批准的 LOC04 主视图为准。

## 回传

将每件基础图放入 `assets/props/<PROP ID>/`，先回传审核；通过后再派生状态图。上传时使用 `PROP01-flat-v1.png` 等含 ID 的文件名，避免四组道具混淆。

## 材料细节板（基础图通过后再做）

- **PROP01-detail-paper-v1.png：** 上传已批准 `assets/props/PROP01/flat-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一碑拓提取纸角与纸面的近观察材料板，保持纸纤维、厚度、墨痕分布和同一角的位置；展示可以卷起又按平的边缘结构。无手、无人物、无可读汉字。」目标 `assets/props/PROP01/detail-paper-v1.png`；附加共同负面约束。
- **PROP02-detail-page-v1.png：** 上传已批准 `assets/props/PROP02/open-page-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一本打开书册提取指定页的纸张、书脊与边缘材料板；保持原本页方向、厚度和翻阅磨痕，不新增可读文字或换页。」目标 `assets/props/PROP02/detail-page-v1.png`；附加共同负面约束。
- **PROP03-detail-fold-v1.png：** 上传已批准 `assets/props/PROP03/folded-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一封未展折信提取折线、纸厚和边缘压痕的材料板；保持折叠方式和一手可持尺度，不展开、不加封印或可读字。」目标 `assets/props/PROP03/detail-fold-v1.png`；附加共同负面约束。
- **PROP04-detail-ceramic-v1.png：** 上传已批准 `assets/props/PROP04/two-bowls-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一组两只陶瓷碗和筷子提取碗口、釉面、碗底接触和筷尖材料板；两碗材质与尺寸一致，局部反光柔和，食物尺度可信，不改碗数或左右归属。」目标 `assets/props/PROP04/detail-ceramic-v1.png`；附加共同负面约束。


---


<!-- SOURCE: costume-combined-multiview-v1.md -->

# CST-LOOK-01｜独立服装与人物组合多角度图

**模式：USER_GENERATE / NOT GENERATED。** 用户明确要求人物多角度一致。先审人物正脸和体态，再审独立服装，最后做穿着该服装的组合六视图。服装设计只采用旧分镜的整体外观方向与朝代生活语境，**不是经过考据的历史复原**。

## 通用依赖和验收

- 每套服装的旧分镜只作 `WARDROBE / provisional`；不要继承其中的人脸、动作、场景或具体历史认证。
- 独立服装图不得出现真实人物面孔。先生成正面，再用同一正面衣装图编辑派生侧面、背面，锁定层数、领口、袖口、衣摆、系结位置、材料和颜色关系。
- 组合定妆的 `IDENTITY` 唯一来源是对应 CH 的已批准正脸；`BODY` 是已批准全身正面/角度；`WARDROBE` 是已批准独立服装正、侧、背原图。不得让服装参考图改脸。
- 每个角度存独立 PNG。任何组合图不替代 CH 和 CST 的独立资产。
- **通用负面约束（每条附加）：** 不要换脸、换体型、改变发际线、增减衣层、改色或换纹样；不要多人物、手脚畸形、服装与身体穿插、塑料织物、均匀脏污、舞台夸张配饰、文字、水印、品牌、镜头场景和戏剧光线。

## CST01｜李清照衣装

- **旧参考 R-CST01：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao/S01-start-v1.png`，只参考**左侧女子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 宋代生活语境、浅色、柔软多层衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST01/front-v1.png`。提示词：「为李清照设计一套独立服装资产，参考 R-CST01 中左侧女子的浅色、柔软多层衣装，放在无脸中性人台上展示完整正面。它属于宋代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST01 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST01 仅辅助颜色。目标 `assets/costumes/CST01/side-v1.png`。提示词：「把同一套李清照服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST01 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST01/back-v1.png`。提示词：「为同一套李清照服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH01/CST01 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH01/combined-CST01-front-v1.png`。提示词：「同一李清照人物，正面全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH01/CST01 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\combined-CST01-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH01/combined-CST01-left45-v1.png`。提示词：「同一李清照人物，左前45°全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH01/CST01 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\combined-CST01-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH01/combined-CST01-left-v1.png`。提示词：「同一李清照人物，左侧全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH01/CST01 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\combined-CST01-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH01/combined-CST01-back-v1.png`。提示词：「同一李清照人物，背面全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH01/CST01 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\combined-CST01-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH01/combined-CST01-right-v1.png`。提示词：「同一李清照人物，右侧全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH01/CST01 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST01\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH01\combined-CST01-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH01/combined-CST01-right45-v1.png`。提示词：「同一李清照人物，右前45°全身中性站姿；脸与体态严格继承 CH CH01，服装结构、层数、颜色、材料严格继承 CST CST01，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST01 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST02｜赵明诚衣装

- **旧参考 R-CST02：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F01-li-zhao/S01-start-v1.png`，只参考**右侧男子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 宋代生活语境、深色、稳重多层衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST02/front-v1.png`。提示词：「为赵明诚设计一套独立服装资产，参考 R-CST02 中右侧男子的深色、稳重多层衣装，放在无脸中性人台上展示完整正面。它属于宋代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST02 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST02 仅辅助颜色。目标 `assets/costumes/CST02/side-v1.png`。提示词：「把同一套赵明诚服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST02 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST02/back-v1.png`。提示词：「为同一套赵明诚服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH02/CST02 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH02/combined-CST02-front-v1.png`。提示词：「同一赵明诚人物，正面全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH02/CST02 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\combined-CST02-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH02/combined-CST02-left45-v1.png`。提示词：「同一赵明诚人物，左前45°全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH02/CST02 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\combined-CST02-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH02/combined-CST02-left-v1.png`。提示词：「同一赵明诚人物，左侧全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH02/CST02 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\combined-CST02-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH02/combined-CST02-back-v1.png`。提示词：「同一赵明诚人物，背面全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH02/CST02 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\combined-CST02-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH02/combined-CST02-right-v1.png`。提示词：「同一赵明诚人物，右侧全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH02/CST02 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\canon-face-front-v2.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST02\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH02\combined-CST02-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH02/combined-CST02-right45-v1.png`。提示词：「同一赵明诚人物，右前45°全身中性站姿；脸与体态严格继承 CH CH02，服装结构、层数、颜色、材料严格继承 CST CST02，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST02 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST03｜苏轼衣装

- **旧参考 R-CST03：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang/S03-start-v1.png`，只参考**左侧男子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 宋代生活语境、深色、宽松日常衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST03/front-v1.png`。提示词：「为苏轼设计一套独立服装资产，参考 R-CST03 中左侧男子的深色、宽松日常衣装，放在无脸中性人台上展示完整正面。它属于宋代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST03 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST03 仅辅助颜色。目标 `assets/costumes/CST03/side-v1.png`。提示词：「把同一套苏轼服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST03 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST03/back-v1.png`。提示词：「为同一套苏轼服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH03/CST03 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH03/combined-CST03-front-v1.png`。提示词：「同一苏轼人物，正面全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH03/CST03 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\combined-CST03-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH03/combined-CST03-left45-v1.png`。提示词：「同一苏轼人物，左前45°全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH03/CST03 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\combined-CST03-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH03/combined-CST03-left-v1.png`。提示词：「同一苏轼人物，左侧全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH03/CST03 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\combined-CST03-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH03/combined-CST03-back-v1.png`。提示词：「同一苏轼人物，背面全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH03/CST03 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\combined-CST03-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH03/combined-CST03-right-v1.png`。提示词：「同一苏轼人物，右侧全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH03/CST03 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST03\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH03\combined-CST03-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH03/combined-CST03-right45-v1.png`。提示词：「同一苏轼人物，右前45°全身中性站姿；脸与体态严格继承 CH CH03，服装结构、层数、颜色、材料严格继承 CST CST03，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST03 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST04｜王弗衣装

- **旧参考 R-CST04：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F02-su-wang/S03-start-v1.png`，只参考**右侧女子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 宋代生活语境、浅暖色、柔软多层衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST04/front-v1.png`。提示词：「为王弗设计一套独立服装资产，参考 R-CST04 中右侧女子的浅暖色、柔软多层衣装，放在无脸中性人台上展示完整正面。它属于宋代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST04 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST04 仅辅助颜色。目标 `assets/costumes/CST04/side-v1.png`。提示词：「把同一套王弗服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST04 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST04/back-v1.png`。提示词：「为同一套王弗服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH04/CST04 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH04/combined-CST04-front-v1.png`。提示词：「同一王弗人物，正面全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH04/CST04 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\combined-CST04-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH04/combined-CST04-left45-v1.png`。提示词：「同一王弗人物，左前45°全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH04/CST04 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\combined-CST04-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH04/combined-CST04-left-v1.png`。提示词：「同一王弗人物，左侧全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH04/CST04 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\combined-CST04-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH04/combined-CST04-back-v1.png`。提示词：「同一王弗人物，背面全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH04/CST04 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\combined-CST04-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH04/combined-CST04-right-v1.png`。提示词：「同一王弗人物，右侧全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH04/CST04 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST04\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH04\combined-CST04-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH04/combined-CST04-right45-v1.png`。提示词：「同一王弗人物，右前45°全身中性站姿；脸与体态严格继承 CH CH04，服装结构、层数、颜色、材料严格继承 CST CST04，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST04 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST05｜陆游衣装

- **旧参考 R-CST05：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang/S05-start-v1.png`，只参考**右侧男子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 南宋生活语境、灰蓝色、适合行走的长衣轮廓；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST05/front-v1.png`。提示词：「为陆游设计一套独立服装资产，参考 R-CST05 中右侧男子的灰蓝色、适合行走的长衣轮廓，放在无脸中性人台上展示完整正面。它属于南宋生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST05 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST05 仅辅助颜色。目标 `assets/costumes/CST05/side-v1.png`。提示词：「把同一套陆游服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST05 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST05/back-v1.png`。提示词：「为同一套陆游服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH05/CST05 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH05/combined-CST05-front-v1.png`。提示词：「同一陆游人物，正面全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH05/CST05 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\combined-CST05-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH05/combined-CST05-left45-v1.png`。提示词：「同一陆游人物，左前45°全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH05/CST05 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\combined-CST05-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH05/combined-CST05-left-v1.png`。提示词：「同一陆游人物，左侧全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH05/CST05 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\combined-CST05-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH05/combined-CST05-back-v1.png`。提示词：「同一陆游人物，背面全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH05/CST05 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\combined-CST05-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH05/combined-CST05-right-v1.png`。提示词：「同一陆游人物，右侧全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH05/CST05 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST05\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH05\combined-CST05-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH05/combined-CST05-right45-v1.png`。提示词：「同一陆游人物，右前45°全身中性站姿；脸与体态严格继承 CH CH05，服装结构、层数、颜色、材料严格继承 CST CST05，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST05 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST06｜唐氏衣装

- **旧参考 R-CST06：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F03-lu-tang/S05-start-v1.png`，只参考**左侧女子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 南宋生活语境、浅暖色、适合步行的多层衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST06/front-v1.png`。提示词：「为唐氏设计一套独立服装资产，参考 R-CST06 中左侧女子的浅暖色、适合步行的多层衣装，放在无脸中性人台上展示完整正面。它属于南宋生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST06 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST06 仅辅助颜色。目标 `assets/costumes/CST06/side-v1.png`。提示词：「把同一套唐氏服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST06 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST06/back-v1.png`。提示词：「为同一套唐氏服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH06/CST06 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH06/combined-CST06-front-v1.png`。提示词：「同一唐氏人物，正面全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH06/CST06 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\combined-CST06-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH06/combined-CST06-left45-v1.png`。提示词：「同一唐氏人物，左前45°全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH06/CST06 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\combined-CST06-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH06/combined-CST06-left-v1.png`。提示词：「同一唐氏人物，左侧全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH06/CST06 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\combined-CST06-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH06/combined-CST06-back-v1.png`。提示词：「同一唐氏人物，背面全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH06/CST06 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\combined-CST06-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH06/combined-CST06-right-v1.png`。提示词：「同一唐氏人物，右侧全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH06/CST06 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST06\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH06\combined-CST06-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH06/combined-CST06-right45-v1.png`。提示词：「同一唐氏人物，右前45°全身中性站姿；脸与体态严格继承 CH CH06，服装结构、层数、颜色、材料严格继承 CST CST06，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST06 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST07｜沈复衣装

- **旧参考 R-CST07：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen/S07-start-v1.png`，只参考**左侧男子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 清代生活语境、朴素低光泽的家居衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST07/front-v1.png`。提示词：「为沈复设计一套独立服装资产，参考 R-CST07 中左侧男子的朴素低光泽的家居衣装，放在无脸中性人台上展示完整正面。它属于清代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST07 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST07 仅辅助颜色。目标 `assets/costumes/CST07/side-v1.png`。提示词：「把同一套沈复服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST07 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST07/back-v1.png`。提示词：「为同一套沈复服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH07/CST07 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH07/combined-CST07-front-v1.png`。提示词：「同一沈复人物，正面全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH07/CST07 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\combined-CST07-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH07/combined-CST07-left45-v1.png`。提示词：「同一沈复人物，左前45°全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH07/CST07 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\combined-CST07-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH07/combined-CST07-left-v1.png`。提示词：「同一沈复人物，左侧全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH07/CST07 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\combined-CST07-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH07/combined-CST07-back-v1.png`。提示词：「同一沈复人物，背面全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH07/CST07 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\combined-CST07-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH07/combined-CST07-right-v1.png`。提示词：「同一沈复人物，右侧全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH07/CST07 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST07\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH07\combined-CST07-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH07/combined-CST07-right45-v1.png`。提示词：「同一沈复人物，右前45°全身中性站姿；脸与体态严格继承 CH CH07，服装结构、层数、颜色、材料严格继承 CST CST07，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST07 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

## CST08｜陈芸衣装

- **旧参考 R-CST08：** `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\storyboard\frames\F04-shen-chen/S07-start-v1.png`，只参考**右侧女子**衣装的整体轮廓和色彩关系；角色 `WARDROBE / provisional`。
- **设计边界：** 清代生活语境、浅色、便于坐姿和夹菜的家居衣装；材质低光泽、层次可辨、袖口不遮挡剧本手部动作；其他精确形制属于创作设计，不能宣传为史实。

### 独立服装三视图

1. **CREATE NEW｜front-v1.png：** 目标 `assets/costumes/CST08/front-v1.png`。提示词：「为陈芸设计一套独立服装资产，参考 R-CST08 中右侧女子的浅色、便于坐姿和夹菜的家居衣装，放在无脸中性人台上展示完整正面。它属于清代生活语境的创作视觉设计，不宣称历史复原。明确内外层、领口、袖口、衣摆、系结与织物结构，布料有自然重量和局部磨损，颜色关系与参考相近；均匀中性光、简单背景，不出现真实人物面孔、手持道具或房间。」附加通用负面约束。
2. **EDIT FROM CST08 front｜side-v1.png：** 上传已批准 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\front-v1.png`（`WARDROBE / EDIT TARGET`），旧 R-CST08 仅辅助颜色。目标 `assets/costumes/CST08/side-v1.png`。提示词：「把同一套陈芸服装只转为左侧面展示；保留正面批准的层数、领袖/系结位置、颜色、织物和衣摆长度，侧面折叠与垂坠物理可信。无脸人台、均匀光、简单背景；不重新设计服装。」附加通用负面约束。
3. **EDIT FROM CST08 front + side｜back-v1.png：** 上传已批准正面与侧面（`WARDROBE / EDIT TARGET`）。目标 `assets/costumes/CST08/back-v1.png`。提示词：「为同一套陈芸服装补全背面，不改变正面和侧面的层数、衣摆、肩线、袖口、颜色和材料；背部结构应能由这两张图合理连接。无脸人台、均匀光、简单背景；不增加未有依据的纹样或配件。」附加通用负面约束。

### 人物穿着组合六视图

先上传并审核 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png` 和本套服装三视图。组合正面一旦通过，其余视图必须以组合正面为母图，配合对应人物体态角度与服装侧/背图编辑派生。

- **CH08/CST08 正面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-front-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\front-v1.png`（WARDROBE）。CREATE NEW；目标 `assets/characters/CH08/combined-CST08-front-v1.png`。提示词：「同一陈芸人物，正面全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH08/CST08 左前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-left45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\combined-CST08-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH08/combined-CST08-left45-v1.png`。提示词：「同一陈芸人物，左前45°全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH08/CST08 左侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-left-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\combined-CST08-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH08/combined-CST08-left-v1.png`。提示词：「同一陈芸人物，左侧全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH08/CST08 背面：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-back-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\back-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\combined-CST08-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH08/combined-CST08-back-v1.png`。提示词：「同一陈芸人物，背面全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH08/CST08 右侧：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-right-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\combined-CST08-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH08/combined-CST08-right-v1.png`。提示词：「同一陈芸人物，右侧全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。
- **CH08/CST08 右前45°：** 上传 `D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\canon-face-front-v1.png`（IDENTITY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\body-right45-v1.png`（BODY）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\front-v1.png`与`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\costumes\CST08\side-v1.png`（WARDROBE）、`D:\project\Codex_zimeiti\AIGC Creater\projects\FPD-20261002-他们把爱写进了千年\assets\characters\CH08\combined-CST08-front-v1.png`（EDIT TARGET）。EDIT FROM 已批准组合正面；目标 `assets/characters/CH08/combined-CST08-right45-v1.png`。提示词：「同一陈芸人物，右前45°全身中性站姿；脸与体态严格继承 CH CH08，服装结构、层数、颜色、材料严格继承 CST CST08，只改变观察角度。领袖、系结、衣摆与手脚穿戴关系自然；均匀中性光、简单背景，无表演、无场景。」附加通用负面约束。

**CST08 验收：** 服装三视图结构一致；组合六视图同一张脸和身形，袖口与衣摆不跳变；若某角度失败，只重做该角度，不重抽身份母图。

+## 独立服装材料细节板（八套各一张）

独立正/侧/背衣装均审核通过后制作；这张图只用于材料和缝制审查，不作为人物组合身份图。

- **CST01-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST01/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST01/detail-fabric-v1.png`。提示词：「从同一套李清照衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在按纸时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST02-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST02/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST02/detail-fabric-v1.png`。提示词：「从同一套赵明诚衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在按纸时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST03-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST03/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST03/detail-fabric-v1.png`。提示词：「从同一套苏轼衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在指书时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST04-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST04/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST04/detail-fabric-v1.png`。提示词：「从同一套王弗衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在指页时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST05-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST05/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST05/detail-fabric-v1.png`。提示词：「从同一套陆游衣装提取衣摆、袖口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在步行回身时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST06-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST06/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST06/detail-fabric-v1.png`。提示词：「从同一套唐氏衣装提取衣摆、袖口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在步行时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST07-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST07/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST07/detail-fabric-v1.png`。提示词：「从同一套沈复衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在坐姿夹菜时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。
- **CST08-detail-fabric-v1.png：** 上传已批准 `assets/costumes/CST08/front-v1.png` 与 `side-v1.png`（均为 WARDROBE / MATERIAL）。目标 `assets/costumes/CST08/detail-fabric-v1.png`。提示词：「从同一套陈芸衣装提取袖口、领口、织物叠层的近观察距离材料板；保持已批准颜色、层数、织法、缝合和系结位置，展示布料在夹菜时的自然折叠与局部接触磨损。中性光、无人物面孔、无场景，不重新设计衣装。」附加本包通用负面约束。验收：纹理、边缘和缝制与三视图一致。

## 回传

独立服装图放入 `assets/costumes/<CST ID>/`，组合图放入对应 `assets/characters/<CH ID>/`。先回传正面脸、全身正面和服装正面三种母图供审核；得到通过结果后按依赖生成其余角度。若在统一网页会话操作，仍按 ID 分别命名和回传，不把多角度结果拼成唯一合板。


---
