# Continuity QC Guide

## Two-pass review

1. **Audience pass:** 正常速度完整播放，记录第一次不理解、不相信或注意力被错误吸引的时刻。
2. **Technical continuity pass:** 重看并检查身份、空间、动作、物理、光线、声音和相邻镜头状态。

复杂动作或闪烁问题再做逐帧/高密度抽帧；抽帧不能替代正常速度播放。

图片查看独立原图整体和必要局部，Playback 记 NOT_APPLICABLE；视频须完整播放，适用音频须实际听取。媒体缺失/损坏记 MISSING_MEDIA；可读但缺播放/听取能力记 NOT_EVALUATED，不混作已检查。无媒体仍可交审核计划和缺口，不能从 Prompt 或缩略图推导结果。

## Correctness and audience read

分别检查身份、动作/保持、实体和空间是否正确，以及观看立场、注意对象、构图 Must Read/Withhold、关系/感知与必要停顿是否实现。每项依据源合同和可观察结果，不以个人偏好代替标准；不能因没有穿帮就判表达成立。等待或重复的微差可承担情绪积累，不要求每镜新转折。

## Artistic rule check

读取 Presentation Mode / Artistic Rule IDs-Version、作用层、允许变化和保持项。物理接触、空气与实体按对应物理承诺；平面化、形变、梦境和非连续转换按批准规则和定位方式检查。没有批准依据的身份漂移仍是错误；有意艺术变化不因违反现实透视自动失败。以下物理/空气诊断适用于真实层，不覆盖非物理艺术规则。

## What to compare

- Prompt/Motion: 动作触发、阶段、摄影机与结束状态。
- Storyboard: 构图、身份、空间和关键帧状态。
- Shot List: 景别、轴线、屏幕方向、时长、Must Show。
- Asset contracts: 脸、身体、服装、场景拓扑、道具材料与状态。
- Neighboring Take: 结束/进入位置、朝向、持物、动作相位、光线、环境和声音。
- Entity ledger: 稳定 ID、数量、所有者、世界位置、可见性、开合/损坏状态和人物知情状态。
- Look/Light ledger: Scene Look & Light State ID、允许变化与实际触发。
- Atmosphere ledger: 介质、来源、分布、密度、驱动力、受光与跨镜触发。
- Rhythm map: 压力、行动/信息密度、视觉/声音能量、必要反应/静默与变化触发。
- Prompt coverage: Unsupported/Degraded 项是否诚实执行，是否出现模型能力伪支持。

## Action and physics

检查接触建立/解除、抓握、重量、重心、脚底支撑、穿模、遮挡后状态、物件落点、衣物/毛发次级运动。不要把“看着怪”作为最终问题描述。

交接物品时同时验证给予者释放、接收者获得和实体数量守恒。遮挡、出画或切换景别不等于物件可以复制、消失或换手。

## Camera diagnostics

- 主体变大但背景透视不变，可能是变焦而非推进。
- 画面旋转但摄影机位置不变，可能是摇摄而非横移。
- 声称环绕却无可追踪背景视差，运动可能未执行。
- 摄影机移动导致世界拓扑翻转或轴线错误，属于 major/blocker。

## Post-fix boundary

提出后期修复须写 Proposed Fix / Protected Intent / Feasibility Evidence / Residual Risk / Verification Scope，检查裁切是否损害 Must Show/留白、稳定是否破坏批准运镜、调时是否删必要停顿、调色是否改变艺术规则。只有可修范围有依据才交 Post；尚不确定写 conditional，并保留原问题，不承诺后期一定解决。

可考虑后期：轻微节奏、稳定、裁切、局部清理、颜色匹配、音量/噪声和无损失的遮罩。  
应重生成/上游返工：人物身份变化、肢体错误、主要动作缺失、道具穿透、错误空间、严重光向变化、错误对白口型、轴线/构图功能失效。

## Whole-sequence review

单镜通过后仍需按顺序播放选择的 Takes。独立好看不等于剪在一起成立；检查节奏、重复、方向、声音空间和观众信息是否连续。

分别记 Take Result、Boundary Result 和 Sequence Result 的范围/确切版本/证据/未检查项；单镜可按范围选用，但不标整段已通过。整段中有批准的省略、倒叙或艺术转换时引用其依据，不强制连续动作匹配。需要声音才成立的含义结合实际声音审核，未听取不推断通过。

状态变化 Take 通过后，把实际画面记录为 `Actual Observation`。若它偏离 Planned Post-state，先判断能否在不改变主合同的情况下接受；否则返回最早责任层。只把 `Affected Dependents` 标为待复核，已通过且不受影响的 Take 保持冻结。

相邻镜头还要比较姿态/重心、视线目标、呼吸/声音/停顿、手与道具以及服装/头发的物理响应是否承接。无触发的灯光方向、冷暖、曝光关系或材料反应变化不能以“更好看”通过。

空气介质必须符合物理来源和空间分布：蒸汽不能无热源持续出现，灰尘不能在无风无扰动时自动翻涌，雾密度不能跨切突然改变。节奏审核关注人物变化是否获得必要时间、快慢转换是否由行动/信息/声音触发；音乐能量不能掩盖画面节奏本身失效。

## Change impact, diagnosis and closure

上游版本变化先核对 Changed Fields / Affected Scope / Dependency Match。仅版本号或无关内容变化，经责任上游确认等价、更新引用并恢复 CURRENT 后可复用原 Take，不重生成；QC 不自行将失效源改回 CURRENT。真实受影响部分才返回对应层，未解决 freshness 不能 PASS。

Issue 分开 Expected Contract-Version / Actual Evidence / Audience-Edit Impact / Cause Hypothesis / Confidence-Basis / Next Diagnostic Check。图片用区域/坐标、视频用时间区间；症状可确定而原因不确定，不把猜测当根因。复核需链接原 Issue、新 Take/修复版本、同维度证据、残余问题与受影响依赖；未实际复核不关闭，不扩大为全批重审。
