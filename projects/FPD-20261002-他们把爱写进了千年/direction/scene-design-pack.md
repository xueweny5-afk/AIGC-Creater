# SCENE DESIGN PACK｜v6｜沈陈动作方向按实图修订

## SCENE DIRECTION IDENTITY

- **Project ID：** FPD-20261002-他们把爱写进了千年
- **Version：** v6，2026-10-12
- **Screenplay：** `../screenplay/screenplay.fountain` v4（沈陈递菜方向按用户选择修订）
- **Visual Bible：** `../visual-development/world-visual-bible.md` v3
- **Asset Manifest：** `../assets/asset-manifest.md` v10；覆盖审查 `../qc/g3-asset-review-2026-10-11.md`
- **Scope：** S001–S008；未采用独立 Method

## COVERAGE & STATUS

- **Status：** STAGE_09_SCENE_DESIGN_CURRENT；覆盖八场，无缺场。人物、服装、组合定妆、空间主视、基础道具及两张关键状态图已入库；G3 按当前可见范围通过。
- **Blocking Dependencies：** 当前八场场面设计无资产缺口。未入镜角度和材料细节按实际机位需要再补；G4 静态分镜已按用户认可实图与构图差异记录审核。

## DIRECTOR THESIS

- **Audience Endpoint：** 四次“有人回应”的日常动作，忽然变为同物同地的“无人回应”。
- **Directing Path：** 共处场各让一句简短请求得到一个可见回应；后来场让相同动作悬空。历史离散原因不混写。
- **Anti-default Decision：** 后段不靠托腮、遗照、幽灵或夸张哭泣说明孤独；人物继续处理纸、书、路、碗，停下的行为本身产生空位。

## CONTINUITY CONTRACT

- 剧本对白仅 S001「帮我按住」、S003「在这一页」、S005「等等我」、S007「尝尝这个」。这些为创作的非逐字对白。
- 四次时间断裂发生在场与场之间；后场人物不会在同场“消失”。每组只保留剧本规定的人数与核心物件。
- 四组时地互不连接；S005–S006 表示离散而非唐氏死亡。S004、S006 引文由后期排版，场内不要求书/信生成可读字。
- 八场分别继承 `LLS-LOC01–04-TOGETHER/ALONE-v1`；空气均 `NONE / CLEAN AIR`，没有场内光态或空气状态突变。

## SPATIAL EVIDENCE MAP

| Anchor | Evidence | Source / Confidence | Allowed Blocking | Unknown Boundary |
|---|---|---|---|---|
| LOC01 书案与赵位置 | VISIBLE in `../assets/locations/LOC01/topology-main-v1.png` | 正式无人空间主图；左/右 30° 已入库 | 桌案横贯前景，左后书架、右后格窗及固定灯；二人同案，赵缺席后保留右侧空位 | 书房反向墙与未拍区域 UNKNOWN |
| LOC02 书页与王座位 | VISIBLE in `../assets/locations/LOC02/topology-main-v1.png` | 正式无人空间主图；左/右 30° 已入库 | 两座椅分列桌后，书置桌面中区；王位在画面右，苏从右页中部同一竖列抬眼看右侧空椅 | 书页实际文字 UNKNOWN；只用不可读纹理 |
| LOC03 石径、桃枝、园门 | VISIBLE in `../assets/locations/LOC03/topology-main-v1.png` | 正式无人空间主图；右 30° 已入库 | 石径从前景通向后方圆门；桃枝在左上，假山在路径左，陆在同一路段回身 | 园门外路径与反向区域 UNKNOWN；左 30° 尚无原图 |
| LOC04 饭桌、两处坐席 | VISIBLE in `../assets/locations/LOC04/topology-main-v1.png` | 正式无人空间主图；左 30° 已入库 | 饭桌横贯前景，左右两座椅与后方格窗固定；沈左、陈右，两碗保持左右位置 | 居所反向墙 UNKNOWN；右 30° 尚无原图 |

现有空间主图只证明当前可见区域；本稿不要求反拍或绕行。LOC03 左 30°、LOC04 右 30° 和各处材料细节尚未入库，Stage 10 不能引用这些视角。

## ASSET VERSION BINDING｜当前场面范围

