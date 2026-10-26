# Delivery Contract

## Qualified-delivery evidence

每个版本必须记录：

- deliverable ID / purpose / audience
- recipient / Required-or-Optional / delivery scope and boundary
- exact path / filename / version
- source picture-lock ID/checksum
- requested spec source and access date
- actual container, codecs, resolution, aspect, frame rate, duration
- color metadata
- audio streams, channels, sample rate, measured loudness/peak when required
- subtitle streams/files/language/timing method
- file size / checksum
- probe tool/output receipt
- full playback completed and date
- Delivery Review: PASS / REVISE / NOT_EVALUATED；tool / exact version-checksum / audio listened / reviewed range / issues
- crop/reframe review
- rights/text/credits status
- final status

来源规格按字段记录 VERIFIED / UNVERIFIED / USER_LOCKED、URL/日期/入口或用户要求；未核实不声称平台合规。图片/字幕/音频等伴随文件按类型记录适用检查，视频母版仍须完整播放，静态伴随文件不伪造播放。正文的逐版本播放要求针对实际视频/音频输出，字幕等按实际使用方式验证。

## Archive vs distribution

- `ARCHIVAL / MEZZANINE`: 高质量、可再导出，避免不必要有损；不等于平台上传文件。
- `DISTRIBUTION`: 为具体播放/平台要求编码。
- `REVIEW`: 轻量、可加水印/时码，不能冒充母版。
- `SOCIAL VARIANT`: 逐镜重构画幅并验证，不是自动裁切。

## Status rule

- 文件缺失 → DELIVERY PLAN 或 RETURN TO POST（列实际责任与修复路径）
- 文件已导出但未 probe/播放 → EXPORTED_PENDING_VERIFICATION
- 技术通过但用户/文字/权利待确认 → DELIVERY CANDIDATE
- 全部门通过 → QUALIFIED DELIVERY

状态分别用于文件与整包。Package Required Set 明确本次 Required / Optional 及约定归档要求；整包仅在全部 Required 通过时 QUALIFIED DELIVERY，部分合格保持 DELIVERY CANDIDATE 并列可交文件和缺口。计划未执行保持 DELIVERY PLAN，不能填虚构路径/规格实测或播放。缺失/失败返回层统一写 RETURN TO POST 或清楚列 Delivery 修复路径，不混用未定义 RETURN。

## Expression and repair evidence

逐变体继承 Viewing Stance / Must Read-Withhold / Composition Relations / Presentation Mode / Artistic Rule IDs-Version / Required Holds。重构保护人物间距、留白/遮挡、关键动作和字幕；超批准范围返回 Post/Shot，不自动中心裁切。色彩、声道、静默和字幕检查区分批准表达与技术错误。每次修复登记原 Issue / New File-Version-Checksum / Recheck Evidence，完整播放结论必须对应新文件，不复用旧候选结果。

## Archive and recovery receipt

archive-manifest 记录 Archive Scope / Root-Entry Project / Relative Path / Source-Version / Checksum / Dependency Role / Availability、Software-Plugin Versions、Missing / Excluded / Authorization Limits、Relink-Recovery Steps。归档清单完整不等于实际恢复通过。

Recovery Check 使用 NOT_TESTED / PARTIAL / VERIFIED，列实际测试的打开/重链接/局部重导出范围、工具、结果/证据与未覆盖部分；只对测试范围声明 VERIFIED，不承诺所有环境或模型重生成一致。是否要求恢复实测按已有交付约定；未要求也需如实列未测试限制，不额外制造全环境重建关口。

## Planning and external delivery

PLAN_ONLY 可在未锁片时完整交付文字规格、变体、验证/归档计划与缺口；实际 EXPORT/VERIFY 须确切 PICTURE_LOCKED 来源和证据。默认本地交付/归档，上传、发布或提交平台需用户明确要求；不把合格文件等同已发布。

