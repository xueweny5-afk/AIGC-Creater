# C01 ASSET CONTRACT｜R1

## IDENTITY

- Asset ID：C01；Type：CHARACTER；Working Name：晋惠帝。
- Version：CONTRACT-R1.1；Status：REWORK；用户回传正脸v1保留；修正v2/v3已实际生成但REJECTED，不能派生。补齐计划以asset-completion-contract-r2.md为准。
- Purpose：锁定可跨镜辨认身份，不是镜头构图。
- Source Visual Bible Version：VISUAL-BIBLE-R1；Source Screenplay：SCREENPLAY-MASTER-R1。
- Evidence Status：人物身份DOCUMENTED；外貌CREATIVE；精确肖像UNKNOWN。用户项目既有生成图供本项目连续性使用，不声明真实肖像授权或完整生成来源元数据。

## LOCKED FEATURES

偏长瘦脸、较窄下颌、粗直眉、深色眼睛、较直鼻梁、薄唇、短髭和下巴小束须，黑发后束且额前无遮挡。这些是由已查看候选图提取的暂定锚点；正式锁定需正脸像素审核。291年轻状态；沿用现有三十岁上下创作年龄外观，不增衰老。

## VARIABLE STATES

291与304自然年龄、殿内/车内状态；不得另造演员。

## PRESENTATION CHOICES

身份标定采用平视正面、中性表情、白至浅灰背景、均匀中性柔光，不将场景灯光锁成人物身份。

## UNKNOWN / OPEN FIELDS

头身比/肩胯比例和耳形侧面未锁，图中深色衣袍掩盖身体；不得从旧像猜精确身高。正脸参考中不可见区域由生成补全仍需审批；不补写历史肖像事实。

## REQUIRED VIEWS / PLATES

先正脸，后必要头部角度与身体锚点，再独立六视图；不得未批脸先生成整套。该协议用于后续跨镜可见身份，角度不可由随机相似脸替代。

## CANONICAL FACE / BODY ANCHORS

- Canonical Face：NOT_APPROVED；本批目标C01-晋惠帝-291-正脸-R1-v1.png。
- Canonical Body：PLANNED；旧衣袍全身不是中性身体批准证据。
- Head Angles：左右45°、左右侧面按下游可见需求。
- Full-body Six Views：正、左前45°、左侧、背、右侧、右前45°，各一独立文件；等待批准脸/身体。

## VIEW MATRIX

| View / Plate | Required | Derivation Parent | File Path | Status | Review Notes |
|---|---|---|---|---|---|
| 正脸v1 | 是 | 历史候选C01 | C01-晋惠帝-291-正脸-R1-v1.png | REWORK | 正面/光线通过；胡须轮廓需修正 |
| 身体、必要头角/六视图 | 是 | APPROVED脸与身体 | NOT_GENERATED | PLANNED | 不先行调用 |
| 历史候选 | 对照 | 既有源 | C01-A-晋惠帝-291-v2.png | REWORK | 只允许下述参考职责 |

## MATERIAL DETAIL PLATES

脸部Macro体积→区域色彩→部位毛孔；不默认新增微距。必要手部接触在身份/服装批准后按下游近景需求确定。

## ENVIRONMENT DETAIL & STATE PLATES

NOT_APPLICABLE：身份标定不含天气、雾尘或场景空间。

## COMBINED LOOK DEPENDENCIES

K01/K02；尚无独立APPROVED服装，不制作正式Combined Look。妆发先锁可见束发/须，未建独立妆发源图；不得把候选冠形当成精确史制。

## REFERENCE ROLE MAP

| Reference | Role | Allowed Influence | Must Not Override |
|---|---|---|---|
| [历史候选](C01-A-晋惠帝-291-v2.png) | IDENTITY候选 | 脸、发际线、髭须、年龄外观 | 正面协议、均匀光、背景、衣装、道具 |

## DERIVATION / EDIT CONTRACT

- Parent/Edit Target：历史候选，不声称APPROVED母图。
- Change：正面平视与中性表情、均匀光、简单背景；去冠和正式服装装饰。
- Preserve：上述暂定脸/发须/年龄锚点。
- Constraints：不重抽演员，不镜像左右标记；不可见区域仍为候选。

## NEGATIVE CONSTRAINTS

不换脸、改年龄、夸张表演、侧脸、强侧光、多格、正式冠服/道具/背景、塑料皮肤/噪点毛孔/磨皮、水印文字。

## FILES AND PATHS

- 已存在：[历史候选](C01-A-晋惠帝-291-v2.png)。
- 已回传：[正脸v1](C01-晋惠帝-291-正脸-R1-v1.png)；v2/v3修正文件已存在且REJECTED，只留失败对照。当前补齐Prompt：[R2全量包](../../prompts/ASSET-COMPLETE-R2.md)；B01/B01R仅为历史批次，不再指向不存在的v2。

## REVIEW RESULTS

- Review Evidence：SELF-REVIEWED；2026-10-01，由Codex查看历史原图。
- Files Inspected：C01-A-晋惠帝-291-v2.png，以及C01-B-晋惠帝-304-v1.png。
- Passed：可见演员候选有辨认锚点，与另一具名角色可分。
- Failed：非中性正面身份图；缺批准脸/身体与跨角度证据。
- Decision：旧图局部复用，REWORK；目标图PLANNED。未声称USER-APPROVED。

## DOWNSTREAM USE

只能作身份候选和历史对照。正脸批准后派生同身份角度，服装批准后组合定妆；G3未过不得进入Scene Design。

## CHANGE LOG

2026-10-01 B01R：用户授权自动修改；v2、v3均实际生成并查看，须束收短但皮肤纹理发生不自然重绘，标REJECTED，不用作母图。v1保留REWORK。最新详情：[执行审核](../../batch-b01r-execution.md)。

2026-10-01：收到用户正脸图v1，原样归档。实际对照原图，正脸角度/背景/柔光通过；新正脸下巴须比旧图更长、更宽且蓬松，上唇髭也偏浓；眉眼鼻口和窄下颌总体接近，不能因光线/头向差异要求逐像素相等。状态REWORK，仅修胡须。最新证据以[回传审核](../../batch-b01-review.md)为准，历史首审记录保留。不是USER-APPROVED，不允许未审先派生正式多视图。

2026-10-01：建立R1身份合同，记录旧图像素观察和B01依赖；没有生成新图片。