| 场景 | 人物身份 / 穿着 | 空间与道具源图 | 当下限制 |
|---|---|---|---|
| S001–S002 | CH01、CH02 正脸 v2；CST01、CST02 独立正面 v1 与各自组合正面 v1 | LOC01 `topology-main-v1.png`；PROP01 `flat-v1.png`、`corner-curled-v1.png` | 右上角同纸角卷起/按平；前后手位需在正式分镜核对 |
| S003–S004 | CH03、CH04 正脸 v2；CST03、CST04 独立正面 v1 与各自组合正面 v1 | LOC02 `topology-main-v1.png`；PROP02 `open-page-v1.png` | 书置桌面中区；指向右页中部同一竖列，不生成可读文字 |
| S005–S006 | CH05、CH06 正脸 v1；CST05、CST06 独立正面 v1 与各自组合正面 v1 | LOC03 `topology-main-v1.png`；S006 的 PROP03 `folded-v1.png` | 仅用已证明的同一路段；折信在另一只手中，前后回身方向一致 |
| S007–S008 | CH07、CH08 正脸 v1；CST07、CST08 独立正面 v1 与各自组合正面 v1 | LOC04 `topology-main-v1.png`；PROP04 `two-bowls-v1.png`、`opposite-empty-v1.png` | 前场左碗米饭、右碗青菜；后场左碗饭菜、右碗空；碗数和位置不变 |

组合六视图均已入库；Stage 10 按实际机位选同角度的 `combined-CSTxx-<angle>-v1.png`，不把组合正面强行用于侧面或反打。场面基图的中性/日间光不决定剧情时段；S001/S003/S007 的夜间灯光必须在后续静态画面中按 Visual Bible 的同一实际灯位实现，不能仅把整张图调暗。

## SCENE DESIGNS

### S001｜李赵书房，共处

- **Cause / Function：** 碑拓纸角卷起，使共同劳动成为可见关系。
- **Entry → Objective / Tactic：** 李清照与赵明诚同在书案；李要让纸平展，按住中间并将卷角推给赵。
- **Trigger → Response → Exit：** 李说「帮我按住」；赵按住纸角，李继续看字。纸角被两人的手共同稳住。
- **Performance / Blocking：** 二人只围绕同一张碑拓移动手与视线；李发话后让出纸角，赵确实接手，不能出现两个各自无关的手势。
- **Look / Air：** NLA-TOGETHER-v1；LLS-LOC01-TOGETHER-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 纸轻响与一句请求，回应发生后短暂留住共同动作；不得用长对白压掉动作。
- **Assets / Boundary：** CH01–02、CST01–02、LOC01 主视及 PROP01 平展/卷角两态已入库；旧首帧动作过期，需重做静态分镜。

### S002｜李赵书房，后来

- **Cause / Function：** 同一纸角再次卷起，赵的位置已经空了。
- **Entry → Objective / Tactic：** 李一人在原书案，仍要稳住纸；先看原本有人帮忙的位置，再独自伸手按住。
- **Trigger → Response → Exit：** 纸角回弹，无人接手；李自己按住，空位保持清楚。
- **Performance / Blocking：** 不要求李表现特定真实心理；动作从求助变成自助。赵不以影、梦或倒影出现。
- **Look / Air：** NLA-ALONE-v1；LLS-LOC01-ALONE-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 前场纸声在断裂后明显变稀；留出无人回应的一小段静默。
- **Assets / Boundary：** CH01、CST01、LOC01 主视及 PROP01 平展/卷角两态已入库；同桌与赵的空位由 LOC01 主视约束。

### S003｜苏王书房，共处

- **Cause / Function：** 苏在书中寻找，王记得位置。
- **Entry → Objective / Tactic：** 王与苏同坐书案，王想把苏的注意指向一行，指页并说「在这一页」。
- **Trigger → Response → Exit：** 苏顺着她指尖找到字行，抬眼看她；这页和这一行成为共同记忆锚点。
- **Performance / Blocking：** 王的手确实指到苏可见处；苏先看书，再看她。口型只承载这一句短话。
- **Look / Air：** NLA-TOGETHER-v1；LLS-LOC02-TOGETHER-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 短句与纸页触碰，留一点找到字后的回应。
- **Assets / Boundary：** CH03–04、CST03–04、LOC02 主视、PROP02 打开页均已入库并经用户确认；书中不出现可读伪文本，指向右页中部同一竖列。

### S004｜苏王书房，后来

