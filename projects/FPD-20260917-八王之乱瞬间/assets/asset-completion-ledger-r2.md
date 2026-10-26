# 《洛阳无赢家》资产补齐总账｜R2

M02最新实际结果（2026-10-01）：用户选择Codex生成并审核；S01清洁拓扑R2-v1、S07无烟荒田R2-v1、P06清洁八棋R2-v1三张已保存，原图保留、源/副本SHA256相等。三单元仅可见结构/无烟/数量等限域SELF-REVIEWED APPROVED，整项仍缺状态与细节；准确[图片及审核范围](batch-r2-m02-review.md)、[完整提示词](prompts/ASSET-R2-M02-城门荒田八棋.md)。没有待运行图像任务，G3 NOT PASSED。以下M01或起始状态是历史快照，不覆盖M02结果。

最新追加：M01累计6张；P04全长实际v3仅简化重建结构/材料限域批准，握持/尺寸/精确西晋器型未批准；整项REWORK。后续结构引用绑定v3。见[追加审核](batch-r2-m01-review.md)。以下5张及v2状态是追加前快照，资产总体未完整。

- 日期：2026-10-01；Project ID：FPD-20260917-八王之乱瞬间。
- 源：SCREENPLAY-MASTER-R1 / VISUAL-BIBLE-R1 / ASSET-REQUIREMENTS-R1。
- 模式：AUTO_GENERATE / REVIEW；用户已选择Codex生成道具/场景母资产。M01实际5张已保存审核；资产总体仍未补齐，107条提示词不等于107张成品。

## 最新实际结果（优先于下方起始快照）

P01-正面尺度实际采用v2，限正面形制/材料APPROVED；绝对尺寸未通过。S03-清洁殿内v1限同方向可见结构/清洁空气APPROVED；不批准反向及全部Look。P04-独立全长v2保持REWORK，单支构图已修但具体戟头形制仍待依据。实际路径及5张审核见[本批回执](batch-r2-m01-review.md)。P01/P04/S03三整项仍未齐全；后续引用批准单元必须用这里的实际版本，而不是任务原计划v1。

## 需求与起始状态快照
- [全量补齐提示词](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/prompts/ASSET-COMPLETE-R2.md>)；[既有像素审核](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/asset-review-r1.md>)；[失败修正记录](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/batch-b01r-execution.md>)。

