# ATMOSPHERE STATE REGISTER

## IDENTITY

Project：FPD-20261018-晴天未完；Version：v2.3；Scope：U01/S002候选。Sources：[Brief v2.3](../project-brief-v2.3.md)、[剧本v2.3](../screenplay/screenplay-v2.3.fountain)、[研究](../research/light-surprise-study.md)。
Status：DEFINED（文字）。本状态不覆盖旧v2.1“干草地/清洁空气”样例；当前候选需整套采用新状态，不能混搭。

## STATES

ATM-LOC02-POSTRAIN-V1：LOC02 / S002 / LOOK02 v2.3 / LIGHT02 v2.3。
Medium：极淡局部雾，细小悬浮水滴；Physical Source：阵雨后林缘阴凉低处残留雾滴，CREATIVE / ASSUMED，非已观察实际天气。
Distribution：前方靠植被的局部空气，约离草地0.3—1.2米的中景小范围；大部分画面空气仍清透。不得全局铺成白色烟。
Density/Scale：单个雾滴无需可辨，散射光路可读但不盖住植被/地形；不生成均匀大光点。温湿背景仅定性为雨后阴凉，不虚构测量数据。
Driver：轻风让介质微弱平移，6秒内总体密度保持；主要可见变化由枝叶遮挡控制，不靠雾瞬间浓淡跳变。
Light：画外侧后方低斜日光，穿过同一枝叶缝隙斜向前下方，深绿树影提供背景；光路方向由太阳固定，边缘可因叶片遮挡变化。
Materials：湿草/湿叶有局部润泽，受照叶片可透亮；无可见人物皮肤/衣服任务。杯稳放地面，杯色不变、不自发光。
Readability：一小道窄光为MAIN；天空不占压倒性多数以免抹掉局部光对比；不出现烟机、体积巨柱、闪光或全局金色滤镜。

## TRANSITIONS

起始叶隙被遮→风拨叶→2—4秒窄光路显现且湿叶被照亮→4—6秒叶回摆、窄光渐弱。雾滴密度与固定背景保持；光变弱不是介质凭空消失。
当前候选替代旧看云动作；不再同时做大幅抬眼、前推或升空。

## DOWNSTREAM HANDOFF

Visual：LOOK02/LIGHT02/AR02更新为v2.3，色彩保持v2.1的中性整体原则，只有受照小区域带自然暖色；AIR02旧NONE不适用于此候选。
Asset：LOC02新增POSTRAIN状态，真实无人拓扑与空气校准画面分开；不要求新角色图。
Scene/Shot：沿眼高侧看近处叶与中景暗背景，风引导光进入注意；保持身体在原处。
Motion：0—2秒基线，2—4秒露光，4—6秒变弱及保持；光方向固定、风驱动枝叶。
Prompt：必须保留局部雾滴来源、斜阳、叶隙遮挡与暗背景关系，不能只写“丁达尔效应”。
QC：未来实际检查起始是否已有过强光柱、光源方向、枝叶遮挡、雾密度保持、物体接触和曝光连续；当前无真实媒体。

## DECISION REGISTER

LOCKED：6秒、文字分工、用户希望意外发现；ASSUMED：雨后漏光候选的全部天气/视觉细节。OPEN：平台入口与生成效果。没有像素/运动QC通过。

## NEXT ROUTE

Visual / Asset / Scene / Shot / Frame / Motion以候选补充传递，完成Prompt内容稿；不生成。