- **Cause / Function：** 同一本书仍在，曾经指页的人缺席。
- **Entry → Objective / Tactic：** 苏的手停在同一行，抬眼寻找原座位；椅子空着。
- **Trigger → Response → Exit：** 无人回答，手指与目光停住；后期才出现「十年生死两茫茫」。
- **Performance / Blocking：** 不重演词中梦，不让王重新出现；身体可以保持静止，重点是书行到空椅的视线变化。
- **Look / Air：** NLA-ALONE-v1；LLS-LOC02-ALONE-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 前场人声消失，静默给空椅；引文不作为人物说话。
- **Assets / Boundary：** CH03、CST03、LOC02、PROP02 均已有源图；同页同列、右侧空椅由现有主视与书图约束。

### S005｜春园石径，共处

- **Cause / Function：** 唐氏落后半步，请陆等她。
- **Entry → Objective / Tactic：** 陆在前，唐停了一瞬说「等等我」；她要追上他。
- **Trigger → Response → Exit：** 陆回身伸手，唐向他走近；手在接近而尚未完成接触时，关系仍有回应。
- **Performance / Blocking：** 陆只回身，不穿越未知园路；唐的步伐自然。不能从衣装或画面暗示她将死亡。
- **Look / Air：** NLA-TOGETHER-v1；LLS-LOC03-TOGETHER-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 一句请求、两人的脚步与回身，保留伸手后的短暂停顿。
- **Assets / Boundary：** CH05–06、CST05–06、LOC03 主视已入库并经用户确认；只使用主视证明的园路与圆门可见区域，园门外拓扑未知。

### S006｜春园石径，后来

- **Cause / Function：** 同一段路上唐氏不在，陆的回身动作失去对象。
- **Entry → Objective / Tactic：** 陆独自站在同一路段，一手持未展开的折信；再次回身伸出另一只手。
- **Trigger → Response → Exit：** 身后无人，他收手，低头看折信；后期才出现「山盟虽在，锦书难托」。
- **Performance / Blocking：** 只呈现伸手、收回、看信，不演唐氏死亡或真实未寄信事件。
- **Look / Air：** NLA-ALONE-v1；LLS-LOC03-ALONE-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 双人脚步失去一组，风是园中自然声；收手前应有无人回应的间隙。
- **Assets / Boundary：** CH05、CST05、LOC03 主视、PROP03 折信已入库；折信不展开成可读文字。

### S007｜沈陈居所，共处

- **Cause / Function：** 一餐里的招呼与夹菜表现平常相守。
- **Entry → Objective / Tactic：** 两人各有碗；沈从左碗夹起一口菜送入陈的右碗，说「尝尝这个」。
- **Trigger → Response → Exit：** 陈抬眼望向沈，接住招呼；一口菜已到了她的碗中。
- **Performance / Blocking：** 菜只从沈的筷到陈的右碗，碗数始终为二；不要只相视微笑而忘掉递菜。
- **Look / Air：** NLA-TOGETHER-v1；LLS-LOC04-TOGETHER-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 短句和筷碰碗的轻响，留一点陈抬眼的回应。
- **Assets / Boundary：** CH07–08、CST07–08、LOC04 主视、PROP04 双碗基础图已入库；左碗为沈碗，右碗为陈碗，具体餐食为创作重构。

### S008｜沈陈居所，后来

- **Cause / Function：** 同一饭桌仍摆两碗，对面碗空了。
- **Entry → Objective / Tactic：** 沈独坐，夹起一口菜，筷子向对面空碗移动。
- **Trigger → Response → Exit：** 到空碗前停住，放下筷子；空碗留在原处结束。
- **Performance / Blocking：** 不让碗凭空装满，不让陈芸以幻影重现；动作完成后不增加解释性表演。
- **Look / Air：** NLA-ALONE-v1；LLS-LOC04-ALONE-v1；CLEAN AIR / HOLD。
- **Sound / Rhythm：** 筷碰碗的熟悉声被悬置，放下筷子后留一段安静；不加总结台词。
- **Assets / Boundary：** CH07、CST07、LOC04 主视和 PROP04 双碗/对面空碗两态已入库；右侧空碗位置必须与前场一致。

## CROSS-SCENE STATE CHAIN