| ID | 职责 | 优先级 | 现状 | 必须补齐/复用范围 | 依赖 | 现有候选/限域批准 | 补齐合同 |
|---|---|---|---|---|---|---|---|
| C01 | 皇帝身份 | P0 | REWORK | 修复胡须且保留皮肤；头部四角；基础体态六视；304年龄；殿内与旅行定妆 | K01,K02 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C01-晋惠帝/C01-晋惠帝-291-正脸-R1-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C01-晋惠帝/asset-completion-contract-r2.md>) |
| C02 | 司马伦身份 | P0 | REWORK | 修复胡须且保留皮肤；头部四角；基础体态六视；宗王定妆和持玺接触 | K03,P01 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C02-司马伦/C02-司马伦-正脸-R1-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C02-司马伦/asset-completion-contract-r2.md>) |
| C03 | 军队群体组合 | P1 | PLANNED | 骑步兵组合职责、数量与差异合同；不要求群演六视图 | C03-A,C03-B,P03,P04 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C03-军队群体/asset-completion-contract-r2.md>) |
| C04 | 洛阳百姓 | P1 | APPROVED（限定范围） | 保留既有避让图；补袖口/墙边接触细节 | K04,S02 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C04-洛阳百姓/C04-洛阳百姓-贴墙避让-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C04-洛阳百姓/asset-completion-contract-r2.md>) |
| C05 | 母子身份与背影 | P1 | PLANNED | 母亲/孩子各一张身份、各一张背影；牵手结构参考 | K04 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C05-母子身份/asset-completion-contract-r2.md>) |
| C06 | 守城军士 | P0 | REWORK | 中性身份；必要背影；同军装定妆；长戟握持接触 | C03-A,P04 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C06-洛阳守城军士/C06-洛阳守城军士-火光-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/characters/C06-洛阳守城军士/asset-completion-contract-r2.md>) |
| K01 | 殿内帝王穿戴 | P0 | PLANNED | 独立服装正/侧/背；冠领袖细节；坐姿褶皱 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/K01-殿内帝王穿戴/asset-completion-contract-r2.md>) |
| K02 | 旅行皇帝穿戴 | P1 | PLANNED | 独立旅行衣正/侧；领袖及坐姿褶皱 | K01 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/K02-旅行皇帝穿戴/asset-completion-contract-r2.md>) |
| K03 | 宗王礼服 | P0 | PLANNED | 独立正/侧/背；袖口腰带细节 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/K03-宗王礼服/asset-completion-contract-r2.md>) |
| K04 | 平民织物体系 | P1 | PLANNED | 母亲/孩子/居民独立服装；粗织领袖下摆细节 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/K04-平民织物体系/asset-completion-contract-r2.md>) |
| C03-A | 步兵与守军铠甲 | P0 | REWORK | 独立正/侧/背；肩袖系带甲裙细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/C03-西晋军服/C03-A-西晋步兵-筒袖铠-v2.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/C03-西晋军服/asset-completion-contract-r2-C03-A.md>) |
| C03-B | 骑兵装备与马具 | P0 | REWORK | 独立骑兵服装；马/马具左右侧；鞍腹带缰绳细节 | C03-A | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/C03-西晋军服/C03-B-西晋骑兵-无外露马镫-v2.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/costumes/C03-西晋军服/asset-completion-contract-r2-C03-B.md>) |
| S01 | 洛阳城门 | P0 | REWORK | 无人清洁拓扑；闭/窄缝/开；同结构晨雾校准；门轴湿地细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S01-洛阳城门/S01-洛阳城门-晨雾-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S01-洛阳城门/asset-completion-contract-r2.md>) |
| S02 | 洛阳街道 | P1 | APPROVED（限定范围） | 保留空街；墙根及积水细节；不为完整机械造反面 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S02-洛阳街道/S02-洛阳街道-雨后-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S02-洛阳街道/asset-completion-contract-r2.md>) |
| S03 | 宫殿与宫门区域 | P0 | REWORK | 清洁殿内；291/301日/306空殿夜；宫门雨态三开度；柱阶帘灯细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S03-皇宫大殿/S03-皇宫大殿-基准-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S03-皇宫大殿/asset-completion-contract-r2.md>) |
| S04 | 形势展示空间 | P1 | PLANNED | 展示面合同与共享底图引用；不冒充军帐或历史地理 | P06 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S04-形势展示空间/asset-completion-contract-r2.md>) |
| S05 | 北方荒野 | P2 | PLANNED | 无人低丘草土与路径；草土接触细节 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S05-北方荒野/asset-completion-contract-r2.md>) |
| S06 | 洛阳城外离城路径 | P1 | PLANNED | 城外看向城门的无人道路；城在后/离城路径关系；轮下接触 | S01 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S06-洛阳城外道路/asset-completion-contract-r2.md>) |
| S07 | 荒田与流民道路 | P1 | REWORK | 无烟拓扑暮色；农具空袋细节；路与田关系 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S07-荒田与流民道路/S07-荒田与流民道路-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S07-荒田与流民道路/asset-completion-contract-r2.md>) |
| S08 | 夜城墙与远火状态 | P0 | REWORK | 无人清洁结构；黑暗/单火点/断续火线；近火源位置与城垛细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S08-洛阳城墙/S08-洛阳城墙-远方火线-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/locations/S08-洛阳城墙/asset-completion-contract-r2.md>) |
| P01 | 玉玺与玺绶 | P0 | REWORK | 正/侧/背可见面；手掌尺度；环钮绶带；托持/交接结构 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P01-玉玺与玺绶/P01-玉玺与玺绶-v2.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P01-玉玺与玺绶/asset-completion-contract-r2.md>) |
| P02 | 雨中青纸诏 | P1 | APPROVED（限定范围） | 保留雨中图；纸纤维朱印湿石近尺度细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P02-青纸诏/P02-青纸诏-雨中-v2.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P02-青纸诏/asset-completion-contract-r2.md>) |
| P03 | 军队旗帜 | P2 | PLANNED | 独立旗杆旗布全貌；系带与缝边细节 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P03-军队旗帜/asset-completion-contract-r2.md>) |
| P04 | 长戟 | P0 | PLANNED | 全长；有侧枝戟头；木铁连接；手握接触 | 独立母资产 | 暂无独立文件；共享/候选依任务卡 | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P04-长戟/asset-completion-contract-r2.md>) |
| P05 | 封闭车驾 | P0 | REWORK | 独立外形侧/后；内厢与外体对应；轮轴辕牛连接/帘缝细节 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P05-封闭牛车/P05-封闭牛车-离城-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P05-封闭牛车/asset-completion-contract-r2.md>) |
| P06 | 八王棋子与底图 | P1 | REWORK | 清洁八枚底板；单枚棋；无字底图；后期标签路线说明 | 独立母资产 | [现有文件](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P06-八王形势地图/P06-八王形势地图-无文字-v1.png>) | [合同](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260917-八王之乱瞬间/assets/props/P06-八王形势地图/asset-completion-contract-r2.md>) |

## 状态解释及已知失败

APPROVED只对C04静态群体POSE、S02单方向湿街、P02雨中纸诏状态；不扩大到完整资产。各历史候选有可复用部分，REWORK不等于全废。C01/C02正脸v1仍REWORK；v2/v3明确REJECTED，不下发多视图。此总账不改变任何旧原图状态。

S08近火源位置待实际批准；三远景状态都从同一批准母图编辑。P01低环钮、C02旧雕刻钮不能混用。P05旧车进门方向不当作离城证据。S01开门图不能当闭门开场。S03宫门和内殿分别有结构资产，未建立的连通关系为UNKNOWN。

## 下一动作

本批母资产方式已选择且M01执行完毕，记录见上方最新结果。继续补不依赖P04的母资产；P04先取可审核形制依据，后续派生遵循实际批准单元版本。逐项闭合26项职责后才进入Stage09。Stage13视频提示词是最终交付边界，Stage14及之后的视频生成由用户操作。

2026-10-02：M03四张实际保存并逐图审核，限域 SELF-REVIEWED APPROVED；S01开门复用清洁拓扑，门轴/晨雾未齐。P06三计划单元已齐。用户“直接全部生成”已取代逐批询问。[实际结果](batch-r2-m03-review.md)。G3 NOT PASSED。
