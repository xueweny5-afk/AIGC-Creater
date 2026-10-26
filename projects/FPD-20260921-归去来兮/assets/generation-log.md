# GENERATION LOG

## RUN IDENTITY

- **Project ID：** FPD-20260921-归去来兮
- **Run Date：** 2026-09-21
- **Mode：** Built-in image generation
- **Batch：** Phase A / neutral identity candidates v1
- **Purpose：** 为三位核心人物各生成一张可供用户选择的正面全身主参考候选；不是剧情画面，也不是正式服装设计。

## SHARED GENERATION CONTRACT

- **Use Case：** historical-scene
- **Style / Medium：** 写实历史电影人物资产，真实皮肤、毛发、手部与织物；中性工作室背景与均匀自然光。
- **Framing：** 平视、正面、完整全身、双手与双脚可见、自然站立。
- **Shared Constraints：** 单人、原创非名人面貌、无文字、无水印、无道具、无剧情动作、无仙侠与跨时代官帽。
- **Costume Status：** 所有衣着均为临时基础衣层，只用于观察面貌与体态；未经过 CST-001 至 CST-003 的历史服饰审批。

## GEN-001｜CHR-001 张翰

- **Output：** `assets/characters/CHR-001/zhang-han-identity-candidate-v1.png`
- **Prompt Summary：** 约42岁，精瘦健康，颧骨略宽、直眉、轮廓清楚，短髭与克制短须；冷静、明确但中性；灰褐无装饰临时衣层；排除放浪名士脸谱、鱼酒秋叶和官帽。
- **Actual Review：** 全身与脸部清楚，体态稳定，手脚无明显结构错误；无多余人物、道具、文字或水印。服饰仅可视为临时基础层。
- **Status：** GENERATED_PENDING_REVIEW

## GEN-002｜CHR-002 陶渊明

- **Output：** `assets/characters/CHR-002/tao-yuanming-identity-candidate-v1.png`
- **Prompt Summary：** 约40岁，修长但不病弱，长窄脸、深眼、轻度日晒与疲惫感、短髭短须；不做白发高龄隐士；土色与亚麻色临时衣层；排除菊、酒、农具和田园标签。
- **Actual Review：** 年龄与体态符合合同方向，没有老人化和隐士道具；手脚无明显结构错误；无文字或水印。服饰未作历史批准。
- **Status：** GENERATED_PENDING_REVIEW

## GEN-003｜CHR-003 王献之

- **Output：** `assets/characters/CHR-003/wang-xianzhi-identity-candidate-v1.png`
- **Prompt Summary：** 约36岁，高挑均衡，额部较宽、下颌收窄、眼神克制，短髭与极短下颌须；成熟但未老，骨相便于后续同脸病弱派生；冷灰临时衣层；排除书法光环、皇室和爱情符号。
- **Actual Review：** 盛年身份清楚，骨相适合年龄连续性设计；手脚无明显结构错误；无道具、文字或水印。服饰未作历史批准。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW

- **Passed：** 三张均为可查看的项目内文件；人物数量、年龄层、全身结构、背景洁净度与无文字要求通过；三人具有可辨差异。
- **Risks：** 三张临时衣层仍共享相近的通用袍服轮廓，不能作为服饰批准证据；真实侧背一致性尚未验证；用户尚未确认三张脸是否作为主参考。
- **Decision：** 不标记 APPROVED。先让用户分别接受或提出面貌修改；接受后从对应图像派生转面与状态，不重新随机生成人物。

## USER REVIEW｜v1

- **Finding 1：** CHR-001 与 CHR-002 面貌、须发和通用袍服轮廓相近，辨识度失败。
- **Finding 2：** 历史人物资产必须参考所属朝代服饰特色，不能继续使用无时代区分的临时袍服。
- **Action：** v1 三张均退出下游使用；建立 `assets/costumes/costume-evidence-brief.md`，生成 v2。

## GEN-004｜CHR-001 张翰 v2