| Pair | Core Entity / Quantity | Together State | Later State | Continuity Test |
|---|---|---|---|---|
| S001→S002 | PROP01 一张碑拓、LOC01 一处书案 | 赵按住同一纸角 | 纸角再卷，李独自按 | 同角、同桌、赵空位 |
| S003→S004 | PROP02 一本书、LOC02 一处书案 | 王指明同一行 | 苏手停该行，王椅空 | 同页同位、椅不换向 |
| S005→S006 | LOC03 一段石径；后场 PROP03 一封折信 | 陆回身向唐伸手 | 陆回身伸手又收，唐不在 | 园门/桃枝位置、伸手方向 |
| S007→S008 | PROP04 两碗与筷、LOC04 一张饭桌 | 沈给陈的右碗一口菜 | 沈再次向对面空碗伸筷 | 碗数、位置、菜量与手位 |

## PERFORMANCE CONTINUITY LEDGER

| Scene Pair / Surviving Character | First Action | Later Repetition | Voice / Pause | Physical Constraint |
|---|---|---|---|---|
| S001–S002 李清照 | 请赵按纸，手让出纸角 | 自己按同角 | 前场一句；后场无回应 | 纸有回弹，手位不能跳 |
| S003–S004 苏轼 | 跟王指尖找书行，抬眼 | 手停同行，抬眼看空椅 | 前场听王说；后场无声 | 同页同椅；不翻页 |
| S005–S006 陆游 | 听唐呼唤，回身伸手 | 回身伸手、收回，持信 | 前场听唐说；后场留白 | 不换持信手；路径方向稳定 |
| S007–S008 沈复 | 夹菜给陈并说话 | 再夹菜向对面空碗后停 | 前场由沈说；后场静默 | 两碗固定，筷子接触可信 |

## SCENE RHYTHM MAP

| Pair | Pressure / Energy | Required Hold | Release Trigger |
|---|---|---|---|
| 李赵 | 小事得到即时帮手 → 同事独做 | 后场纸角卷起到李自己按住之间 | 手按住后进入下一组 |
| 苏王 | 找到字行 → 没人再指给他看 | 苏抬眼后空椅无人回应 | 视线停住后进入下一组 |
| 陆唐 | 呼唤得到回身 → 同路无人 | 后场伸手到收手之间 | 折信进入注意后进入下一组 |
| 沈陈 | 招呼得到接应 → 递菜动作落空 | 筷子停在空碗前与放下后 | 空碗余韵结束全片 |

## SOUND INTENT & BRIDGE MAP

| Pair | Together Source | Later Source / Silence | Transition Function |
|---|---|---|---|
| 李赵 | 一句请求、纸声 | 纸声变少、无人回答 | 共同按纸变独自按纸 |
| 苏王 | 一句指示、轻触书页 | 人声消失、同书页安静 | 记得位置的人不在 |
| 陆唐 | 一句呼唤、双人脚步 | 单人脚步、自然风 | 回身后无人跟上 |
| 沈陈 | 一句招呼、筷碗接触 | 筷子停顿后的静默 | 同一桌的空位收束 |

声音只写叙事功能，具体录音、配乐和混音不在本阶段决定。声音突变发生在两场之间，不把前场对白复制成历史回声。

## ASSET & PRODUCTION DEPENDENCIES

- 当前已入库的人物独立图、八套衣装及组合定妆、四处空间主视、四件基础道具和两张关键状态图已确认；逐项状态见 `../assets/asset-manifest.md` v9。
- 本场面稿固定行动、可见关系、空间锚点与状态依赖；具体机位、镜头时长、逐帧姿态及任何反向视图由后续阶段决定。正式静态分镜仍须等相应 G3 范围通过。

## DECISION REGISTER

### LOCKED

- 剧本 v3 的四句短对白、四个互动及后来无人接续、四组人物、两处原文引句。

### OPEN

- 未见空间的反向拓扑；声音制作方式；正式分镜及运动方案。

### ASSUMED

- 已入库 LOC 主视仅覆盖当前可见区域；灯光状态可以在同一固定空间上调整，但不能移动窗、桌椅和灯位。

## NEXT STAGE

- **Primary Recommendation：** Stage 10 Shot Design（八场均可设计当前可见区域内的镜头）。
- **Reason：** 八场场面已对齐 G2 v3 和当前真实资产；两张关键道具状态图入库后，G3 已按当前可见范围通过。
