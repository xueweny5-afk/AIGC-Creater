# ASSET REQUIREMENTS

## PROJECT

- **Project ID：** FPD-20261002-他们把爱写进了千年
- **Version / Source：** v2，2026-10-03；`world-visual-bible.md` v3、G2 通过的 `../screenplay/screenplay.fountain` v3，以及用户明确要求人物/场景多角度一致性
- **Scope：** 仅 S001–S008 当前可见需求；不预造未入镜视角。此清单是 Stage 07 需求，**不是已生成资产或提示词**。
- **Adopted Method：** 无。
- **Approval Gate：** 所有 P0 须在 Stage 08 有独立原图、版本和像素审查后，按覆盖镜头范围进入 G3。现有 `storyboard/frames/` 图不能充当 P0。

## ASSET LIST

### CHARACTER

共同规则：每项 `Type=CHARACTER`，身份锚点是**本项目内前后一致的面容、体态与发型轮廓**，不宣称复原历史真人。用户指定多角度一致性为核心，因此八人均先审正面脸，再以其为唯一身份母图派生左右 45°、左右侧面；全身先审正面体态，再从同一身份派生左前 45°、左侧、背面、右侧、右前 45°，每个角度独立原图。四位说话者须能看清简短发话口型；后段独处者须有相同身份的静态状态。材质/光线板与对应服装分开；皮肤在灯光/日光下有自然局部差异，不能换脸。所有项目 `Evidence=CREATIVE visual reconstruction`，`Priority=P0`，`Gate=G3`。

| Asset ID | Narrative Function / Scenes | Required States / Physical Response | Dependencies | Locked / Variable | Continuity Risk |
|---|---|---|---|---|---|
| CH01 李清照 | S001 发话、S002 独自按纸 | 发话/伸手/独处；手与纸接触可信 | CST01、LOC01、PROP01 | 同一脸体；情绪强弱可变 | 前后换脸、卷角手位不接 |
| CH02 赵明诚 | S001 按纸回应 | 看字、按住纸角 | CST02、LOC01、PROP01 | 仅前段身份稳定；姿态可变 | 后段残留人影 |
| CH03 苏轼 | S003 找字、S004 看空椅 | 指页/抬眼；手指贴页 | CST03、LOC02、PROP02 | 同一脸体；视线可变 | 前后身份和字行漂移 |
| CH04 王弗 | S003 发话并指明字行 | 口型、指尖在书页上 | CST04、LOC02、PROP02 | 仅前段身份稳定；手势可变 | 指向区域不清 |
| CH05 陆游 | S005 回身、S006 再回身 | 伸手、收手；后段另一手持信 | CST05、LOC03、PROP03 | 同一脸体；行走状态可变 | 手方向前后不一致 |
| CH06 唐氏 | S005 发话、走近 | 口型、行走衣摆与手部 | CST06、LOC03 | 仅前段身份稳定；步伐可变 | 后段误现、丧偶暗示 |
| CH07 沈复 | S007 发话并向陈的右碗夹菜、S008 向同一空碗夹菜又停 | 坐姿、筷子持握与停顿 | CST07、LOC04、PROP04 | 同一脸体；动作阶段可变 | 筷子/碗接触失真 |
| CH08 陈芸 | S007 抬眼回应 | 坐姿、目光回应 | CST08、LOC04、PROP04 | 仅前段身份稳定；动作可变 | 后段误现、碗主错位 |

### COSTUME

共同规则：每项 `Type=COSTUME`，需独立服装原图、前面与当前动作相关的侧/袖口视图；六视图只有新增机位时补。`Material Detail Plate` 为织物、领袖/系结、接触桌面或行走时的褶皱。`Physical/Lighting Response` 为自然垂坠、非塑料反光，袖口不得盖住关键动作；无湿、污、损状态。具体时代形制尚 `OPEN / UNKNOWN`，选定前须与宋/清研究边界核对。所有项 `Priority=P0`，`Gate=G3`。

| Asset ID | Type / Narrative Function | Required Views / States | Dependencies | Locked / Variable | Evidence / Risk |
|---|---|---|---|---|---|
| CST01 李清照 | COSTUME；按纸/独处 | 前面、袖口；S001–S002 可识别 | CH01 | 轮廓/层次稳定；明暗可变 | CREATIVE/OPEN；不能凭参考图称宋服复原 |
| CST02 赵明诚 | COSTUME；按纸 | 前面、袖口 | CH02 | 同一场内稳定；褶皱可变 | CREATIVE/OPEN；手袖遮纸风险 |
| CST03 苏轼 | COSTUME；指书/独处 | 前面、袖口；S003–S004 可识别 | CH03 | 轮廓/层次稳定；明暗可变 | CREATIVE/OPEN；前后衣形漂移 |
| CST04 王弗 | COSTUME；指页 | 前面、袖口 | CH04 | 同一场内稳定；褶皱可变 | CREATIVE/OPEN；袖口遮指尖 |
| CST05 陆游 | COSTUME；步行/回身 | 前面、侧面、衣摆；S005–S006 可识别 | CH05 | 轮廓/层次稳定；行走褶皱可变 | CREATIVE/OPEN；后段身份漂移 |
| CST06 唐氏 | COSTUME；步行/走近 | 前面、侧面、衣摆 | CH06 | 同一场内稳定；步态可变 | CREATIVE/OPEN；不以服装暗示死亡 |
| CST07 沈复 | COSTUME；坐姿/夹菜 | 前面、袖口；S007–S008 可识别 | CH07 | 轮廓/层次稳定；坐姿褶皱可变 | CREATIVE/OPEN；现有参考服饰未经清代考据 |
| CST08 陈芸 | COSTUME；夹菜 | 前面、袖口 | CH08 | 同一场内稳定；臂部动作可变 | CREATIVE/OPEN；袖口遮筷风险 |

