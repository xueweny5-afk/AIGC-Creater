# Film Researcher Default Vault Smoke Test

- **Test Date｜测试日期：** 2026-09-17
- **Project Topic｜项目主题：** 八王之乱历史瞬间
- **Purpose｜测试目的：** 验证默认 Obsidian vault、只读本地检索、无结果降级和公开网络补缺链路。

## DEFAULT VAULT

- **Vault Name｜名称：** `claude-obsidian`
- **Resolved Path｜CLI 实际路径：** `D:\project\codex_project\claude-obsidian`
- **Connection｜连接状态：** PASS
- **Write Operations｜写操作：** None

## LOCAL SEARCH

使用 `search:context` 只读检索，范围为默认 vault。

| Query | Result |
|---|---|
| 八王之乱 | No matches |
| 西晋 | No matches |
| 晋惠帝 | No matches |
| 司马 | No matches |

结论：默认 vault 可访问，但当前没有检索到八王之乱或西晋的直接相关笔记。未扩大到其他 vault，也未读取无关笔记。

## WEB FALLBACK

在本地无结果后执行小规模公开来源发现，未进行完整 Research Pack：

### SRC-001｜《“八王之乱”爆发原因试探》

- **Source Type｜来源类型：** ACADEMIC_SOURCE
- **Institution｜机构：** 北京大学学报（哲学社会科学版）
- **URL｜链接：** https://ccj.pku.edu.cn/Article/info?aid=271016016
- **Use｜用途：** 提供八王之乱起因与影响的学术研究入口。
- **Limitations｜限制：** 当前 smoke test 只核对页面摘要，具体论点仍需阅读全文并与其他研究交叉验证。

### SRC-002｜《晋书·列传第二十九》文本入口

- **Source Type｜来源类型：** PUBLIC_REFERENCE（原始史籍文本转录入口）
- **URL｜链接：** https://m.gushiwen.cn/guwen/bookv_57275f46e7cd.aspx
- **Use｜用途：** 定位《晋书》八王相关列传和可继续核对的事件记录。
- **Limitations｜限制：** 网站不是权威校勘机构，正式引用前需要与可靠点校本或其他原始文本来源核对。

### SRC-003｜《西晋关中都督选任与晋末关陇豪右政治》

- **Source Type｜来源类型：** ACADEMIC_SOURCE
- **Institution｜机构：** 南开大学历史学院 / 《南开史学》
- **URL｜链接：** https://history.nankai.edu.cn/2025/1201/c37306a585609/page.htm
- **Use｜用途：** 提供西晋政治地理、都督制度和关陇权力结构的专题研究线索。
- **Limitations｜限制：** 属于专题研究，不能单独承担八王之乱完整时间线或全部因果解释。

### SRC-004｜福建省文旅厅西晋青釉瓷资料

- **Source Type｜来源类型：** OFFICIAL_INSTITUTION
- **Institution｜机构：** 福建省文化和旅游厅 / 浦城县博物馆藏品
- **URL｜链接：** https://wlt.fujian.gov.cn/zwgk/ztzl/bmwu/202311/t20231124_6307641.htm
- **Use｜用途：** 提供西晋实物与人口南迁相关视觉研究线索。
- **Limitations｜限制：** 适合物质文化和后果研究，不能直接证明具体政治事件中的人物行为。

## RESULT

- 默认 vault 配置：PASS
- Obsidian 只读检索：PASS
- 本地无结果时诚实报告：PASS
- 公开网络补缺：PASS
- 来源类型与局限标注：PASS
- 虚构本地命中或历史事实：NONE
- 生成候选历史瞬间：NOT RUN；当前证据覆盖不足，不提前评分。

## NEXT FULL TEST

完整研究需要继续建立：

1. 八王之乱时间线和人物关系；
2. 《晋书》《资治通鉴》等原始记载的可靠文本入口；
3. 现代学术研究之间的解释差异；
4. 可作为独立短片的候选事件；
5. 每个候选事件的史料、视觉依据、争议和制作可行性评分。

