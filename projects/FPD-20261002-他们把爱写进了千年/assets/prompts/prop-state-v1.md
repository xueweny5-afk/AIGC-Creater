# PROP-01｜四组关键道具与状态图

**模式：USER_GENERATE / PARTIAL。** 这些是独立道具图，不是镜头图。先批准每件基础道具，再用原图编辑派生状态。道具位置和手部接触在后续分镜阶段组合检查。

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

四件基础图均已放入 `assets/props/<PROP ID>/`。当前只执行 `remaining-assets-handoff-v1.md` 中列出的状态图与材料细节；按 PROP ID 回传审核，避免四组道具混淆。

## 材料细节板（基础图通过后再做）

- **PROP01-detail-paper-v1.png：** 上传已批准 `assets/props/PROP01/flat-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一碑拓提取纸角与纸面的近观察材料板，保持纸纤维、厚度、墨痕分布和同一角的位置；展示可以卷起又按平的边缘结构。无手、无人物、无可读汉字。」目标 `assets/props/PROP01/detail-paper-v1.png`；附加共同负面约束。
- **PROP02-detail-page-v1.png：** 上传已批准 `assets/props/PROP02/open-page-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一本打开书册提取指定页的纸张、书脊与边缘材料板；保持原本页方向、厚度和翻阅磨痕，不新增可读文字或换页。」目标 `assets/props/PROP02/detail-page-v1.png`；附加共同负面约束。
- **PROP03-detail-fold-v1.png：** 上传已批准 `assets/props/PROP03/folded-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一封未展折信提取折线、纸厚和边缘压痕的材料板；保持折叠方式和一手可持尺度，不展开、不加封印或可读字。」目标 `assets/props/PROP03/detail-fold-v1.png`；附加共同负面约束。
- **PROP04-detail-ceramic-v1.png：** 上传已批准 `assets/props/PROP04/two-bowls-v1.png`（MATERIAL / EDIT TARGET）。提示词：「从同一组两只陶瓷碗和筷子提取碗口、釉面、碗底接触和筷尖材料板；两碗材质与尺寸一致，局部反光柔和，食物尺度可信，不改碗数或左右归属。」目标 `assets/props/PROP04/detail-ceramic-v1.png`；附加共同负面约束。