### LOCATION

共同规则：每项 `Type=LOCATION`，先要**无人物的空间主视图**、固定锚点布局，再以同一主图和布局派生左、右约 30° 两个独立角度图；三张图必须是同一空间，不能用三次文本抽卡。还要当前可见区域的结构/材料细节板；镜头若需反向，再基于已批准的完整拓扑补图，不从单张正面图猜测不可见墙面。结构、桌椅/园门位置为锁定项，光与时间是变量。`Physical/Lighting Response` 要求木、石、纸等各自反射合理；空气 `NONE / CLEAN AIR`，无独立空气资产。`Evidence=CREATIVE reconstruction`，`Priority=P0`，`Gate=G3`。

| Asset ID | Narrative Function / Scenes | Required Views / States / Detail Plates | Dependencies | Locked / Variable | Continuity Risk |
|---|---|---|---|---|---|
| LOC01 | 李赵同案与空位 S001–S002 | 无人书房；书案、窗、书架、灯位置；桌面磨痕板；对应两个 LLS 状态 | PROP01 | 书案/赵空位稳定；照度可变 | 后段换房、纸角无处对应 |
| LOC02 | 苏王共读与空椅 S003–S004 | 无人书房；书案、椅、窗/灯关系；书桌材料板；两个 LLS 状态 | PROP02 | 椅与书位稳定；照度可变 | 空椅方向跳变 |
| LOC03 | 陆唐回身与同路 S005–S006 | 无人园路；石径、桃枝、远处门、地面接缝板；两个 LLS 状态 | PROP03 | 回身所处路段稳定；天光可变 | 路/门变成另一园 |
| LOC04 | 沈陈饭桌与空碗 S007–S008 | 无人居所；桌、双坐席、窗/灯；木桌磨痕板；两个 LLS 状态 | PROP04 | 桌位与对面空席稳定；照度可变 | 两只碗或座位方向漂移 |

### PROP

共同规则：每项 `Type=PROP`，须独立原图及状态板，不把人物手臂画进道具资产。材料在有来源的灯/日光下响应。道具不承载可读的伪史料文字。所有项 `Evidence=CREATIVE`，`Priority=P0`，`Gate=G3`；其中折信仅 S006 可见，按该镜范围审核。

| Asset ID | Narrative Function | Required Views / States / Material Plate | Physical / Lighting Response | Dependencies | Locked / Variable / Risk |
|---|---|---|---|---|---|
| PROP01 碑拓 | S001 有人按卷角；S002 独自按 | 平展/同角卷起；纸边与回弹细节 | 软纸有重量，灯下不反光成塑料 | LOC01 | 尺寸、卷角方位锁定；卷曲量可变；前后不对应风险 |
| PROP02 书 | S003 指明一行；S004 同行前停顿 | 同一打开页、同一区域标识、书脊/纸厚板 | 纸页微弯、不出现可读假字 | LOC02 | 页方向/字行锁定；指尖位置可变；换页风险 |
| PROP03 折信 | S006 陆手中未展 | 折叠态、手持尺度、纸折痕板 | 折纸有压痕、不出现可读信文 | LOC03、CH05 | 折叠态锁定；持握角度可变；遮住回身动作风险 |
| PROP04 双碗、筷与一口菜 | S007 递菜；S008 面对空碗停筷 | 双碗摆位、盛菜/空碗两态、筷与陶瓷板 | 碗有重量和柔和反射，筷能夹住食物 | LOC04、CH07–08 | 碗数与对面空碗锁定；菜量可变；碗主/手指错位风险 |

### GRAPHIC / EFFECT STATE

不建立生成图像资产。四句对白字幕、S004/S006 的引文由后期排版；其文字主版本在 `../screenplay/screenplay.fountain` 与登记表。无雾、烟、花粉、幻影或人物消失特效资产。

## APPROVAL ORDER

1. 先确认四组空间的可见结构与 PROP01–04 的位置/接触状态；这决定前后是否真能接上。
2. 再确认八人独立身份与八套服装。四位留下者需跨前后两态；说话者需可辨口型。
3. 组合检查每组前后身份、手部、核心物件、空位和对应 LLS 状态。只对实际入镜范围申请 G3，不为未入镜六视图阻塞。

## DEFERRED / NOT REQUIRED

- 未入镜的房屋背面、园门外路径、独立妆发资产、气氛粒子、可读信文、文字图像资产。人物六视图已因用户明确要求纳入交接，不再延期。
- 现有八张分镜图保留为视觉方向参考；新剧本动作所需关键帧在 Stage 11 重编，不在本阶段生成。

## NEXT STAGE

- **Primary Recommendation：** Asset Design。
- **Reason：** 当前八场所需的身份、空间、服装、道具与状态已列明；需建立独立资产合同与原图，之后按镜头范围审核 G3。
