# Stage 11 静态分镜生图交接｜v3

**项目：** FPD-20261002-他们把爱写进了千年  
**状态：** `USER_GENERATE HANDOFF / FRAMES NOT YET RECEIVED / G4 PENDING`  
**上游锁定：** `composition-guides-v3.md`、`../direction/shot-list.md` v3、`../assets/asset-manifest.md` v9。此包只制作静态分镜关键帧，不生成视频。

> **2026-10-12 历史交接说明：** 八张 `S01–S08-key-v2.png` 已全部生成并获用户画面认可。本文件下方 SH07 仍为生成前的旧“陈给沈夹菜”提示词，现已被**沈给陈夹菜**的剧本与实际帧取代，禁止继续复制它生成当前版。当前逐镜来源是 `frame-manifest.md`、`../direction/shot-list.md` 和 `../qc/g4-static-review-2026-10-12.md`。

## 使用方法

资产路径均相对本项目 `assets/`。按每张卡的顺序上传参考图，并明确告诉生图工具参考角色：`IDENTITY` 锁脸、`WARDROBE` 锁发型身形衣服、`TOPOLOGY` 锁已见空间、`PROP` 锁道具形制、`COMPOSITION` 只锁画面边界。旧 `Sxx-start-v1.png` 只作版式参考，不能作为人物身份参考。生成输出为 **9:16 竖屏**，中部横向叙事画面与上下深色留白；若平台可选尺寸，用 1080×1920。模型、参考权重和种子由你实际使用的平台决定，尚未验证，不写虚构参数。

**生成顺序：** SH01→SH02；SH03→SH04；SH05→SH06；SH07→SH08。每组先检查双人帧，再将双人帧作为后镜的构图编辑底图。后镜应是“同场所后来发生的独立画面”，不是在前镜内抹掉一个人；必须依其独立身份、服装与状态图重画人物和手势。

**2026-10-12 年龄状态补充：** 四位留下者的 `later-face-front-v1.png` 已入库并按 `../qc/later-age-state-review-2026-10-12.md` 复核。原 Canon Face 锁身份，后来状态图只锁脸部/发丝年龄，组合图和 CST 资产锁衣服；后来状态照中的新衣服不得进入分镜。SH02/04/06/08 必须有可见年龄变化，不能沿用前镜年轻容貌。已生成但未做到的旧分镜须返工，不能因文件存在而跳过。

**共同退回标准：** 脸与定妆母图不符；服装/发型前后漂移；左右位置、桌缘/路缘、窗/圆门/灯位或镜头角度变化；手指数量/左右手错误；物件位置变化；画出可读字、字幕、鬼影、分屏、同镜消失、无来源的蓝光或浓雾。双人/单人配对叠图检视；若发生这些问题，先改失败镜头，不改已通过母图。

## CG-F01｜李清照与赵明诚

### SH01 / S001｜双人按纸｜输出 `frames/F01-li-zhao/S01-key-v2.png`

**上传参考（按角色）：** `characters/CH01/canon-face-front-v2.png`（李 IDENTITY）、`characters/CH02/canon-face-front-v2.png`（赵 IDENTITY）、`characters/CH01/combined-CST01-front-v1.png` 与 `characters/CH02/combined-CST02-front-v1.png`（WARDROBE）、`locations/LOC01/topology-main-v1.png`（TOPOLOGY）、`props/PROP01/corner-curled-v1.png`（PROP）、`storyboard/frames/F01-li-zhao/S01-start-v1.png`（COMPOSITION，仅版式；此路径相对项目根目录）。

**主提示词（复制）：**
> 电影写实静态分镜关键帧，9:16 竖屏画布，中部横向电影叙事区，上下深色留白。宋代语境的书房夜景，只使用场景参考中可见的书案、后左书架、后右格窗和同位置灯火。固定正面中景，李清照在画面左、赵明诚在画面右，二人身份和衣装严格依各自参考图。桌面中区是一张碑拓，只有画面右上角微微卷起。抓取“帮我按住”刚说出、动作刚被回应的瞬间：李清照右手按住碑拓中部并朝右上角推纸，目光仍落在纸上；赵明诚用靠近卷角的左手伸来按住同一个角。两人的手、纸角、彼此关系清楚可读，动作温暖而克制。原有灯位照亮纸面和手指，纸、木、衣料质感真实；干净空气。画面不写对白，留出后期字幕安全区。

**负面提示词（复制）：**
> 不要托腮、指着旧卷、不相干的道具、第三人、脸部漂移、换衣换发型、畸形手、额外手指、左右手颠倒、两个卷角、可读碑文、字幕、水印、分屏、鬼影、过度磨皮、舞台光、蓝色悲伤滤镜、雾、未知背墙。