- **Output：** `assets/characters/CHR-001/zhang-han-identity-candidate-v2.png`
- **Prompt Summary：** 方圆宽脸、下颌较厚、紧凑结实体态、浓髭短方须；西晋在职属官完整衣层与小冠/冠帻候选；深黯绛与灰褐层次。
- **Actual Review：** 与陶渊明 v2 的脸部几何、体态、须发和服装轮廓差异明显；冠高、冠式和腰带金属饰件仍需核验。
- **Status：** GENERATED_PENDING_REVIEW

## GEN-005｜CHR-002 陶渊明 v2

- **Output：** `assets/characters/CHR-002/tao-yuanming-identity-candidate-v2.png`
- **Prompt Summary：** 长窄高额脸、较长鼻梁、清瘦高挑体态、稀疏髭须；东晋归家士人幅巾、宽衫大袖与博带候选；浅土、亚麻和橄榄灰。
- **Actual Review：** 与张翰 v2 明显区分，未老人化、仙人化或加入标签道具；幅巾包法和宽衫比例仍需核验。
- **Status：** GENERATED_PENDING_REVIEW

## GEN-006｜CHR-003 王献之 v2

- **Output：** `assets/characters/CHR-003/wang-xianzhi-identity-candidate-v2.png`
- **Prompt Summary：** 约36岁，额宽、下颌收窄的软方脸，高挑均衡，稀薄短须；东晋高门公职冠帻和精整宽博衣层候选；墨蓝、炭灰与石灰色。
- **Actual Review：** 三人身份轮廓可辨；高门公职方向成立，但冠式与中书令服制细节仍为研究推定。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜v2

- **Passed：** 三人的脸部几何、体态、须发、头部状态与服装轮廓不再同质化；时代方向来自博物馆展览和冠服制度研究，不再使用纯通用古装。
- **Open：** 所有冠式、腰带金属件、官阶色彩和具体服层仍需服装专家级证据；当前只能批准“身份与方向”，不能批准“精确复原”。
- **Decision：** 等待用户审阅 v2 面貌与整体历史感；通过后再制作三人转面，并优先返修有疑问的冠带细节。

## USER REVIEW｜v2

- **Date：** 2026-09-22
- **Decision：** 用户接受三位人物 v2 的面貌与整体身份方向。
- **Approval Scope：** 面貌、年龄带、体态与三人辨识关系。
- **Not Yet Approved：** 具体冠式、腰带、官阶色彩、服层结构、侧背一致性，以及王献之病重状态。
- **Routing：** 先完成服饰证据收紧，再由已锁定主参考派生所需视图和状态。

## TURNAROUND BATCH｜v1

- **Run Date：** 2026-09-22
- **Mode：** Built-in image generation / identity-preserving edit
- **Purpose：** 从用户批准的三张 v2 主参考派生正面、严格左侧面和背面三视图；同时去除缺少证据的通用古装细节，建立可供后续状态派生的晋代服装候选。
- **Shared Layout：** 单张横向三联全身图，同一人物、同一套衣服、同一比例；中性棚拍背景、低表情、无文字、无道具、无场景。

### GEN-007｜CHR-001 张翰三视图

- **Output：** `assets/characters/CHR-001/zhang-han-turnaround-v1.png`
- **Prompt Summary：** 严格锁定方圆宽脸、厚下颌、浓髭短方须和紧凑结实体态；采用西晋属官的一梁进贤冠候选、黯绛外袍、灰褐内层与素织腰带；移除 v2 连续金属腰牌。
- **Actual Review：** 三视图同脸与体态基本稳定，服层正侧背连续，无文字和多余物；冠体仍偏视觉化，梁制需保持“研究推定”标记。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-008｜CHR-002 陶渊明三视图

