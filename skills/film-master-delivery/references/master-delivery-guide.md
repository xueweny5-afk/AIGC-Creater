# Master Delivery Guide

## Specification sources

平台规则会变化。使用官方帮助中心、上传规范或 API 文档，记录 URL 和访问日期。第三方博客只可辅助，不单独作为当前规格依据。用户自定义交付应标 `USER_LOCKED`。

按 Deliverable ID / Purpose / Recipient / Required-or-Optional 只建本次版本，规格逐项标来源、适用入口与 VERIFIED / UNVERIFIED / USER_LOCKED。来源冲突列差异，不把自定参数冒称平台要求；未核实可交计划，不声称平台合规。

## Probe is necessary, not sufficient

`ffprobe` 等工具可以确认容器与流信息、时长、帧率、分辨率、音轨和部分色彩元数据；它不能判断故事、裁切、字幕可读性、色偏、冻结、音画同步或听感。技术探测后仍要完整播放。

## Reframing

对每镜记录：

- 主体与关键道具位置；
- 可安全裁切区域；
- 是否需要平移/缩放/动态重构；
- 字幕和文字安全区；
- 轴线与视线是否仍可读；
- 需要返回 Post/Shot 的情况。

若竖版无法保留故事信息，不强行创建；向用户说明需专门重构或补镜。

同时核对 Viewing Stance、Must Read/Withhold、人物间距、负空间/遮挡及 Artistic Rule IDs-Version。允许裁切以批准范围为准；动态重构需 Post/Shot 方案，已有授权不重复询问。变体保持锁片意义，不擅添新事件/人物或用自动中心裁切牺牲表达。

## Audio and subtitles

- 响度目标必须来自交付规范，不使用通用数值冒充所有平台。
- 检查声道映射、相位、峰值、静音和结尾截断。
- 字幕检查拼写、断句、说话人、时间码、换行、安全区和语言标签。
- 烧录字幕与外挂/内封字幕分别验证；播放器支持不能假定。

有意静默、非标准色彩/曝光和声音空间按批准规则保护；检查是否是导出转换错误，不把风格差异统一“纠正”。色彩标签不能证明显示正确，音频流存在不能证明同步/听感通过；响度目标有来源，实际测量结果与工具单列，未测不伪造。

## Per-file qualification

每个文件绑定路径/版本/checksum、源锁片、实际 probe、完整播放/听取、画幅/声画/文字/权利结论。Delivery Review 用 PASS / REVISE / NOT_EVALUATED，缺工具保留缺口；修复生成新文件后重做对应技术和完整播放验证，不套旧证据。每个实际要求版本需验证，不能只看来源母版。

Package Required Set 写 Required / Optional 与约定归档要求；所有 Required 文件合格才整体 QUALIFIED DELIVERY。部分通过可交具体已合格文件，整包 DELIVERY CANDIDATE；未要求可选项不无故阻断。归档恢复测试是否为验收要求按已有交付约定，不强加全环境重建。

## Archive

保存：锁片、交付母版、字幕、音频 stems、项目文件、EDL、字体/音乐/素材许可、源 Take、资产、Prompt、生成日志、QC 报告、软件/模型版本和 checksum。私人素材的归档位置与访问权限须符合用户授权。

archive-manifest 记 Relative Path / Original Source-Version / Checksum / Dependency Role / Availability、项目与软件/插件版本、排除/缺失及重链接步骤。归档内相对路径与起始项目文件明确，不要求复制所有历史失败文件或未授权素材；写清范围与限制。Recovery Check 为 NOT_TESTED / PARTIAL / VERIFIED，记录实际执行的打开、重链接或局部重导出范围/工具/结果；仅文件存在不代表恢复成功，未测不宣称全部可恢复，也不承诺模型重生成一致。

## Plan vs publication

无实际锁片仍可交 DELIVERY PLAN、规格、验证与恢复步骤，缺媒体不阻止文本交付。EXPORT/VERIFY 才需真实锁片证据。合格本地文件、归档、上传和发布分别记录；没有明确发布请求不执行上传，也不声称已上线。