**核对：** 李左赵右；李右手、赵左手在同一右上角；书案/窗/灯有可复用坐标。通过后再做 SH02。

### SH02 / S002｜李独按纸｜输出 `frames/F01-li-zhao/S02-key-v2.png`

**上传参考：** 前镜 `storyboard/frames/F01-li-zhao/S01-key-v2.png`（COMPOSITION ONLY，需先修正动作）；`characters/CH01/canon-face-front-v2.png`（IDENTITY）；`characters/CH01/later-face-front-v1.png`（LATER AGE FACE ONLY）；`characters/CH01/combined-CST01-front-v1.png`（WARDROBE）；`locations/LOC01/topology-main-v1.png`（TOPOLOGY）；`props/PROP01/corner-curled-v1.png`（PROP）。

**主提示词（复制）：**
> 以修正通过的 SH01 双人关键帧作构图和空间底图，制作同一书房后来发生的独立静态镜头。9:16 竖屏，中部横向叙事区和上下深色留白保持原样。摄影机、焦距感、景别、桌缘、后左书架、后右格窗与灯位、碑拓的位置严格匹配 SH01。赵明诚原先的画面右侧位置现在真实地空着，没有任何人影。李清照仍在画面左，身份依原 Canon Face，脸部与发丝依后来年龄状态照，衣服严格依 CST01 定妆图，不复制年龄状态照中的新衣服；同一张碑拓的画面右上角再次卷起。李先望向右侧空位，随后自己用右手伸到同一右上角按住纸。抓取右手刚按住纸角、目光仍指向空位的瞬间。灯位不动，室内可较静较暗，纸角和手仍清楚；没有镜内消失效果。无生成字幕。

**负面提示词（复制）：**
> 不要赵明诚、第三人、透明人物、鬼影、分屏、抹除残影、托腮、另一只手代按、改卷角位置、改桌窗灯机位、换衣换脸、畸形手、可读文字、字幕、水印、蓝色滤镜、雾。

**核对：** 叠在 SH01 上看右席、纸角、桌缘、灯窗是否对齐；右侧必须真正空。

## CG-F02｜苏轼与王弗

### SH03 / S003｜王指书页｜输出 `frames/F02-su-wang/S03-key-v2.png`

**上传参考：** `characters/CH03/canon-face-front-v2.png`（苏 IDENTITY）、`characters/CH04/canon-face-front-v2.png`（王 IDENTITY）、`characters/CH03/combined-CST03-front-v1.png` 与 `characters/CH04/combined-CST04-front-v1.png`（WARDROBE）、`locations/LOC02/topology-main-v1.png`（TOPOLOGY）、`props/PROP02/open-page-v1.png`（PROP）、`storyboard/frames/F02-su-wang/S03-start-v1.png`（COMPOSITION，仅版式）。

**主提示词（复制）：**
> 电影写实静态分镜关键帧，9:16 竖屏，中部横向叙事区、上下深色留白。宋代语境的室内书桌夜景，只画场景主视已证明的书桌、两把椅子、窗与原有室内灯位。固定桌前正面中景，苏轼画面左，王弗画面右，容貌、发型、衣服与定妆参考一致。桌面中间摊着同一本书，页码和纸张外形固定，书中文字不可辨。王弗用靠近书页的左手指向**右页中部的一列**，刚说出“在这一页”；苏轼先沿她手指看向该列，正抬眼看她。选指尖、书页和苏的回应都清楚的瞬间，关系温和自然，不长时间凝望。纸页受同一灯位柔和照亮，真实纸和木材质，清洁空气。无画面内文字或字幕。

**负面提示词（复制）：**
> 不要翻页、指左页、改为右手指、苏轼托腮、第三人、换座位、改书桌或椅子位置、畸形手、可读书文、印刷诗句、字幕、水印、分屏、鬼影、蓝色滤镜、雾。

**核对：** 苏左王右；王左手指右页中部；两椅与书可在后镜原样复用。

### SH04 / S004｜苏指同一列｜输出 `frames/F02-su-wang/S04-key-v2.png`

**上传参考：** 前镜 `storyboard/frames/F02-su-wang/S03-key-v2.png`（COMPOSITION ONLY，需先修正）；`characters/CH03/canon-face-front-v2.png`（IDENTITY）；`characters/CH03/later-face-front-v1.png`（LATER AGE FACE ONLY）；`characters/CH03/combined-CST03-front-v1.png`（WARDROBE）；`locations/LOC02/topology-main-v1.png`（TOPOLOGY）；`props/PROP02/open-page-v1.png`（PROP）。