- **Output：** `assets/characters/CHR-002/tao-yuanming-turnaround-v1.png`
- **Prompt Summary：** 严格锁定长窄高额脸、清瘦高挑体态、稀疏髭须；采用低调深色巾式候选、素色宽衫、交领内层与布带，不加入官阶物、酒菊或农具。
- **Actual Review：** 三视图同脸与体态稳定，归田者轮廓明确，与张翰不再同质；巾式包裹结构仍需按研究推定使用。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-009｜CHR-003 王献之三视图

- **Output：** `assets/characters/CHR-003/wang-xianzhi-turnaround-v1.png`
- **Prompt Summary：** 严格锁定额宽、直鼻、收窄下颌、稀薄须发和修长体态；采用两梁进贤冠候选、黯绛朝服、墨色绶带方向及一件克制的青玉佩。
- **Actual Review：** 三视图同脸、身形和冠服连续性稳定，高门任官方向清楚；服制来自制度文本的视觉推定，不是出土服装复原。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜TURNAROUND v1

- **Passed：** 三位人物在脸部几何、年龄感、体态、须发、色彩和身份轮廓上均可快速区分；正侧背没有明显换脸、肢体结构错误、文字或场景污染。
- **Open：** 三套冠巾的精确结构均未达到专家复原级别；王献之病重状态及三人的剧情状态板尚未生成。
- **Decision：** 三张作为 TURNAROUND CANDIDATE 进入用户复核；用户接受后再制作状态对照，不直接进入剧情镜头生成。

## USER REVIEW｜TURNAROUND v1

- **Date：** 2026-09-22
- **Decision：** 用户接受张翰、陶渊明、王献之三张正侧背三视图。
- **Approval Scope：** 同脸性、体态、须发、基础服装轮廓及三人辨识关系。
- **Continuing Caveat：** 冠、巾和具体服层仍按研究推定使用，不升级为精确考古复原。

## STATE COMPARISON BATCH｜v1

- **Run Date：** 2026-09-22
- **Mode：** Built-in image generation / identity-preserving edit
- **Purpose：** 将已批准人物派生为能服务“归”主题的三阶段状态板；保持中性背景，不提前制作剧情镜头。
- **Shared Layout：** 单张横向三联、正面全身、同一尺度和光线；仅改变衣层、细微姿态、表情及必要的健康状态。

### GEN-010｜CHR-001 张翰状态板

- **Output：** `assets/characters/CHR-001/zhang-han-state-comparison-v1.png`
- **States：** 在职 → 离任 → 归途。
- **Prompt Summary：** 锁定方圆宽脸、厚重体态和须发；从黯绛官署外层逐步减为素色离任与完整、克制的行旅衣层；不使用散发、酒、鱼或狂喜表情。
- **Internal Rework：** 初次生成把归途外衣做成明显毛边破损，造成落魄化误读；该版本未归档。定向返工仅修复第三状态衣物，使其完整、朴素并保留轻微风尘感。
- **Actual Review：** 三状态同脸与体态稳定；返工后“主动归去”不再被贫困化。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-011｜CHR-002 陶渊明状态板

- **Output：** `assets/characters/CHR-002/tao-yuanming-state-comparison-v1.png`
- **States：** 彭泽令 → 离任 → 归家。
- **Prompt Summary：** 锁定长窄高额脸、清瘦体态和稀疏须发；从深灰低阶官署衣层与冠候选，过渡到去冠浅色内层，再回到素色宽衫与布巾。
- **Actual Review：** 三状态同脸与体态稳定，颜色与衣层变化克制；没有把归田做成乞丐、仙人或标签化隐士。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-012｜CHR-003 王献之状态板

- **Output：** `assets/characters/CHR-003/wang-xianzhi-state-continuity-v1.png`
- **States：** 盛年书写 → 公开任官 → 病重末期。
- **Prompt Summary：** 锁定额宽直鼻、收窄下颌、稀薄须发和修长体态；以灰黑室内衣、黯绛朝服、浅灰病中衣区分状态；病重只减少软组织与体力，不做老人化和疾病奇观。
- **Actual Review：** 三阶段骨相可追认；末期有疲惫、削瘦和姿态下沉，但未变成高龄老人或另一人物。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜STATE v1

