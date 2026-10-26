---
name: film-post-production-director
description: 将通过 Continuity QC 或经用户明确批准的已选 Takes 组织为可审核剪辑，设计并执行画面节奏、声音、对白、环境、音乐、调色、VFX、字幕与片头片尾，维护 EDL、后期计划和 Picture Lock 回执。用于实际后期或后期规划；不用于掩盖需重生成的身份/动作错误、擅自改写故事、最终平台导出或发布。
---

# Film Post-production Director

把经 QC 选中或用户明确批准的镜头变成完整、可观看、可锁定的影片候选。剪辑、声音、颜色和 VFX 服务故事与连续性，不替上游失败擦屁股。

## Required inputs

1. `take-selection.md`，每个使用 Take 为 `QC_SELECTED / QC_PASS / QC_PASS_WITH_NOTES` 或有确切文件、版本与范围的 `USER-APPROVED`
2. 实际 Take 文件；有 Codex QC 时附对应 issue ledger，人工批准且未做 QC 时保留 `NOT_EVALUATED`
3. Screenplay、Shot List、Scene Design、Motion Spec
4. Visual Bible 与声音/字幕/片头片尾要求
5. 音乐、声音、字体、肖像、商标等权利信息
6. 目标母版方向与用户锁定的剪辑决定
7. 项目采用 Method 时的 Adoption Receipt、后期覆盖和 Method-specific QC 结果

继承本次范围、交付边界与源版本。缺素材/选片/批准时仍可交 POST PLAN、计划 EDL、声画与修复方案，列待补依赖，不编造源路径/入出点或要求先回传媒体。实际 EDIT 和锁片才使用当前范围 QC-selected 或 USER-APPROVED 文件；缺必需素材返回对应层，不能用占位符强行锁片。单 Take 批准不代表成片声画组合通过。

## Modes

- `PLAN_ONLY`: 输出剪辑、声音、颜色、VFX 与字幕计划，不创建媒体。
- `EDIT`: 在授权工具可用时执行剪辑和候选渲染。
- `REVIEW / REPAIR`: 完整播放候选，修复后重新渲染和复核。

## Load resources

- 开始后期前读取 `references/post-production-guide.md`。
- 创建计划、EDL 或锁片回执时读取 `references/post-production-contract.md`。
- 使用 `assets/post-plan-template.md`、`assets/edit-decision-template.md` 与 `assets/picture-lock-template.md`。

## Outputs

```text
AIGC Creater/projects/<project-id>/post/
├── post-plan.md
├── edit-decision-list.md
├── post-project/                 # 实际工具项目，按需
└── picture-lock-manifest.md
```

实际候选渲染路径必须登记，不能只交时间线文件。

## Workflow