**主提示词（复制）：**
> 用修正通过的 SH03 作构图底图，制作同一书房后来发生的独立静态镜头。9:16 竖屏中部横向叙事区及上下留白、机位、桌缘、书的开页、两椅、窗与灯位均与 SH03 精确相同。画面右侧王弗原先的椅子清楚可见但完全空着，绝无残影。苏轼在画面左，身份依原 Canon Face，成熟脸部与灰丝依后来年龄状态照，衣服严格依 CST03 定妆图，不复制状态照中的深色外衣。他用右手指尖停在那本书**右页中部同一竖列**，抬眼望向右边空椅；抓取目光刚离开书页而手指尚未离开的孤独瞬间。不翻页，不托腮。原灯位不变，环境可稍静稍暗，但手指、书页、空椅可读。后期才会加诗句，图中不生成字。

**负面提示词（复制）：**
> 不要王弗、第三人、鬼影、透明人、分屏、托腮、翻页、指另一页、改用左手、可读书文、诗句、字幕、水印、改椅书窗灯位置、换脸换衣、畸形手、蓝色滤镜、雾。

**核对：** 叠 SH03 检查右椅与右页同列对齐；空位和苏的视线都清楚。

## CG-F03｜陆游与唐婉

### SH05 / S005｜等等我｜输出 `frames/F03-lu-tang/S05-key-v2.png`

**上传参考：** `characters/CH05/canon-face-front-v1.png`（陆 IDENTITY）、`characters/CH06/canon-face-front-v1.png`（唐 IDENTITY）、`characters/CH05/combined-CST05-front-v1.png` 与 `characters/CH06/combined-CST06-front-v1.png`（WARDROBE）、`locations/LOC03/topology-main-v1.png`（TOPOLOGY）、`storyboard/frames/F03-lu-tang/S05-start-v1.png`（COMPOSITION，仅版式）。

**主提示词（复制）：**
> 电影写实静态分镜关键帧，9:16 竖屏，中部横向叙事区、上下深色留白。春日园中同一石径，从石径前景朝远处圆门拍摄的固定中景；桃枝在画面左上、假山在左侧、圆门在远处，严格沿场景主视中已见方向。陆游在前景偏左，唐婉在其右后方落后半步，二人的脸、发型和衣装严格依各自参考图。唐婉停下，刚说“等等我”，向陆游靠近；陆游正面对向镜头，向画面右后方回身，用自己的右手向她伸出。抓取两人的手即将接近、尚未握住的瞬间，视觉上有明确回应与期待。自然日光，地面和衣料质感真实，空气清洁；不添加未见园路和门外空间，无生成字幕。

**负面提示词（复制）：**
> 不要牵手完成、并排面向镜头行走、改人物左右、改回身方向、左手伸出、第三人、纸信出现在前镜、改圆门桃枝假山位置、未知门外景、畸形手、可读文字、字幕、水印、分屏、鬼影、飞花雨、浓雾、悲伤蓝滤镜。

**核对：** 陆前左、唐右后；陆右手伸出但未接触；圆门与路缘可在后镜复用。

### SH06 / S006｜无人接手｜输出 `frames/F03-lu-tang/S06-key-v2.png`

**上传参考：** 前镜 `storyboard/frames/F03-lu-tang/S05-key-v2.png`（COMPOSITION ONLY）；`characters/CH05/canon-face-front-v1.png`（IDENTITY）；`characters/CH05/later-face-front-v1.png`（LATER AGE FACE ONLY）；`characters/CH05/combined-CST05-front-v1.png`（WARDROBE）；`locations/LOC03/topology-main-v1.png`（TOPOLOGY）；`props/PROP03/folded-v1.png`（PROP）。

**主提示词（复制）：**
> 用已通过的 SH05 作构图底图，制作同一段春园石径后来发生的独立静态镜头。9:16 竖屏中部横向叙事区及上下留白、机位、陆游屏幕位置、路缘、左上桃枝、左侧假山、远处圆门与 SH05 对齐。唐婉原先站在画面右后方的位置完全空着，没有任何残影。陆游身份和衣装仍依母图，朝相同的画面右后方回身，仍用右手伸向原来唐婉的位置，动作停住；左手单独握着一封**未展开的折信**。抓取他意识到无人接手、右手尚未收回的瞬间，眼神落向空处。自然天光可比前镜略阴，但方向不变；纸信可辨，园门和石径仍可辨。后期才会加引文，图中不生成文字。

**负面提示词（复制）：**
> 不要唐婉、第三人、鬼影、透明人、分屏、左手伸向空处、右手拿信、展开信、可读信文、诗句、字幕、水印、改变圆门桃枝路缘、门外未知景、换脸换衣、畸形手、无因飞花、浓雾、蓝色滤镜。