- **Passed：** 三组状态板均保持人物身份连续，且张翰的行动性、陶渊明的松脱感、王献之的不可逆衰弱形成不同的视觉变化逻辑。
- **Open：** 陶渊明离任与归家的差别刻意克制，需由用户判断是否足够；所有状态板仍未进入剧情环境。
- **Decision：** 等待用户确认状态对照。通过后进入关键场景资产与镜头设计，不再扩展无关服装变体。

## LOCATION & PROP BATCH｜B1

- **Run Date：** 2026-09-22
- **Mode：** Built-in image generation
- **Purpose：** 生成张翰段所需的中性空间与交还物候选；不是剧情镜头、分镜或最终画面。
- **Evidence Boundary：** 汉代建筑明器研究只能提供建筑观念与材料范围，不能直接还原西晋官署；故宫玺印资料可支持秦汉魏晋统一印制、铜印及常见钮式范围，但不能确定张翰职务实物；未找到足以锁定张翰南归船型的直接材料。
- **Research Entry Points：** 中国国家博物馆《汉代建筑明器研究》；故宫博物院“玺印”专题与秦汉魏晋官印研究。

### GEN-013｜LOC-001 西晋洛阳官署空间候选

- **Output：** `assets/locations/LOC-001/luoyang-office-spatial-reference-v1.png`
- **Prompt Summary：** 同一小尺度木构官署的工作案看出口、出口反看工作案和俯视拓扑；汉晋范围材料、秋日自然光、无人物文字与宫殿化装饰。
- **Actual Review：** 正反与俯视锚点基本一致，行动路径可用；瓦、窗、家具为低断言视觉候选。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-014｜LOC-002 南归水路与行旅船候选

- **Output：** `assets/locations/LOC-002/southbound-waterway-boat-reference-v1.png`
- **Prompt Summary：** 秋季内河、水路方向、小型人力木舟的环境、侧面和俯视；排除楼船、画舫、高桅帆船和旅游地标。
- **Actual Review：** 环境和几何关系清楚；拱形编织篷仍造成后世常见小舟联想。
- **Status：** REWORK

### GEN-015｜PRP-001 官职铜印候选

- **Output：** `assets/props/PRP-001/western-jin-duty-seal-candidate-v1.png`
- **Prompt Summary：** 掌心尺度、方形铜质、穿绳鼻钮、暗色系带、不可读底面和简素木盒；中性博物馆式四视图。
- **Actual Review：** 结构、材料和握持通过；具体官职对应与印文保持未知。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-016｜LOC-002 无篷船定向返工

- **Output：** `assets/locations/LOC-002/southbound-waterway-boat-reference-v2.png`
- **Edit Scope：** 仅移除三处视图中的拱形编织篷与支架，保留水路、岸线、船体比例、桨位、行囊、光线与色彩；增加平放卷席作为便携物，不形成屋顶。
- **Actual Review：** 三处船体一致，开放式乘坐区可用，后世旅游小舟联想显著降低；仍保持“功能候选而非复原”标记。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜B1

- **Passed：** LOC-001 功能拓扑与 PRP-001 结构可供用户审核；三张均无人物、文字或水印污染。
- **Rework：** LOC-002 v1 已拒绝，v2 完成无篷低断言返工。
- **Decision：** 等待用户确认 LOC-001、LOC-002 v2 与 PRP-001；未确认前不组合人物或进入镜头。

## USER REVIEW｜B1

- **Date：** 2026-09-22
- **Decision：** 用户接受 LOC-001、LOC-002 v2 与 PRP-001 的视觉和功能方向。
- **Approval Scope：** 西晋官署的行动拓扑、无篷小型人力木舟方向，以及铜印的尺度、鼻钮、系带和握持关系。
- **Continuing Caveat：** 三项均为研究范围内的创作候选，不升级为张翰实际官署、船型或官印的精确复原。

