# Film Prompt Adapter V1 Cases

## CASE-P01｜Mock I2V S005-SH04

- **Inputs：** READY Motion Spec、READY Storyboard fixture、`MOCK-CINEMA-I2V v1` profile。
- **Expected：** 编译 7 秒 I2V Prompt；精确映射首尾帧、两人物参考、运动阶段和条件式后移；音频因不支持而进入后期，不被写成已生成。

## CASE-P02｜目标模型未指定

- **Expected：** 根据输入模式给一个首选路由及理由，但实际 Package 保持 Model Verification Required，不能编造平台限制。

## CASE-P03｜真实模型资料过期

- **Expected：** 浏览官方资料并记录版本/日期；旧博客或第三方汇总不能单独证明当前能力。

## CASE-P04｜模型不支持结束帧

- **Expected：** 优先评估拆 Clip、简化次级动作或替代模型；不能删除锁定结束状态。

## CASE-P05｜图片 Prompt

- **Expected：** 从批准 Frame Contract 编译单一静态时刻，不加入动作过程或视频参数。

## CASE-P06｜十三项覆盖但保持紧凑

- **Input：** I2V Unit，部分项目不适用，目标模型不支持音频。
- **Expected：** 十三项全部有 `MAPPED / NOT_APPLICABLE / UNSUPPORTED / CONFLICT / RETURN` 状态和来源/落点；声音标 `UNSUPPORTED` 并转后期；Copy-ready Prompt 不机械复制十三段内容。

## CASE-P07｜负向提示与声音能力伪支持

- **Input：** Profile 明确不支持独立 negative prompt 和音频生成。
- **Expected：** 两项进入 Unsupported/Degraded；必要排除项仅按已核实方式处理，不宣称自然语言能保证平台功能。

## CASE-P08｜悲伤表演链传递

- **Input：** READY Motion Spec 中包含姿态/重心、视线、呼吸/停顿、手与信件及退出状态。
- **Expected：** Prompt 保留有动机的表演链与 Look/Light State，不退化为“sad, cinematic”或随机微动作。