**核对：** 叠 SH05 检查右后原位与景物对齐；陆仍以右手伸出，信仅在左手。

## CG-F04｜沈复与陈芸

### SH07 / S007｜尝尝这个｜输出 `frames/F04-shen-chen/S07-key-v2.png`

**上传参考：** `characters/CH07/canon-face-front-v1.png`（沈 IDENTITY）、`characters/CH08/canon-face-front-v1.png`（陈 IDENTITY）、`characters/CH07/combined-CST07-front-v1.png` 与 `characters/CH08/combined-CST08-front-v1.png`（WARDROBE）、`locations/LOC04/topology-main-v1.png`（TOPOLOGY）、`props/PROP04/two-bowls-v1.png`（PROP）、`storyboard/frames/F04-shen-chen/S07-start-v1.png`（COMPOSITION，仅版式）。

**主提示词（复制）：**
> 电影写实静态分镜关键帧，9:16 竖屏，中部横向叙事区、上下深色留白。清代语境的家居夜饭，固定饭桌正面中景；格窗和原有桌侧实用灯在场景主视证明的位置。沈复坐画面左、陈芸坐右，容貌发型衣装严格依各自母图。桌上始终两只陶碗：左边沈碗有饭，右边陈碗有少量青菜。陈芸用**她右手的一双筷子**从右碗夹起一口青菜，刚说“尝尝这个”，正把菜送入左碗；沈复用**他自己另外一双同材质筷子**微微抬筷望向她。抓取青菜刚落进沈碗、两双筷子和两碗都清楚可辨的温馨瞬间。参考道具图提供碗与筷的形制，按此形制复制成两双独立筷子，不能一双筷子同时出现在两人手中。灯位固定，陶碗和木桌真实低光泽，干净空气，无生成字幕。

**负面提示词（复制）：**
> 不要只出现一双共用筷子、额外第三双筷子、把菜送错碗、两碗左右交换、右碗空、陈芸用左手夹菜、沈复托腮、畸形手、第三人、换脸换衣、改灯窗桌缘、字幕、水印、分屏、鬼影、蓝色滤镜、雾。

**核对：** 沈左陈右；两碗两双筷，菜确实落入左碗；桌、格窗、灯可在后镜复用。

### SH08 / S008｜筷停空碗前｜输出 `frames/F04-shen-chen/S08-key-v2.png`

**上传参考：** 通过后的 `storyboard/frames/F04-shen-chen/S07-key-v2.png`（COMPOSITION / EDIT TARGET）；`characters/CH07/canon-face-front-v1.png`（IDENTITY）；`characters/CH07/later-face-front-v1.png`（LATER AGE FACE ONLY）；`characters/CH07/combined-CST07-front-v1.png`（WARDROBE）；`locations/LOC04/topology-main-v1.png`（TOPOLOGY）；`props/PROP04/opposite-empty-v1.png`（PROP）。

**主提示词（复制）：**
> 用已通过的 SH07 作构图底图，制作同一饭桌后来发生的独立静态镜头。9:16 竖屏中部横向叙事区及上下留白、正面机位、桌缘、格窗、灯位、左右两碗的大小与坐标都和 SH07 对齐。陈芸右侧座位现在完全空着，无幻影。左碗是沈复的碗，仍有饭和青菜；右碗是陈芸原来的碗，**完全空**。沈复坐左，身份衣装依母图，只用自己的那一双筷子，从左碗夹起一口青菜，向右空碗送去，却在碗沿前停住，菜尚未落入右碗。抓取筷子停在空碗前的最清晰瞬间，沈复没有托腮；让空位与空碗可被一眼看出。照明仍来自原灯位，可略暗，陶碗、筷、菜和手真实可辨；无生成文字。

**负面提示词（复制）：**
> 不要陈芸、第三人、鬼影、透明人、分屏、托腮、把菜放进右碗、右碗有饭或菜、交换左右碗、出现第二双悬空筷子、畸形手、改桌缘格窗灯位、换脸换衣、字幕、水印、蓝色滤镜、雾。

**核对：** 叠 SH07 检查双碗和右席坐标；右碗完全空，菜仍夹在沈的筷上，画面可留住空碗结束。

## 交回与下一关

把八张输出图按各卡的目标文件名放进对应 `storyboard/frames/F0x-.../` 文件夹；若先只完成一组，也按该组两张交回。提交时附平台/模型名称与实际使用的参考图（尤其后镜是否使用前镜作构图编辑）。我会按 `frame-manifest.md` 登记实图并逐对检查脸、衣装、机位、动作、灯光；必要时只返工失败帧。随后做八镜顺序预览、对白与硬切节奏复核。**新图未交回及审阅前，G4 不通过，Stage 12 运动设计不启动。**
