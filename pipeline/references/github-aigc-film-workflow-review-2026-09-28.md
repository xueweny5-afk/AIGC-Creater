# GitHub AIGC 电影工作流调研

- **调研日期：** 2026-09-28
- **目标：** 改善剧本到镜头的电影感与连续性、增加 Seedance/MiniMax 模型适配、为每个分镜建立可执行参考图映射、提高人物与服化道资产密度。
- **采用原则：** 只吸收可验证的流程与字段；不把第三方仓库整包复制进本项目，不执行第三方脚本，不把社区经验冒充官方规格。

## 结论

1. “电影感”不能靠追加 `cinematic / epic / masterpiece` 解决。需要在 Shot Design 阶段明确场景视觉句法、镜头功能、景别/角度对比、反应镜头、动作接点、切点动机和相邻镜头交接。
2. 创作主合同与模型 Prompt 必须分层。Shot List 和 Storyboard 保持模型无关；Prompt Adapter 再根据实际模型、版本和入口编译 Seedance 或 MiniMax 语法。
3. 每个 Frame 都需要显式 Reference Input Map：文件路径、版本、角色、允许影响、禁止影响、平台槽位以及 Prompt 中的绑定写法。
4. 跨镜头复用的主要人物不能只有一张“漂亮定妆图”。应先批准正面人脸特写，再派生头部角度、全身六视图、表情/手部/材质细节；服装单独建资产，最后形成 Combined Look。
5. 参考优先于重复描述。身份、服装、场景和道具分别使用稳定参考；分镜帧负责构图和开场状态；视频 Prompt 负责可见运动、镜头、声音和终点。

## 重点项目与采用决定

| 项目 | 可借鉴内容 | 许可证/状态（调研日） | 决定 |
|---|---|---|---|
| [Forget-C/Jellyfish](https://github.com/Forget-C/Jellyfish) | 分镜准备状态、人物/场景/道具/服装实体关联、首尾帧与多版本管理 | Apache-2.0；活跃 | 采用“资产关联 + 生成就绪检查”的数据思想，不引入应用代码 |
| [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | 每镜关联资产 ID、人物位置/朝向预分析、模型 Prompt 分层 | MIT；活跃 | 采用显式参考映射和空间连续性字段，不复制整套工作流 |
| [bytedance/agentkit-samples](https://github.com/bytedance/agentkit-samples) | Seedance 文生视频、首帧、首尾帧、多参考输入模式与有序引用示例 | Apache-2.0；ByteDance 官方组织 | 作为 Seedance 输入模式的高优先级依据 |
| [ByteDance Seedance 2.0/2.5 官方页面](https://seed.bytedance.com/en/blog/seedance-2-0-official-launch) | 多模态引用、分镜/角色/场景/道具分工、长叙事与镜头连续性能力 | 官方产品资料 | 用于能力边界；具体入口限制仍需执行前核实 |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | Hailuo 模型、时长/分辨率约束、方括号摄影机命令 | MIT；MiniMax 官方组织 | 作为 Hailuo Profile 依据 |
| [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | H3 工作流与多模态生成示例 | 未声明仓库级许可证 | 仅引用公开能力说明，不复制代码或文本 |
| [HVision-NKU/StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | 先建立一致条件图，再进行长序列生成的两阶段思想 | Apache-2.0；研究实现 | 采用 reference-first 思路；不引入旧 SDXL 运行栈 |
| [FireRedTeam/StoryMaker](https://github.com/FireRedTeam/StoryMaker) | 脸、发型、身体和服装同时保持的角色一致性思路 | 仓库未声明许可证 | 只作研究参考，不引入代码/权重 |
| [LinHao-city/StoryMind](https://github.com/LinHao-city/StoryMind) | 结构化镜头语言、情绪节拍到画面原因的转换 | AGPL-3.0；规模较小 | 只吸收通用摄影原则，不复制实现 |
| [zlbigger/story-video-director](https://github.com/zlbigger/story-video-director) | Seedance 引用顺序、参考角色、Prompt 阶段 Gate | MIT；社区项目 | 作为二级实践证据；官方资料冲突时不采用 |
| [Nagacash/character-continuity-skill](https://github.com/Nagacash/character-continuity-skill) | Canon Face、逐角度派生、服装/道具/伤妆/手持状态连续性表 | MIT；社区项目 | 采用合同字段与审核思路，不复制原文 |

## 未采用或降级处理

- 不采用“相邻镜头绝不能同景别”之类机械规则。相邻镜头可以同景别，但必须有新的叙事功能、空间变化或节奏理由。
- 不把社区写法中的固定参考上限、固定 Prompt 语言或固定标签当成所有 Seedance 入口的共同标准。标签和限制必须由当前 UI/API Profile 确认。
- 不引入 GPL/AGPL 应用代码，也不引入无许可证仓库的代码、模板或权重。
- 不采用 `bytedance-seedance2/seedance-2.0`。该仓库不属于已验证的 ByteDance 官方组织，README 含高风险安装命令与无法证实的“绝对一致性”宣传。
- 不将多格 Character Sheet 当成唯一身份输入。独立原图是生产主资产，Contact Sheet 只是审阅派生物。

## 对本项目的落地

- Shot Design 增加 `Scene Visual Strategy` 和 `Shot-to-shot Handoff`。
- Storyboard 每帧增加 `Reference Input Map` 与 `Image Generation Brief`。
- Prompt Adapter 增加 Seedance 与 MiniMax Profile，并强制区分模型/版本/入口。
- Asset Design 增加 Canonical Face、头部角度、全身六视图、独立 Costume、Combined Look 与 Material Detail Plate。
- World Visual Development 的资产需求模板同步增加上述依赖和交付字段。

## 证据等级

- `OFFICIAL`：模型厂商官网或官方 GitHub 组织。
- `RESEARCH`：论文作者官方实现。
- `COMMUNITY`：社区项目、实践模板或经验总结。
- `OBSERVED`：本项目实际生成结果和人工审核。

任何模型 Profile 的动态参数都必须记录来源与访问日期；执行时发现资料已过期，状态改为 `STALE`，不得继续批量生成。
