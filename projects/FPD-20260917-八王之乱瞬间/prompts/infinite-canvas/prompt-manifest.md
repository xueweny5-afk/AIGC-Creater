# 《洛阳无赢家》无限画布 Prompt Manifest

## Package Identity

- Project：`FPD-20260917-八王之乱瞬间`
- Package：`infinite-canvas-i2v-v1`
- 状态：`READY FOR TECHNICAL PILOT`
- 访问日期：2026-09-27
- 母版：`storyboard/storyboard-plan.md`、`storyboard/frame-manifest.md`、`motion/motion-spec.md`

## Model Profile Receipt

| 平台 | 已核实能力 | 本项目使用方式 | 未锁定项 |
|---|---|---|---|
| RunningHub rhTV／悠船 | 官方支持单图起始或首尾双帧；单次 5 秒；480p/720p；运动强度参数 | 单图 I2V；SH19、SH20 使用首尾帧；统一低运动 | 画布中具体可选模型会变化 |
| 小云雀 Web | 官方提供自由画布、Seedance 系列视频生成、图片/视频混合参考和运镜库 | 单图或首尾帧；选择低幅度运镜 | 具体账户可见版本、时长和分辨率 |
| LibTV | 官方提供无限画布、自由编排、智能 Agent 与多视频模型聚合 | 在画布中建立图片→视频节点；按当前所选模型使用单图或首尾帧 | 具体模型的时长、分辨率、参考帧和负向词支持需现场确认 |

资料来源：

- https://rhtv.runninghub.cn/runninghub-api-doc-cn/api-448183081
- https://www.runninghub.cn/
- https://xyq.jianying.com/tutorials/web-manual
- https://xyq.jianying.com/tutorials/creation-agent-canvas
- https://www.liblib.tv/wappro?sourceid=040004

## 通用参数

- 画幅：9:16。
- 生成时长：优先 5 秒；剪辑取计划时长，不用提示词强迫模型在 3 秒内完成复杂动作。
- 运动强度：低；SH03、SH12A 可用中低。
- 清晰度：试片 720p；锁定可用 Take 后再做高清或超分。
- 音频：生成阶段关闭或忽略，旁白、音效和音乐在后期完成。
- 字幕／地图姓名：全部后期添加，不让视频模型生成文字。
- 负向提示词：平台有独立负向栏时使用；没有时追加在正文末尾。

## 输入文件映射

| Unit | 模式 | 输入文件（相对项目根目录） | 计划成片 |
|---|---|---|---:|
| SH01 | 单图 | `assets/locations/S01-洛阳城门/S01-洛阳城门-晨雾-v1.png` | 3s |
| SH02 | 单图 | `storyboard/frames/SH02-骑兵入洛阳/SH02-骑兵入洛阳-v1.png` | 3s |
| SH03 | 单图 | `storyboard/frames/SH03-马蹄与百姓避让/SH03-马蹄与百姓避让-v2.png` | 4s |
| SH04A | 单图 | `assets/props/P02-青纸诏/P02-青纸诏-雨中-v2.png` | 3s |
| SH04B | 单图 | `storyboard/frames/SH04B-宫门闭合/SH04B-宫门闭合-v1.png` | 2s |
| SH05 | 单图 | `storyboard/frames/SH05-晋惠帝独坐空殿/SH05-晋惠帝独坐空殿-v1.png` | 3s |
| SH06 | 单图 | `storyboard/frames/SH06-晋惠帝与群臣影子/SH06-晋惠帝与群臣影子-v1.png` | 4s |
| SH07 | 单图 | `assets/props/P06-八王形势地图/P06-八王形势地图-无文字-v1.png` | 4s |
| SH08 | 单图 | `storyboard/frames/SH08-八王合围洛阳/SH08-八王合围洛阳-v1.png` | 4s |
| SH09 | 单图 | `storyboard/frames/SH09-司马伦取玺/SH09-司马伦取玺-v1.png` | 3s |
| SH10 | 单图 | `storyboard/frames/SH10-司马伦登阶/SH10-司马伦登阶-v1.png` | 3s |
| SH11 | 单图＋后期路线 | `assets/props/P06-八王形势地图/P06-八王形势地图-无文字-v1.png` | 4s |
| SH12A | 单图 | `storyboard/frames/SH12A-荒野骑兵/SH12A-荒野骑兵-v2.png` | 2s |
| SH12B | 单图 | `storyboard/frames/SH12B-玉玺易手/SH12B-玉玺易手-v1.png` | 3s |
| SH13 | 单图 | `storyboard/frames/SH13-晋惠帝车内/SH13-晋惠帝车内-v1.png` | 3s |
| SH14 | 单图 | `storyboard/frames/SH14-车驾离城/SH14-车驾离城-v2.png` | 4s |
| SH15 | 单图 | `assets/locations/S07-荒田与流民道路/S07-荒田与流民道路-v1.png` | 4s |
| SH16 | 单图 | `storyboard/frames/SH16-母子走入流民队伍/SH16-母子走入流民队伍-v1.png` | 4s |
| SH17 | 单图 | `storyboard/frames/SH17-八王棋子暗下/SH17-八王棋子暗下-v1.png` | 3s |
| SH18 | 单图 | `storyboard/frames/SH18-空殿玉玺/SH18-空殿玉玺-v1.png` | 3s |
| SH19 | 首尾帧 | START `storyboard/frames/SH19-城外纯黑/SH19-城外纯黑-v1.png`；END `storyboard/frames/SH20A-远方单个火点/SH20A-远方单个火点-v1.png` | 3s |
| SH20 | 首尾帧 | START `storyboard/frames/SH20A-远方单个火点/SH20A-远方单个火点-v1.png`；END `storyboard/frames/SH20B-远方密集火线/SH20B-远方密集火线-v1.png` | 3s |
| SH21 | 单图＋后期黑场 | `assets/characters/C06-洛阳守城军士/C06-洛阳守城军士-火光-v1.png` | 3s |

## 生产顺序

### TECHNICAL_PILOT

1. SH20：首尾帧锁机位。
2. SH13：晋惠帝身份稳定。
3. SH03：马腿与泥水。
4. SH09：手与玉玺。
5. SH21：守军手、脸和火光。

### PRODUCTION

试片通过后按 SH01→SH21 顺序生成。每镜先出 2 个候选，低风险镜头选 1 条；高风险镜头最多补 2 轮，仍失败则执行 Prompt Package 中的简化方案。