## LOCATION & PROP BATCH｜B2

- **Run Date：** 2026-09-22
- **Mode：** Built-in image generation / targeted image edit
- **Purpose：** 生成陶渊明段所需的县衙工作间、归家路径及公务文书与旧家书候选；不是剧情镜头、分镜或正式史料复刻。
- **Evidence Boundary：** 晋代已有纸本书写传统，可支持纸作为材料范围；这不能证明陶渊明家书或彭泽公务文书的具体形制和文字。所有空间均按剧情动作建立低断言功能拓扑。
- **Research Entry Points：** 故宫博物院《平复帖》藏品资料；故宫博物院《出师颂》的艺术定位。

### GEN-017｜LOC-003 东晋彭泽县衙工作空间候选

- **Output：** `assets/locations/LOC-003/pengze-office-spatial-reference-v1.png`
- **Prompt Summary：** 同一小尺度地方行政工作间的案后看门口、门口反看工作案和俯视拓扑；低案、席、印信、未完文书、旧家书、收纳与门外等待点；黄昏自然光。
- **Actual Review：** 三向功能锚点可追认，空间尺度克制，与张翰官署形成区别；无人物、公堂、匾额、刑具或水印。家具和建筑细节仍是研究推定。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-018｜LOC-004 陶渊明归家路径与居所候选

- **Output：** `assets/locations/LOC-004/tao-home-path-spatial-reference-v1.png`
- **Prompt Summary：** 同一朴素、有人居住的乡居家门与窄径；正向、反向和俯视关系；门槛、行囊落点、儿童等待位、有限松菊、杂草、水缸、柴与篮筐；清晨自然光。
- **Actual Review：** 房屋可居住但不豪华，路径和动作点清楚，未做废墟、花海、酒意象或仙境；松菊与居所结构仅为克制艺术加工。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-019｜PRP-002 公务文书与旧家书组

- **Output：** `assets/props/PRP-002/tao-documents-family-letter-reference-v1.png`
- **Prompt Summary：** 中性四联道具板；浅色纤维纸、正式文书束、素木压板与系绳、反复折叠且较柔软的私人家书；排除卷轴、收藏印和藏宝图式做旧。
- **Internal Rework：** 初版出现过于接近可辨认书法的字迹，存在伪造文献感，未归档为正式候选；定向编辑仅将所有字迹改为极淡、稀疏、不可辨识墨痕，保留材质、折痕、木板和系束。
- **Actual Review：** 公务与私人载体的使用状态可区分；无可辨识姓名、名句、日期、印章或真实文字。材料仍只代表晋代纸本范围候选。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜B2

- **Passed：** LOC-003 与 LOC-004 的正反/俯视拓扑可服务 S003、S004 动作；PRP-002 经返工后消除了伪造书法风险。三张均无人物与水印污染。
- **Open：** LOC-003 家具与院落关系、LOC-004 的诗意程度、PRP-002 的具体形制均需用户确认；历史边界保持为范围候选。
- **Decision：** 三张作为 B2 候选提交用户复核；通过后进入王献之段空间与核心书写道具，不提前组合成剧情镜头。

## CREATIVE DIRECTION UPDATE｜PRP-002

- **Date：** 2026-09-22
- **User Direction：** 真实可读的书法没有问题，整体创作应允许更大胆的艺术创新。
- **Boundary Update：** 可读书法从风险项改为主动叙事手段；仍需把原创道具文字与史料引文、人物真迹明确区分。

### GEN-020｜PRP-002 创作书法版 v2

- **Output：** `assets/props/PRP-002/tao-documents-family-letter-reference-v2.png`
- **Mode：** Built-in image generation / precise object edit
- **Prompt Summary：** 保留 v1 四联布局、纤维纸、木板、系绳与折叠关系；恢复真实毛笔书写感。家书使用原创三列“家中粗安、兒常候門、願君早歸”，笔势亲密克制；公务文书更整齐、更密，形成公私反差。
- **Actual Review：** 家书三列可读且情绪明确，公私书写层级成立；公务纸上的次要文字仍带生成字形风险，不能直接用于停留时间较长的特写。
- **Status：** GENERATED_PENDING_REVIEW

