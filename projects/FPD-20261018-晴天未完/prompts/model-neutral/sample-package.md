# 《风进来的下午》提示词内容稿 v1.1

> 对当前v2需求状态：STALE。用户已反馈生成效果缺少参考感觉；原v1范围保留追溯，不继续叠加形容词修补。新版见[POV v2提示词](pov-v2-package.md)。下文CURRENT只表示历史v1内部来源曾一致，不适用于v2。

2026-10-18：按完整阶段主稿重新编译；取代v0.1对探索合稿的依赖。当前只交内容，不表示源合同获用户逐项批准。

## Package Identity

- Project：FPD-20261018-晴天未完；本轮仅文字交付，不提交生成任务。
- Package Status：CONTENT DRAFT。Unit Execution Status：NOT_READY；实际参考与平台能力：WAITING_DEPENDENCY。
- 使用 film-prompt-adapter 的内容草稿入口。以下正文可复制，未针对某一模型验证。

## Model Profile Receipt

Provider / Platform / Model-Version / Task Entry / API-UI Route / Account-Region Scope：OPEN。

Profile：UNVERIFIED；参考语义、时长、分辨率、画幅、音频、负向词及参数语法均未核实。本文件只给模型无关文字，不作平台兼容承诺。横版16:9、约12秒是创作目标，不是已验证支持值。

## Source Version Lock

[Brief](../../project-brief.md)、[Screenplay](../../screenplay/screenplay.fountain)、[Visual Bible](../../visual-development/world-visual-bible.md)、[Asset Manifest](../../assets/asset-manifest.md)、[Scene](../../direction/scene-design-pack.md)、[Shot](../../direction/shot-list.md)、[Storyboard](../../storyboard/storyboard-plan.md)、[Motion](../../motion/motion-spec.md)均v1.0；具体分镜状态见[Frame Manifest](../../storyboard/frame-manifest.md)。

IMG01来自S001-SH01-F01 v1.0合同；VID01来自S001-SH01-C01 v1.0 Motion合同。人物C01、服装COS01、场景LOC01、书P01、帘P02合同均v1.0；LOOK01/LIGHT01/AIR01 v1.0。Source Freshness：CURRENT，只表示文字版本与语义相符；实际资产和Frame均PLANNED、Approval Scope NONE。未采用公共Method或已验证生成Pattern。旧afternoon-sample.md仅保留探索历史，不再作事实源。

## Input File Map

当前无批准人物图、场景图或首帧图。IMG01为拟制作的起始画面逻辑单元，不是已经存在的文件；本稿不包含虚假路径或平台槽位。若走图生视频，应先取得符合IMG01构图与起始状态的画面，确认后才将其作为VID01的CURRENT START；此依赖不阻止本次文字交付。

逻辑参考职责沿F01合同：@IDENTITY_C01只锁人，@WARDROBE_COS01只锁衣着，@SCENE_LOC01只锁拓扑，@PROP_P01/P02锁形制/材料/当前状态，@POSE_CG01只锁构图；真实文件、上传序号、平台Token均UNKNOWN。实际Frame生成前还需CG01构图批准，不能以本段文字代替。F02仅作结束状态对照，当前不要求上传尾图。

## Prompt Units

### IMG01｜起始画面描述

单一静态时刻，内容草稿；无实际图像输出。

> 晴朗夏日下午的普通住宅房间，从室内斜看一扇开着的窗。浅奶白墙面，浅木地板，一位约二十多岁的成年女性坐在画面左侧中景的木椅上，黑色及肩发，米白棉质短袖、浅灰长裤，低头看摊开放在腿上的书，双手轻扶书本。画面右侧前景是一幅垂在窗边的白色纱帘，窗外可见安静绿地、清澈蓝天和柔和白云。侧向日光经窗进入，白墙反射柔和填充人物面部，地板上有一小片暖日光。蓝、绿、奶白和浅木色相互协调，肤色自然，窗外与白纱保留明暗层次。环境与人物同时可读，纱帘织纹、棉衣和木材质地清楚，亮边柔和，空气清透。

### VID01｜图生视频动作描述

启用条件：未来输入图符合IMG01起始状态，并确认目标入口支持对应图生视频任务。文字描述输入画面之后的动作。

> 延续起始画面的人物、衣着、房间、窗框和光线。人物起初安静低头看书，摊开的书留在腿上，双手始终轻扶。窗外一阵轻风将右侧白纱帘的下半部缓慢吹向室内，帘子仍悬挂在原处，让窗外绿地显露得更多。摄影机沿原视线缓慢向前靠近一小段，保持人物在左、纱帘在右的构图。人物注意到帘子的变化，先停顿片刻，再缓慢抬眼望向窗外，头部只小幅转动，神情放松。风势变小，纱帘缓慢落回窗侧。摄影机在结尾前停下，最后留出约三秒，看人物安静望着窗外。全程一个连续镜头，明亮清透，柔和高光中仍保留肤色、白布与云的细节。

