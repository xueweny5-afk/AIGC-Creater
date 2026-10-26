# Midjourney提示词写法核对
查阅日期2026-10-20。本轮为用户要求查找标准写法，不提交生成。
官方来源：
- [Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)
- [Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
- [Stylize](https://docs.midjourney.com/hc/en-us/articles/32196176868109-Stylize)
- [No](https://docs.midjourney.com/hc/en-us/articles/32173351982093-No)
- [Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference)
- [Getting Started](https://docs.midjourney.com/hc/en-us/articles/33329261836941-Getting-Started-Guide)

官方事实：提示词可短至一词，无强制固定顺序；简短明确的画面描述通常更合适，避免长列表与详细操作指令。官方建议考虑主体、媒介、环境、光线、色彩、情绪及构图。这是描述维度，不是必填模板。
参数放正文末尾，用空格隔开，如--ar 16:9 --s 250。--no支持逗号分隔排除对象，并可能逐词解释；避免把长句否定塞入正文。250是创作起试建议，不是官方中式美学预设。
网页在Imagine输入框直接输入描述和参数，不需把命令前缀当正文。
风格参考承载色彩、媒介、纹理和光线等美感；网页用Style Reference槽，Discord可用--sref与有效图片链接。没有实际参考图时不虚构链接/代码。
本项目建议工作结构（非官方强制）：主体场景→视点构图→关键细节→光色→单一媒介/美学方向→参数。
上版五条语法可用，但部分美学形容词重复，篇幅偏长；后续适配可保留必要构图、色调与媒介，删去重复抽象情绪。不靠堆砌8k/masterpiece等词代替具体画面。

精简示例：
Ancient Jiangnan canal town in gentle spring rain, viewed obliquely from a second-floor gallery, dark tiled eaves framing the foreground, whitewashed houses, a stone arch bridge, willow branches over pale celadon water, spacious composition inspired by Song landscape painting, luminous overcast light, pearl white and ink gray, fine-art photography --ar 16:9 --s 250 --no people cars neon text watermarks

示例维持M01的同一场景/视点/风格意图，属于表达精简示范，不把未测试文本提升为已验证效果或替换完整五镜包。模型版本与账户默认设置仍未确定。