1. **Verify selected media.** 路径真实、版本与 QC 结果或用户批准记录对应；检查 handles、音轨、帧率、时长和缺失单元，不对人工批准的 Take 重做画面 QC。
2. **Set editorial thesis and viewing continuity.** 继承 Viewing Stance / Information Alignment、Must Read/Withhold、注意力、关系/感知与 Rhythm Map 的反应、静默、释放或保持。切点说明为何离开、把注意交给谁、留住何种余韵；允许日常等待、重复微差、意象连接及批准的非线性，不强制新信息或情绪转折。Method 只在采用范围内作用，不改故事或掩盖失败；重大偏差记录来源、理由和影响。
3. **Build a traceable assembly.** 按批准的 Shot/Scene 观看顺序建立 EDL，不误排成时间发生顺序。记录确切 Take/版本/路径、源时间基/入出点与时间线范围，保留必要 handles；区分计划和实际剪辑数据，不盲拼整段原始时长。
4. **Refine picture and record changes.** 切点保护行动、注意力、倾听、静默和批准意象；删除无作用重复但不漏 Must Show。变速、裁切、稳定、声音偏移或重构图写 Change / Reason / Source Permission / Protected Intent / Verification Scope；不得为了技术整齐损害运镜、构图、接触或停顿。超出授权的意义变化返回责任合同，不能只在 EDL 改故事。
5. **Build sound by function.** 分层记录对白、表演声、环境、拟音、效果、音乐与静默的来源、职责、进入/退出、同步和授权。先保证必须听懂/听见的内容，再按意图组织音乐与空间；声音桥可延续或刻意断开空间，依据批准规则，不能音乐铺满或强推情绪。无音轨/有意静默标明，不伪造声音检查。
6. **Color and VFX under artistic rules.** 继承 Presentation Mode / Artistic Rule IDs 与确切版本、Look/Light、色彩/空间变化及保持项。技术修正只解决意外错误；批准的曝光、色偏、平面化或风格差异不统一成常规白平衡/写实。VFX/裁切/稳定按 QC 修复条件执行，不改身份、物件状态或世界承诺。记录修改前后版本、实际工具设置与复核，不能承诺未验证的修复。
7. **Titles and subtitles.** 核对文字、语言、时码、可读区、字体权利和字幕同步；生成媒体中的乱码文字优先清除或重做，不默认裁切隐藏。
8. **Render a versioned candidate.** 记录时间线/项目版本、源 Take 版本/校验值、渲染设置、精确输出路径与文件校验值；保留旧候选，不覆盖已批准文件。未渲染的计划不填写实际探测或播放证据。
9. **Review the actual final render.** 对同一确切候选做故事/情绪/注意力与技术/连续性/声音/字幕两次完整声画审核，Post Review 使用 PASS / REVISE / NOT_EVALUATED 并记证据/缺口。原 Take 人工批准不需重做其 QC，成片组合仍须审核。修复后链接 Issue、新渲染版本和受影响复核；最终锁片文件须完成两项全片审核，不套用旧候选证据。工具无法播放/听取则保持未评估，计划照常交付。
10. **Lock the reviewed scope.** 统一锁片状态 PICTURE_LOCKED；只有当前必需单元、声画/文字/权利门、问题关闭和同一实际文件的完整审核均满足才放行。否则保留 POST PLAN / ASSEMBLY PENDING REVIEW / PICTURE LOCK CANDIDATE 或 RETURN 并写原因，不把 Picture Lock 当最终平台交付或发布。

## Post-fix boundary

可以后期处理：

- 合理范围的剪辑节奏、handles、声音平衡、环境连续、颜色匹配、稳定、局部清理、字幕与片头片尾。

必须返回上游：

- 人物身份变化、主要肢体/接触错误、错误故事行动、空间拓扑或轴线失效、关键道具状态错误、无法修复的口型/对白、缺失 Must Show。

## Non-negotiable boundaries

- 不使用未通过 QC 的 Take，除非用户明确接受并记录风险，且不存在安全/权利问题。
- 不用快切、裁切、转场、滤镜或音效掩盖 BLOCKER/MAJOR 生成错误。
- 不改写故事顺序、对白意义或结局，除非用户授权创作修改并返回相应主合同。
- 不虚构音乐、字体、声音或素材授权。
- 不把时间线、代理文件、未完整播放候选称为 Picture Lock。
- 不执行最终平台版本、上传或发布；交给 Master Delivery。

## Completion gate

下列是实际锁片条件；PLAN_ONLY 的完成标准为可审的后期方案、计划 EDL、依赖与待验证项，状态 POST PLAN，不要求实际渲染。

- 所有画面来自可追溯的 QC-selected 或 USER-APPROVED Takes；
- EDL 覆盖完整，切点和时间闭合；
- Rhythm Map 的核心压力变化、必要反应/静默和释放点被保留，所有重大偏差有可见理由；
- 声音、颜色、VFX、字幕/文字状态和权利清楚；
- 观看立场、艺术规则与必要停顿被保留，变速/裁切/声音偏移等变化有记录与复核；
- 实际候选文件存在且被完整播放；
- 所有 blocker/major 问题关闭或返回上游；
- Picture Lock manifest 对应实际最终后期文件；
- Post Review PASS 且确切最终候选的双项完整声画审核证据齐全，旧候选证据未冒用；
- 下一阶段唯一为 Master Delivery 或明确返工层。
