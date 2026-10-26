# Prompt Coverage Receipt｜生成前版本

> **STALE / NOT A CURRENT RECEIPT。** 源版本仍是旧 screenplay-master v2 与旧 Shot/Motion；G2 v3 通过后须从新版批准源重新编译。

覆盖范围：S01–S08；源版本为 `screenplay-master.md v2`、`shot-list.md v2`、`frame-manifest.md v2`、`motion-spec.md v2`。目标模型未定，故为模型中立的可审查合同，不声明 G5 通过。

| 13 项框架 | 落点 | 处理 |
|---|---|---|
| 1 输入与参考锚定 | `../storyboard/frame-manifest.md`；提示词包逐镜输入 | 八张独立首帧为硬锚点；旧上下复合图只作溯源 |
| 2 概念与叙事命题 | `../project-brief.md`、`../story/story-blueprint.md` | 双人温馨突然切为同物一人；四组独立 |
| 3 动态 | `../motion/motion-spec.md`、提示词包逐镜动作 | 每镜一个可见主动作，避免模型内消失 |
| 4 画面质感 | `../visual-development/world-visual-bible.md`、首帧 | 保留自然材质与既有首帧；不写未经验证的摄影参数 |
| 5 镜头语言 | `../direction/shot-list.md` | 各镜锁定首帧机位，以同物同地识别前后；硬切由剪辑完成 |
| 6 场景 | `../direction/scene-design-pack.md`、`../assets/asset-manifest.md` | 每组空间与主道具独立 |
| 7 色彩风格 | `../visual-development/world-visual-bible.md` | 前镜偏暖、后镜较冷，不能让色差毁掉同地辨认 |
| 8 光影 | `../visual-development/world-visual-bible.md`、首帧 | 继承原有光源；只允许灯火/窗光微动 |
| 9 构图空间 | 八张首帧、`../direction/shot-continuity-ledger.md` | 空席/空碗为后镜视觉中心；深色留白不延展 |
| 10 可观察表演 | `../motion/motion-spec.md` | 指尖轻移、托腮侧目、慢行、看向空碗等不同微动作 |
| 11 时间与衔接 | `../storyboard/animatic/rhythm-map.md`、`../screenplay/screenplay-master.md` | 8×3 秒闭合；每对前镜动作未完时以同物件硬切 |
| 12 声音 | 剧本与 `../storyboard/animatic/rhythm-map.md` | 声音骤停/留白在后期；未假定模型有同步音频 |
| 13 连续性与排除 | `../direction/shot-continuity-ledger.md`、提示词包统一合同/逐镜禁项 | 锁人、衣、道具、空间、轴线；拒绝幽灵、多余手指、乱码文字 |

**压缩原则：** 输入首帧已携带的构图、脸、衣服和光色不逐字重述；每条提示词只写首帧之后的运动与最关键风险。模型能力、负向字段和时长设置待选定平台后编译，记录在 `../generation/generation-manifest.md`。

**创作取舍：** 对冲击力，选择“温馨动作未完时突切空位”。观众先以同一物件认出前后关系，再读到人的缺席；现有静帧的手势和人物站位不构成严格动作匹配，需要未来成对试镜验证突切是否顺畅。