## LOCATION & PROP BATCH｜B3

- **Review Date：** 2026-09-23
- **Mode：** USER_GENERATE → REVIEW
- **Prompt Source：** `assets/prompts/phase-b3-wang-prompt-pack.md`
- **Purpose：** 审核并归档用户依据提示词手动生成的王献之段四项空间与书写资产；Codex 未重复调用生图工具。
- **Shared Boundary：** 四项均为东晋范围内的电影艺术重构，不宣称王献之宅邸、书写工具或道教章表的精确复原；生成书法必须在成片近景前逐字校对。

### GEN-021｜LOC-005 王献之书斋与公职过渡空间

- **User Source：** `ChatGPT Image 2026年9月23日 07_36_11 (1).png`
- **Output：** `assets/locations/LOC-005/wang-study-public-transition-reference-v1.png`
- **Actual Review：** 正向、反向和俯视拓扑中的低案、公文、水盆、素布、收纳与出口基本一致；明亮、克制、可通行，没有明清书房陈列。俯视比例偏狭长，后续只锁功能锚点，不锁绝对尺寸。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-022｜PRP-003 盛年书写工具与功能性长纸

- **User Source：** `ChatGPT Image 2026年9月23日 07_36_11 (2).png`
- **Output：** `assets/props/PRP-003/wang-writing-tools-long-sheet-reference-v1.png`
- **Actual Review：** 工具分件、新墨、横向长纸和双端木板托举关系成立；没有装裱、收藏印或悬挂卷轴。书法只能作为笔势与材料参考，未经校字不能作为成片近景。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-023｜LOC-006 王献之病榻与章表空间

- **User Source：** `ChatGPT Image 2026年9月23日 07_36_11 (3).png`
- **Output：** `assets/locations/LOC-006/wang-sickroom-ritual-space-reference-v1.png`
- **Actual Review：** 病榻、现用书写区、独立旧砚、灯和沿墙守候区可辨，夜间材料仍清楚，无灵异仪式和现代床具。两处灯与花枝略显精致，正式镜头需控制注意力。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-024｜PRP-004 临终章表、现用笔砚与干涸旧砚

- **User Source：** `ChatGPT Image 2026年9月23日 07_36_11 (4).png`
- **Output：** `assets/props/PRP-004/wang-ritual-writing-dry-inkstone-reference-v1.png`
- **Actual Review：** 湿润现用砚、悬笔与独立干涸旧砚形成清楚对照；旧砚三向和空间距离关系可用。章表标题“上章首過”没有可靠呈现，正式近景须重做准确文字层。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜B3

- **Passed：** 四项均与资产 ID 正确对应，空间和道具功能逻辑成立；白日开放书斋与夜间收缩病室形成清楚反差，新墨与干涸旧砚也能一眼区分。
- **Open：** LOC-005 绝对比例、LOC-006 灯与花枝的注意力，以及 PRP-003/004 的逐字书法仍未锁定。
- **Decision：** 归档为用户手动生成、自审通过的候选资产；等待用户决定是否批准视觉方向。文字问题不触发自动返工。

## USER REVIEW｜B3

- **Date：** 2026-09-23
- **Decision：** 用户确认四张均“没问题”，LOC-005、LOC-006、PRP-003、PRP-004 升级为 APPROVED。
- **Approval Scope：** 空间拓扑、功能分区、材料关系、白日/夜间反差、新墨/干砚反差及整体视觉方向。
- **Continuing Caveat：** PRP-003 与 PRP-004 的纸面书法不视为逐字批准；成片若使用可停留阅读的近景，须另做准确书法层并校对。

## USER REVIEW｜B2 CLOSURE

