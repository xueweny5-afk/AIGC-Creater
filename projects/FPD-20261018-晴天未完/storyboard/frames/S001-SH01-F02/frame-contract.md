# FRAME CONTRACT

- Frame ID：S001-SH01-F02；Source Shot：S001-SH01；Source Scene：S001/B01—B03；Type：END_KEYFRAME；Version：v1.0；Status：PLANNED。
- Sources：[Shot](../../../direction/shot-list.md)、[Scene](../../../direction/scene-design-pack.md)、[Visual](../../../visual-development/world-visual-bible.md)均v1.0；Freshness：CURRENT（文本相符，非生产批准）。
- Represented Instant：约12秒，回应后；Audience Read / Basis：对照最终视线、手书状态与摄影机终点；不强制成为视频尾图输入。
- Previous / Next Handoff：只继承Shot状态；本次结束，无下一镜承诺。
- Viewing Stance：陪伴式旁观；Must Read：当前视线、书与窗帘关系；Must Withhold：未定义内心与人物过去。
- Narrative Function / Earning Reason：证明当前感知状态，必要时作同镜静态状态对照，不声称证明完整动作。
- Dramatic Read / Snapshot：C01保持坐姿，视线已落在窗外；头部小幅抬起；书仍摊在腿上、双手未离开；P02已回落窗侧。
- Attention MAIN：望向窗外的持续注意；SUPPORT：环境和帘子；HOLD：坐姿、手、书、房间。静态图不承担延迟或呼吸时序验证。
- Response Chain Source：PB01/B01—B03，完整时序交Motion，不把整条动作塞入本帧。
- Aspect：16:9提案；Variants OPEN；Protected Region：脸、手、书、帘固定点在画面内；竖版RECOMPOSE REQUIRED。
- Asset IDs / Versions：C01/COS01/LOC01/P01/P02合同v1.0，实际图片版本NONE。Makeup-Hair：随C01，无独立资产。
- Composition Guide：S001-SH01-CG01 v1.0，GRAYSCALE_LAYOUT / PLANNED；[合同](../../composition-guides/S001-SH01-CG01/guide-contract.md)；图像不存在。
- Composition Allowed Influence：机位/景别/主体占比/位置/深度/留白/遮挡/屏幕方向；Must Not Transfer：身份、服装、美术细节、最终光色与旧状态。
- Dependencies：真实P0用途、CG01；未来以F01与原始身份/空间回锚检查，不只沿上一帧累积漂移。
- World / Axis：ORI-S001 / CAM-SH01 v1.0，机位K1，同轴侧；左人、右帘、窗外可读，不创造反向房间。
- Composition & Depth：斜向环境中景，膝部以上与腿上书可见；右前帘不遮脸手书，人物与环境同可读。
- Visible Character / Prop State：C01保持坐姿，视线已落在窗外；头部小幅抬起；书仍摊在腿上、双手未离开；P02已回落窗侧。
- Observable Performance Snapshot：坐姿承重、肩胯保持；视线在窗外；无额外嘴角/眉眼动作，双手与书接触。头发不无因大幅摆动。
- Look / Light / Air：LOOK01/LIGHT01/AIR01 v1.0；夏日晴，侧向日光、墙反射；CLEAN AIR，无可见介质；PHYSICAL，Artistic NONE。只允许帘的局部遮光差异。
- Rhythm / Hold：继承Shot；末尾停留由Motion承担，静态图不能证明3秒保持。
- Continuity In / Out：同人同书同房间；视线与机位变化须与Shot相符；无数量/所有权变化。
- Must Show：人、书、窗外环境、帘悬挂逻辑；Must Avoid：额外角色、文字水印、过曝或整体模糊、结构漂移。

## REFERENCE INPUT MAP

| Logical Alias | File / Version | Role | Allowed / Must Not Transfer | Required |
|---|---|---|---|---|
| @IDENTITY_C01 | 待补，无真实文件 | IDENTITY | 只锁人物脸与年龄，不迁移背景/服装 | 是 |
| @WARDROBE_COS01 | 待补 | WARDROBE | 只锁衣层材料，不改脸 | 是 |
| @SCENE_LOC01 | 待补 | TOPOLOGY | 只锁房间结构，不把源图偶然人物带入 | 是 |
| @PROP_P01 / @PROP_P02 | 待补 | PROP / MATERIAL / STATE | 锁书本/帘形制及本帧状态，不迁移机位 | 是 |
| @POSE_CG01 | 待补 | COMPOSITION | 只锁构图，不转移身份、美术或光色 | 是 |

别名只是模型无关语义，不是已核实的平台槽位；所有输入WAITING_DEPENDENCY。

## IMAGE GENERATION BRIEF

Subject / Instant：C01保持坐姿，视线已落在窗外；头部小幅抬起；书仍摊在腿上、双手未离开；P02已回落窗侧。

Composition / Camera：继承K1与斜向环境中景；Light / Air：LIGHT01/AIR01；Materials：棉、纸、木与半透明纱可辨；Continuity：同一人物、一本摊开书、一幅固定帘、同一窗。Planned Image Prompt由Stage 13编译，不在本合同新增运动或模型指令。

File Path：无图片；Review Evidence：NOT_GENERATED；Correctness / Expression Review：NOT_EVALUATED；Actual Observation：NOT_EVALUATED；Approval Scope：NONE；Frozen Source：NONE。待验证静态构图、受光、接触和全部中间运动，不标APPROVED。

