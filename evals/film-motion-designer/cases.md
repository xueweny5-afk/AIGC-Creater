# Film Motion Designer V1 Cases

## CASE-M01｜老菜市场 S005 Ready Fixture

- **Expected：** 四个 Clip 覆盖 23 秒；人物、手/道具、摄影机和环境分层；SH04 运动先由人物完成，再触发可选后移；不写平台 Prompt。

## CASE-M02｜PLAN_ONLY Storyboard

- **Expected：** 返回 Generate/Review Storyboard，不把文本 Frame Brief 当批准关键帧。

## CASE-M03｜复杂接触

- **Expected：** 说明接触点、施力、支撑、重量、遮挡后状态和解除条件。

## CASE-M04｜静止镜头

- **Expected：** 对不动层明确写 HOLD，不自动添加呼吸、眨眼、飘发、粒子和推镜。

## CASE-M05｜平台能力不足

- **Expected：** 保留 Motion Master，将执行问题交给 Prompt/Generation 路由，不反向篡改故事。

## CASE-M06｜“悲伤”转为可观察表演

- **Input：** Scene/Shot 只允许克制悲伤；角色坐着读完信，下一镜保持同一状态。
- **Expected：** 用姿态/重心、视线、呼吸/停顿、手与信件、必要的衣物响应写进入—触发—退出链；不随机添加眨眼、喘息、飘发或推镜。

## CASE-M07｜灯光状态继承

- **Input：** Storyboard 绑定同一 Look/Light State，剧情没有光线变化事件。
- **Expected：** Light / Weather / Time 写 `HOLD`；不得为了运动感改变光向、冷暖、曝光或材料反应。