- **Date：** 2026-09-23
- **Decision：** 结合用户对 B2 的反馈以及对 PRP-002 创作书法版的明确确认，LOC-003、LOC-004、PRP-002 升级为 APPROVED。
- **Approval Scope：** 彭泽工作间与陶宅的功能拓扑、生活化诗意程度、纸张材料、公私文书反差和原创家书书法方向。
- **Continuing Caveat：** 空间与文书形制属于历史范围内艺术重构；“家中粗安、兒常候門、願君早歸”为电影原创道具文字，不是陶渊明史料原文。

## COSTUME BATCH｜C1

- **Run Date：** 2026-09-23
- **Mode：** Built-in image generation / identity-preserving targeted edit
- **Prompt Source：** `assets/prompts/costume-prompt-pack-v1.md`
- **Purpose：** 生成三位核心人物的三状态服装参考板；不是剧情镜头或服制考古复原图。

### GEN-025｜CST-001 张翰服装状态板

- **Output：** `assets/costumes/CST-001/zhang-han-costume-state-reference-v1.png`
- **Prompt Summary：** 锁定已批准张翰面貌与体态，建立西晋属官在职、离任和水路归途三状态的同层增减关系。
- **Internal Rework：** 初版冠体偏高、归途衣摆有不必要的破损感；定向降低冠高并修复衣摆，使归途保持完整、主动而不落魄。
- **Actual Review：** 身份、体态和衣层连续性通过；具体一梁冠形制与官服色相仍为研究推定。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-026｜CST-002 陶渊明服装状态板

- **Output：** `assets/costumes/CST-002/tao-yuanming-costume-state-reference-v1.png`
- **Prompt Summary：** 锁定已批准陶渊明面貌与清瘦体态，建立县令、离任和归家三状态；生活化但不贫困化、仙人化。
- **Internal Rework：** 初版县令冠体偏高；定向压低冠体并保持三状态基础衣层连续。
- **Actual Review：** 人物连续性和生活质感通过；三状态差异有意克制，冠式与宽衫比例仍为研究推定。
- **Status：** GENERATED_PENDING_REVIEW

### GEN-027｜CST-003 王献之服装状态板

- **Output：** `assets/costumes/CST-003/wang-xianzhi-costume-state-reference-v1.png`
- **Prompt Summary：** 锁定已批准王献之面貌与年龄连续性，建立盛年书写、公职和病中三状态；正式层采用两梁冠、绛服、墨绶和水苍玉的低断言方向。
- **Internal Rework：** 初版正式冠体偏高；定向降低冠高，保留可读但克制的制度轮廓。
- **Actual Review：** 三状态身份与衣层逻辑通过，无帝王化、婚礼化或现代病号服；具体两梁结构和佩挂制度仍为研究推定。
- **Status：** GENERATED_PENDING_REVIEW

## BATCH REVIEW｜C1

- **Passed：** 三张服装板均保持已批准人物身份、体态与年龄连续性；状态间衣层增减可解释，没有文字、水印、多余肢体或明显时代串用。
- **Open：** 冠式、制度色、绶带与玉佩的精确形态仍属研究推定，当前批准请求仅针对电影视觉与功能方向。
- **Decision：** 三张完成内部定向修正并提交用户复核；用户确认前不升级为 APPROVED，也不组合进入剧情镜头。

## USER REVIEW｜C1

- **Date：** 2026-09-23
- **Decision：** 用户确认三张服装状态板“没问题”，CST-001、CST-002、CST-003 升级为 APPROVED。
- **Approval Scope：** 三位人物的身份辨识、服装视觉方向、在职/离任/归途、县令/离任/归家以及书写/公职/病中的衣层变化与穿脱逻辑。
- **Continuing Caveat：** 一梁冠、县令冠式、两梁冠、制度色、墨绶和玉佩佩挂方式仍属于历史范围内的研究推定，不作为晋代冠服制度的精确复原依据。
