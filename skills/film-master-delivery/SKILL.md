---
name: film-master-delivery
description: 从实际 PICTURE_LOCKED 后期母版和交付要求规划、导出并验证横版、竖版、平台版、字幕版、审片版与归档母版，记录编码、画幅、帧率、色彩、音频、字幕、校验值和完整播放证据。用于最终本地交付与归档；不用于重新剪辑故事、未经审核自动裁切、上传或发布。
---

# Film Master Delivery

把锁片文件转化为可验证、可追溯的交付母版和派生版本。导出成功不等于交付合格；每个版本都必须验证并完整播放。

## Required inputs

1. `picture-lock-manifest.md`，状态 `PICTURE_LOCKED`
2. 实际锁片文件与媒体探测结果
3. 用户/平台交付要求：分辨率、画幅、帧率、编解码器、容器、色彩空间、音频、字幕、文件大小和命名
4. 字幕、片头片尾、版权、授权、署名和合规信息
5. 平台版本要求的当前官方来源（适用时）
6. 项目采用 Method 时的交付覆盖，例如循环闭合、画幅重构、声音或包装要求

没有实际锁片或未完整播放时，只能 PLAN_ONLY。

沿用本次交付边界、已定规格与源版本。PLAN_ONLY 可完整交付规格、变体、验证/归档计划及缺口，不要求先回传锁片或填入虚构文件。实际 EXPORT/VERIFY 才检查 PICTURE_LOCKED 与真实媒体证据；交付规划、合格文件、本地归档、上传发布分别记录，不自动扩成平台发布。

## Modes

- `PLAN_ONLY`: 创建交付规格、变体和验证计划。
- `EXPORT`: 用可用工具导出本地文件。
- `VERIFY`: 对每个实际版本进行 probe、校验值、字幕/音频检查和完整播放。

上传、发布、提交审核不是默认权限；只有用户明确要求时才进入单独授权流程。

## Load resources

- 规划或执行前读取 `references/master-delivery-guide.md`。
- 创建交付/验证记录时读取 `references/delivery-contract.md`。
- 使用 `assets/delivery-spec-template.md`、`assets/delivery-manifest-template.md` 与 `assets/delivery-verification-template.md`。

## Outputs

```text
AIGC Creater/projects/<project-id>/delivery/
├── delivery-spec.md
├── delivery-manifest.md
├── verification-report.md
├── masters/                       # 实际导出
└── archive-manifest.md
```

## Workflow

1. **Verify picture lock.** 精确锁定来源路径、版本、checksum、时长、帧率、画幅、色彩和音频；未锁片返回 Post-production。
2. **Define the requested delivery set.** 为本次确需版本记 Deliverable ID / Purpose / Recipient / Required-or-Optional / Spec Source。区分归档、发行、审片、字幕与画幅变体，不默认全套导出。Method 仅在采用范围内作用；规格冲突列待决定项，不擅增版本。
3. **Bind specification sources.** 平台要求查当前官方文档并记 URL/日期、入口/适用范围；用户自定标 USER_LOCKED，不冒称平台标准。无法核实标 UNVERIFIED，允许完成文字计划但不声称该平台规格已通过。
4. **Protect authored reframing.** 逐镜继承 Viewing Stance、Must Read/Withhold、人物间距、留白/遮挡、关键动作、字幕安全区与艺术规则。只有允许裁切范围内可直接派生；需动态重构或新内容时回 Post/Shot，列影响和可审方案，已有批准照用，不重复确认。无法保留表达时不自动中心裁切、不伪造补镜，不改锁片主版。
5. **Plan audio/subtitles.** 明确声道、采样率、响度/峰值目标及来源；字幕区分烧录、内封、外挂和无障碍字幕，检查时码、断句、语言和安全区。
6. **Export non-destructively.** 原锁片和归档母版保持不变；派生版本使用唯一文件名和版本号。转码可能有损时明确记录。
7. **Probe and identify the actual file.** 检查容器/流、时长/帧率/画幅、音频/字幕与色彩元数据，记录实际值、工具/回执和 checksum；有要求的响度/峰值另做实际测量，元数据不冒充视觉或听感检查。
8. **Review each exact variant.** 每文件完整播放并听取适用声音，核对黑帧/冻结、画幅表达、字幕、同步/声道、静默、色彩与结尾。按 Presentation Mode / Artistic Rule IDs 区分批准风格与转码错误；不能用统一调色/响度模板改掉意图。Delivery Review（PASS / REVISE / NOT_EVALUATED）绑定路径/版本/checksum、工具、日期、范围和问题；缺播放能力保持未评估，修复后验证新文件，不借用旧结果。
9. **Qualify files before the package.** 单文件满足来源锁片、规格、完整播放、声画文字/权利门才 QUALIFIED DELIVERY。本次所有 Required 版本通过且归档要求满足后才整体合格；部分通过按清单交已合格文件和缺口，整体保留 DELIVERY CANDIDATE，不外推。平台来源 UNVERIFIED 不声称该平台合规，用户自定规格按其范围验收。
10. **Archive with explicit recovery evidence.** archive-manifest 记录项目文件、素材相对路径/版本/checksum、所需软件/插件、EDL/字幕/许可/源 Take 与日志、缺失/授权排除项及重链接/恢复步骤。区分文件清单和实际恢复检查（NOT_TESTED / PARTIAL / VERIFIED），写检查范围/结果；未测试不声称可完整恢复，不承诺模型可重新生成相同 Take。只做本次授权的本地归档，不自动外传或发布。

## Delivery states

- `DELIVERY PLAN`
- `EXPORTED_PENDING_VERIFICATION`
- `DELIVERY CANDIDATE`
- `QUALIFIED DELIVERY`
- `RETURN TO POST`

## Non-negotiable boundaries

- 不从未锁片、代理、时间线预览或未完整播放文件创建“最终母版”。
- 不因 ffmpeg/导出命令成功、规格匹配或 checksum 存在就判合格。
- 不自动中心裁切横版为竖版，不允许字幕、人物、关键动作或道具被裁掉。
- 不未经验证改变帧率、色彩空间、音频布局或字幕方式。
- 不覆盖原始锁片和历史版本；有损转码不能冒充无损归档母版。
- 不虚构平台规格、授权、上传或发布成功。
- 不在未明确授权时上传、发布或提交到平台。

## Completion gate

以下为实际合格交付条件；PLAN_ONLY 以可审规格、来源/不确定项、变体和验证/恢复计划完成，状态 DELIVERY PLAN，不填虚构实际路径或检查结果。

- 每个要求的交付版本都有真实路径、版本、规格和 checksum；
- probe 结果与 delivery spec 一致；
- 每个版本都完整播放并记录证据；
- 竖版/方形重构逐镜通过；
- 音频、字幕、片头片尾、权利和署名通过；
- archive manifest 覆盖本次约定的依赖与归档范围，恢复能力按实际检查证据声明；
- 归档依赖、缺失项与恢复步骤明确，实际恢复检查范围/结果与未验证部分分开；
- 只有全部通过才标 `QUALIFIED DELIVERY`。
- 逐文件结果与整包结果分开，Required 未通过不整体放行；未执行上传/发布不声称已上线。