### 约束备忘

全程一人，窗框、椅子、书和房间结构稳定；不翻页、不站起、不大幅转头；纱帘不穿过身体、不脱离悬挂处；镜头不旋转、不突然加速、不切换场景；不增加文字、水印、雾或发光粒子。这是验收与编译约束，不假设存在可直接粘贴的负向提示栏。

## Intent Preservation Map

| 要保护的意图 | 来源 | 承载点 | 缺口 |
|---|---|---|---|
| 明亮空间中独处的舒展感 | LOOK01/剧本v1.0 | IMG01环境与色彩，VID01结尾停留 | 未做画面与声画检查 |
| 人物和环境同时可读 | S001-SH01 / F01 v1.0 | IMG01斜向构图；VID01保持左右关系 | 首帧待补 |
| 风吹帘后才抬眼 | S001-SH01-C01 / PB01 v1.0 | VID01动作顺序 | 模型执行时序待验证 |
| 手、书、坐姿与空间稳定 | C01/P01/LOC01 | 两条正文及约束备忘 | 连续性待真实Take检查 |

## Prompt Coverage Receipt

MAPPED仅表示已进入文字，不表示已被模型执行。IMG01来源F01及其引用的Visual/Shot/Asset v1.0；VID01来源Motion v1.0，各合同范围见Source Version Lock。

| 项目 | IMG01 | VID01 |
|---|---|---|
| Reference anchors | RETURN：人物/场景用途尚未批准 | RETURN：首帧待补与批准 |
| Overall concept | MAPPED：明亮窗边阅读 | MAPPED：被来风吸引，转而望窗 |
| Dynamic description | NOT_APPLICABLE：单一时刻 | MAPPED：吹帘—停顿—抬眼—回落 |
| Image texture/cinematography intent | MAPPED：织纹、木材、柔和亮边 | MAPPED：继承清透、保留细节 |
| Shot language | MAPPED：室内斜向环境中景 | MAPPED：缓慢前移并停止 |
| Scene | MAPPED：住宅窗边及绿地 | MAPPED：保持起始场景 |
| Color/style | MAPPED：蓝绿奶白木色 | MAPPED：继承起始颜色 |
| Light | MAPPED：侧向日光和墙面反射 | MAPPED：光照状态保持 |
| Composition | MAPPED：左人右帘、窗外可读 | MAPPED：保持左右关系 |
| Emotion/observable performance | MAPPED：低头看书 | MAPPED：停顿后抬眼、保持观看 |
| Shot timeline | NOT_APPLICABLE | MAPPED：顺序过程与末尾停留；精确12秒外部控制待核实 |
| Sound | NOT_APPLICABLE | NOT_APPLICABLE：本视频视觉Prompt不承担声音，见声音后期意图 |
| Exclusions | MAPPED：约束备忘 | MAPPED：约束备忘，真实平台语法待核实 |

## Compatibility & Degradation

若平台时长、画幅、参考或动作控制无法承载本稿，先记录实际差异再适配，不自动压缩结尾停留或增加剪辑。当前不宣称某项能力SUPPORTED/UNSUPPORTED。声音走后期意图：轻风、细微布料声、远鸟声，无对白，首版不加音乐。

## Reverse-check

文字反查可恢复：一位成年女性在住宅窗边阅读；风吹起帘子后停顿抬眼；摄影机短距离前移后停止；结尾望窗，书与手保持。人物身份、空间像素、平台控制和实际效果未评估。

Prompt Review：NOT_EVALUATED（完整输入组合缺实际参考与Profile）；仅完成正文与当前探索主稿的一致性检查。

## Generation Order

本轮NONE。未来仅在获得生成授权并补齐对应依赖后，先批准当前所需资产用途和CG01，再检验IMG01构图、肤色与室内外亮度，再做VID01代表样例；首次使用具体模型/人物方案时按Shot中的H01—H03组织TECHNICAL_PILOT，不直接进入PRODUCTION。未产Take，未写QC通过。

单元卡见[production-unit-cards.md](production-unit-cards.md)，只从上述合同汇总，不作为独立事实源。

## Decision Register

- LOCKED：文字交付、沿用现有Project ID、不调用图片或视频生成。
- ASSUMED：窗边样例、成年女性、单镜头约12秒、横版16:9，均供用户审阅。创作权来源为各上游v1.0的CREATIVE_PROPOSAL，不将当前提案填为用户LOCKED。
- OPEN：具体人物外观、首帧、模型平台与实际规格、后期声音素材。

## Next Stage

用户审阅本样例表达后，按其反馈修正创作主稿，再完成对应上游文字与实际生成依赖；本内容稿不表示生产Gate通过。
