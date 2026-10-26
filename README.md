# AIGC Creater

AIGC 电影与短片创作工作区，用可追溯的阶段产物连接选题、研究、故事、剧本、视觉、分镜、运动、提示词及后续制作。

## 从这里开始

1. 阅读 [项目工作准则](AGENTS.md)，了解交付范围与归档要求。
2. 按 [电影制作工作流](pipeline/film-production-pipeline.md) 推进相关阶段。
3. 在 `projects/<project-id>/` 中维护项目，沿用稳定的 Project ID、Asset ID 与版本引用。

默认交付范围为文字内容，推进到视频生成前；图片、视频生成与剪辑可交接至 RunningHub 或其他平台。实际生成与后期范围以各项目最新要求为准。

## 目录

| 目录 | 内容 |
| --- | --- |
| `pipeline/` | 制作流程、共享知识与研究参考 |
| `skills/` | 各制作阶段的技能说明、模板与接口 |
| `evals/` | 工作流与技能的评估用例、记录及产物 |
| `projects/` | 各项目的创作主版本、提示词、资产登记与制作记录 |

各技能的使用方式见对应的 `skills/<skill-name>/SKILL.md`。本仓库以文档和模板为主，没有统一的应用启动命令；项目中的 Python 脚本按各自用途和本地依赖运行。

## GitHub 同步范围

仓库保存工作流、技能、评估记录、项目文档、提示词和必要脚本。图片、音视频、凭据、环境和缓存通过 [.gitignore](.gitignore) 排除，媒体文件继续保留在本地。

文档中保留的媒体路径用于本地制作追溯；克隆仓库不会获得这些媒体，相关画面与制作审核需要本地素材或平台结果才能复核。

后续同步：

```sh
git status --short
git add --all
git commit -m "Update project documents"
git push
```

提交前检查暂存文件，确保同步范围符合当前项目要求。
