# 《香积寺之战》剩余资产生图交接 V2

- Project ID：FPD-20260929-香积寺之战。
- 日期：2026-10-05；执行方式：USER_GENERATE，Codex不再提交图片或视频任务。
- 范围：Stage08静态资产候选制作与返工；不是正式分镜/视频提示词交付，G3尚未整片通过。
- 当前文件情况见 [完成情况与缺口](<D:/project/Codex_zimeiti/AIGC Creater/projects/FPD-20260929-香积寺之战/assets/asset-status-20261005.md>)。
- 共102张执行卡：95张待生成／返工候选卡，7张条件或版式卡。这是完整资产清单的独立出图单元数，不是已批准图数，也不是拍摄必须新增的最低数量。合板按1张计；一张骑乘图跨三项资产复用只计1张。必要视角按现有镜头需求先做，未入镜的增强角度可后补，不把102张全做完当作局部G3的通用要求。
- 旧 `ALL-REMAINING-ASSETS` 为2026-10-02快照，含后续已完成项，不再逐行照做。本包排除了这些重复任务，未撤销旧版本留档。

## 推荐先做的六张（可分别制作候选）

1. UP-083：战前B0 V4，修复地面循环马蹄纹；没过之前别做B1/B2/B3。
2. UP-025：李嗣业持刀V2，只修刀尖几何，不再生成他已有全身角度。
3. UP-024：主角双手持B刀，验证手柄与衣甲受力；后续三张掌痕卡等它通过。
4. UP-026：仆固怀恩骑乘抬手；转向→加速→接敌后逐张接力。
5. UP-069：A头盔结构对齐，已缺左护耳绝不能再掉一次；M1/M2等本图通过。
6. UP-034：唐前军T0关系，固定主角左右A/B与后排C；后续减员图等它通过。

## 编号执行顺序与依赖

- 卡号是稳定Unit ID，不表示先把所有人物角度做完才能处理地表。
- 先做上述风险母图和下表所有无前置卡，可相互独立；引用文件存在但尚未批准的部分先制作候选，不把候选叫已验收。
- 再做有前置卡：只在列明上一张回传并批准或通过审核后解锁，允许同层不同资产并行。
- 同一状态链保持单向：B0→B1→B2→B3；Dusty→Damaged→Aftermath；T0→T1→T2→T3a→T3b→T4；P1发令→转向→加速→P2；U0→U1→U2→U3；燕步兵Y0→Y1→Y2→Y3→Y4；W0→W1→W2→W3；每件标记结构→M1→M2（现有M3只在结构一致时复用）。
- 空气卡最后引用已审环境及群体；不靠尘层遮盖结构错误。
- READY_FOR_CANDIDATE=50张无缺图前置的非条件卡；其他卡的WAITING_DEPENDENCY不自动放行。所有平台能力仍待核实，未指定生成平台，不提供虚构按钮/@语法/成本。

## 文件入口

| 内容 | 执行卡数 | 文件 |
|---|---:|---|
| 01-人物 | 16 | [01-characters.md](01-characters.md) |
| 02-衣甲 | 17 | [02-costumes.md](02-costumes.md) |
| 03-群体 | 25 | [03-groups.md](03-groups.md) |
| 04-道具 | 24 | [04-props.md](04-props.md) |
| 05-空间材质空气 | 18 | [05-world-and-atmosphere.md](05-world-and-atmosphere.md) |
| 06-字幕版式 | 2 | [06-graphics.md](06-graphics.md) |

## 使用与回传

1. 在对应文档找到卡号，看状态与前置。WAITING_DEPENDENCY卡先等待，不直接复制执行。
2. 打开你选择的生图平台的参考图/编辑任务入口；按卡内编号上传确切原图。平台不支持所需数量或局部编辑时先不要删掉身份/几何锚点，需缩小任务或改用支持的入口。
3. 卡内建议比例仅针对资产参考照，不锁最终电影画幅。单次1张；高质量原尺寸，平台参数未核实则不强填。
4. 只复制“直接复制｜主提示词”正文。不要把路径、状态、QC说明放进提示词。
5. 原图另存卡内确切文件名；对应目录尚不存在时随实际产物创建。禁止覆盖已有v001/v002，返工加版本。
6. 按UP编号回传图片或目录；有明确批准可说“UP-083审核通过”，否则交给Codex图片审核。回传路径与实际版本登记后才解锁依赖，文本卡本身不是产出。

## 已有但不应重复做

- 四名核心人物Canon/Body基础，安西头部五视图与身体六视图；李嗣业已有全身角度（左侧见用户拼版），郭子仪/仆固怀恩全身六方向。
- 李嗣业L0正背、L1正侧、L2、扣带板均已有；只安排持刀局部修正及必要近景条件项。
- 郭子仪正背双侧/45°衣甲、G0抬手、G1轻尘和工作室旗层级测试已有；只联合审核。工作室底座不进入战场。
- 仆固怀恩P0左侧静态骑乘已有；动态H1/H2/H3本包存COST-PUGU一处，分别交叉引用人物/服装/马具，不再同态生三遍。
- 长刀全形比较/结构/握距、三旗正反与前军F1/F4、三遗物M3、主马左侧V2、拓扑V2、五种基础材料已有。
- ATM-BF-ORDER-AFTERNOON-V1清洁空气优先复用通过的B0（无实际扬尘时），登记双用途，不另存复制图。是否具备人物/刀/远景可读性由后续同状态群体联合校准，不宣称空环境证明了演员。
- 燕步兵Y3/Y4同时覆盖FLAG F3退旗组合；旗密度在T0、中军F2与燕Y0/战场分区联合审核，不额外重复生密度图。
- 三遗物落点由B3/T4联合对齐，不另生不依赖空间的随机摆物图。
- 无字幕安全版复用通过的战后原图。身份文字和片尾最终文字后期可编辑排字，图片模型只做无字版式。

## 暂存／不自动复用的版本

- 主角C4 V1：伤痕消失；C4 V2连续性已修复，V3仅情绪区分失败时做。
- 主坐骑左侧V1：现代鞍错误；用V2。
- 郭子仪左侧衣甲V1：用V2；仆固怀恩45左V1：头身方向不一致，用45右候选锁正式组合。
- B0 V1/V2/V3：循环地面纹理未通过；不要作为后续状态父图。
- 旧六人V1、旧硬筒布M3 V1：不用；分别用V2。
- 旧材料V1地表/织物/皮革不覆盖各V2。

## 仍需验收，不等于缺图

演员角度与衣甲联合身份；C1/C3/C4情绪辨识；李L0/L1/L2扣带/裸露范围解释；郭中军层级与动作；骑乘双侧及动态受力；同列左右标志、减员与遗物；B型刀几何；战前战后地形与空气单向变化。局部失败只修对应资产与受影响卡，保持批准部分。

## 片尾史实文字边界

旧包提供的片尾工作文案不是最终已核验结论；尤其“次日”的时间关系不直接排字发布。本次不新增史实断言或伤亡比例，不渲染历史文字，待研究/剧本文案核验后再正式排字。阵列补位、人数减少、遗物与同构图空缺承担惨烈表达。

## 全部卡片清单

| 卡号 | Asset ID／任务 | 前置卡 | 执行类别 |
|---|---|---|---|
| [UP-001](01-characters.md#up-001) | CHAR-LISIYE-001／李嗣业独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-002](01-characters.md#up-002) | CHAR-LISIYE-001／李嗣业独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-003](01-characters.md#up-003) | CHAR-LISIYE-001／李嗣业独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-004](01-characters.md#up-004) | CHAR-LISIYE-001／李嗣业独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-005](01-characters.md#up-005) | CHAR-GUOZIYI-001／郭子仪独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-006](01-characters.md#up-006) | CHAR-GUOZIYI-001／郭子仪独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-007](01-characters.md#up-007) | CHAR-GUOZIYI-001／郭子仪独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-008](01-characters.md#up-008) | CHAR-GUOZIYI-001／郭子仪独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-009](01-characters.md#up-009) | CHAR-PUGU-001／仆固怀恩独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-010](01-characters.md#up-010) | CHAR-PUGU-001／仆固怀恩独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-011](01-characters.md#up-011) | CHAR-PUGU-001／仆固怀恩独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-012](01-characters.md#up-012) | CHAR-PUGU-001／仆固怀恩独立头部角度 | 现有参考 | 候选制作/返工 |
| [UP-013](01-characters.md#up-013) | CHAR-LISIYE-001／l1-regroup近景身份状态 | 现有参考 | 条件/版式 |
| [UP-014](01-characters.md#up-014) | CHAR-LISIYE-001／l2-advance近景身份状态 | 现有参考 | 条件/版式 |
| [UP-015](01-characters.md#up-015) | CHAR-GUOZIYI-001／郭子仪G1近景 | 现有参考 | 条件/版式 |
| [UP-016](01-characters.md#up-016) | CHAR-ANXI-001／C4情绪局部返工（条件项） | 现有参考 | 条件/版式 |
| [UP-017](02-costumes.md#up-017) | COST-ANXI-FRONT-001／观察人物自身左侧，左肩修补可见，严格90度全身侧面 | 现有参考 | 候选制作/返工 |
| [UP-018](02-costumes.md#up-018) | COST-ANXI-FRONT-001／观察人物自身右侧，右肩不新增修补，严格90度全身侧面 | 现有参考 | 候选制作/返工 |
| [UP-019](02-costumes.md#up-019) | COST-ANXI-FRONT-001／观察人物自身左前45度，左肩修补、胸甲、腰带同时可读 | 现有参考 | 候选制作/返工 |
| [UP-020](02-costumes.md#up-020) | COST-ANXI-FRONT-001／观察人物自身右前45度，不把左肩修补镜像到右肩 | 现有参考 | 候选制作/返工 |
| [UP-021](02-costumes.md#up-021) | COST-ANXI-FRONT-001／主角衣甲Dusty | 现有参考 | 候选制作/返工 |
| [UP-022](02-costumes.md#up-022) | COST-ANXI-FRONT-001／主角衣甲Damaged | UP-021 | 候选制作/返工 |
| [UP-023](02-costumes.md#up-023) | COST-ANXI-FRONT-001／主角衣甲Aftermath | UP-022 | 候选制作/返工 |
| [UP-024](02-costumes.md#up-024) | COST-ANXI-FRONT-001／主角双手持B型刀 | 现有参考 | 候选制作/返工 |
| [UP-025](02-costumes.md#up-025) | COST-LISIYE-001／李嗣业持刀局部校准 | 现有参考 | 候选制作/返工 |
| [UP-026](02-costumes.md#up-026) | COST-PUGU-001／P1抬手发令 | 现有参考 | 候选制作/返工 |
| [UP-027](02-costumes.md#up-027) | COST-PUGU-001／P1/H1转向受力 | UP-026 | 候选制作/返工 |
| [UP-028](02-costumes.md#up-028) | COST-PUGU-001／H2加速受力 | UP-027 | 候选制作/返工 |
| [UP-029](02-costumes.md#up-029) | COST-PUGU-001／P2/H3接敌后汗尘 | UP-028 | 候选制作/返工 |
| [UP-030](02-costumes.md#up-030) | COST-PUGU-001／骑装接触细节 | 现有参考 | 候选制作/返工 |
| [UP-031](03-groups.md#up-031) | GROUP-TANG-FRONT-001／A拉回同列受力 | 现有参考 | 候选制作/返工 |
| [UP-032](03-groups.md#up-032) | GROUP-TANG-FRONT-001／B握持失效受力 | 现有参考 | 候选制作/返工 |
| [UP-033](03-groups.md#up-033) | GROUP-TANG-FRONT-001／C从后排补位受力 | 现有参考 | 候选制作/返工 |
| [UP-034](03-groups.md#up-034) | GROUP-TANG-FRONT-001／唐前军T0 | 现有参考 | 候选制作/返工 |
| [UP-035](03-groups.md#up-035) | GROUP-TANG-FRONT-001／唐前军T1 | UP-034 | 候选制作/返工 |
| [UP-036](03-groups.md#up-036) | GROUP-TANG-FRONT-001／唐前军T2 | UP-035 | 候选制作/返工 |
| [UP-037](03-groups.md#up-037) | GROUP-TANG-FRONT-001／唐前军T3a | UP-036 | 候选制作/返工 |
| [UP-038](03-groups.md#up-038) | GROUP-TANG-FRONT-001／唐前军T3b | UP-037 | 候选制作/返工 |
| [UP-039](03-groups.md#up-039) | GROUP-TANG-FRONT-001／唐前军T4 | UP-038、UP-034 | 候选制作/返工 |
| [UP-040](03-groups.md#up-040) | GROUP-UYGHUR-CAV-001／U0侧向等候 | 现有参考 | 候选制作/返工 |
| [UP-041](03-groups.md#up-041) | GROUP-UYGHUR-CAV-001／三骑后向 | 现有参考 | 候选制作/返工 |
| [UP-042](03-groups.md#up-042) | GROUP-UYGHUR-CAV-001／四至六骑轮廓扩展 | 现有参考 | 候选制作/返工 |
| [UP-043](03-groups.md#up-043) | GROUP-UYGHUR-CAV-001／U1转东 | UP-040 | 候选制作/返工 |
| [UP-044](03-groups.md#up-044) | GROUP-UYGHUR-CAV-001／U2加速 | UP-043 | 候选制作/返工 |
| [UP-045](03-groups.md#up-045) | GROUP-UYGHUR-CAV-001／U3接敌后 | UP-044 | 候选制作/返工 |
| [UP-046](03-groups.md#up-046) | GROUP-YAN-001／燕步兵后向 | 现有参考 | 候选制作/返工 |
| [UP-047](03-groups.md#up-047) | GROUP-YAN-001／燕三骑侧向 | 现有参考 | 候选制作/返工 |
| [UP-048](03-groups.md#up-048) | GROUP-YAN-001／燕三骑后向 | 现有参考 | 候选制作/返工 |
| [UP-049](03-groups.md#up-049) | GROUP-YAN-001／燕步兵Y0 | 现有参考 | 候选制作/返工 |
| [UP-050](03-groups.md#up-050) | GROUP-YAN-001／燕步兵Y1 | UP-049 | 候选制作/返工 |
| [UP-051](03-groups.md#up-051) | GROUP-YAN-001／燕步兵Y2 | UP-050 | 候选制作/返工 |
| [UP-052](03-groups.md#up-052) | GROUP-YAN-001／燕步兵Y3 | UP-051 | 候选制作/返工 |
| [UP-053](03-groups.md#up-053) | GROUP-YAN-001／燕步兵Y4 | UP-052 | 候选制作/返工 |
| [UP-054](03-groups.md#up-054) | GROUP-YAN-001／燕骑迂回 | 现有参考 | 候选制作/返工 |
| [UP-055](03-groups.md#up-055) | GROUP-YAN-001／燕骑撤离 | UP-054 | 候选制作/返工 |
| [UP-056](04-props.md#up-056) | PROP-LONGBLADE-001／B刀W0材料基准 | 现有参考 | 候选制作/返工 |
| [UP-057](04-props.md#up-057) | PROP-LONGBLADE-001／W1汗尘 | UP-056 | 候选制作/返工 |
| [UP-058](04-props.md#up-058) | PROP-LONGBLADE-001／W2轻损 | UP-057 | 候选制作/返工 |
| [UP-059](04-props.md#up-059) | PROP-LONGBLADE-001／W3遗落 | UP-058 | 候选制作/返工 |
| [UP-060](04-props.md#up-060) | PROP-LONGBLADE-001／三角色刀差异 | UP-025 | 候选制作/返工 |
| [UP-061](02-costumes.md#up-061) | COST-ANXI-FRONT-001／主角战前握柄 | UP-024 | 候选制作/返工 |
| [UP-062](02-costumes.md#up-062) | COST-ANXI-FRONT-001／主角受力握柄 | UP-024、UP-061 | 候选制作/返工 |
| [UP-063](02-costumes.md#up-063) | COST-ANXI-FRONT-001／主角战后掌痕 | UP-024、UP-062 | 候选制作/返工 |
| [UP-064](04-props.md#up-064) | PROP-FLAGS-001／三旗无风垂落 | 现有参考 | 候选制作/返工 |
| [UP-065](04-props.md#up-065) | PROP-FLAGS-001／三旗同向侧风 | 现有参考 | 候选制作/返工 |
| [UP-066](04-props.md#up-066) | PROP-FLAGS-001／旗反面与杆绳细节 | 现有参考 | 候选制作/返工 |
| [UP-067](04-props.md#up-067) | PROP-FLAGS-001／F1前军倾旗由人承重 | 现有参考 | 候选制作/返工 |
| [UP-068](04-props.md#up-068) | PROP-FLAGS-001／F2中军维持旗号 | 现有参考 | 候选制作/返工 |
| [UP-069](04-props.md#up-069) | PROP-CONTINUITY-MARKERS-001／缺左护耳整顶头盔结构校核 | 现有参考 | 候选制作/返工 |
| [UP-070](04-props.md#up-070) | PROP-CONTINUITY-MARKERS-001／缺左护耳整顶头盔M1松脱 | UP-069 | 候选制作/返工 |
| [UP-071](04-props.md#up-071) | PROP-CONTINUITY-MARKERS-001／缺左护耳整顶头盔M2无人持有 | UP-069、UP-070 | 候选制作/返工 |
| [UP-072](04-props.md#up-072) | PROP-CONTINUITY-MARKERS-001／右前臂旧布结构校核 | 现有参考 | 候选制作/返工 |
| [UP-073](04-props.md#up-073) | PROP-CONTINUITY-MARKERS-001／右前臂旧布M1松脱 | UP-072 | 候选制作/返工 |
| [UP-074](04-props.md#up-074) | PROP-CONTINUITY-MARKERS-001／右前臂旧布M2无人持有 | UP-072、UP-073 | 候选制作/返工 |
| [UP-075](04-props.md#up-075) | PROP-CONTINUITY-MARKERS-001／C独特B刀结构校核 | 现有参考 | 候选制作/返工 |
| [UP-076](04-props.md#up-076) | PROP-CONTINUITY-MARKERS-001／C独特B刀M1松脱 | UP-075 | 候选制作/返工 |
| [UP-077](04-props.md#up-077) | PROP-CONTINUITY-MARKERS-001／C独特B刀M2无人持有 | UP-075、UP-076 | 候选制作/返工 |
| [UP-078](04-props.md#up-078) | PROP-HORSE-TACK-001／主马正斜 | 现有参考 | 候选制作/返工 |
| [UP-079](04-props.md#up-079) | PROP-HORSE-TACK-001／主马右侧 | 现有参考 | 候选制作/返工 |
| [UP-080](04-props.md#up-080) | PROP-HORSE-TACK-001／主马背面 | 现有参考 | 候选制作/返工 |
| [UP-081](04-props.md#up-081) | PROP-HORSE-TACK-001／马具组件 | 现有参考 | 候选制作/返工 |
| [UP-082](04-props.md#up-082) | PROP-HORSE-TACK-001／骑乘双侧接触 | 现有参考 | 候选制作/返工 |
| [UP-083](05-world-and-atmosphere.md#up-083) | LOC-BATTLEFIELD-001／B0地表重复纹理返工 | 现有参考 | 候选制作/返工 |
| [UP-084](05-world-and-atmosphere.md#up-084) | LOC-BATTLEFIELD-001／B1溃乱地表 | UP-083 | 候选制作/返工 |
| [UP-085](05-world-and-atmosphere.md#up-085) | LOC-BATTLEFIELD-001／B2推进地表 | UP-084、UP-083 | 候选制作/返工 |
| [UP-086](05-world-and-atmosphere.md#up-086) | LOC-BATTLEFIELD-001／B3战后原地 | UP-085、UP-083 | 候选制作/返工 |
| [UP-087](05-world-and-atmosphere.md#up-087) | LOC-BATTLEFIELD-001／唐前军朝燕军方向 | UP-083 | 候选制作/返工 |
| [UP-088](05-world-and-atmosphere.md#up-088) | LOC-BATTLEFIELD-001／追击走廊反看唐军后方 | UP-083 | 候选制作/返工 |
| [UP-089](05-world-and-atmosphere.md#up-089) | LOC-BATTLEFIELD-001／制作东翼走廊 | UP-083 | 候选制作/返工 |
| [UP-090](05-world-and-atmosphere.md#up-090) | LOC-BATTLEFIELD-001／地表尺度细节 | UP-083 | 候选制作/返工 |
| [UP-091](05-world-and-atmosphere.md#up-091) | MAT-BATTLEFIELD-001／织物汗湿可读性条件返工 | 现有参考 | 条件/版式 |
| [UP-092](05-world-and-atmosphere.md#up-092) | MAT-BATTLEFIELD-001／五材料三时段受光 | 现有参考 | 候选制作/返工 |
| [UP-093](05-world-and-atmosphere.md#up-093) | MAT-BATTLEFIELD-001／尘土局部附着 | 现有参考 | 候选制作/返工 |
| [UP-094](05-world-and-atmosphere.md#up-094) | ENV-ATMOSPHERE-001／ATM-BF-ROUT-AFTERNOON-V1 | UP-084、UP-035 | 候选制作/返工 |
| [UP-095](05-world-and-atmosphere.md#up-095) | ENV-ATMOSPHERE-001／ATM-CENTER-HOLD-AFTERNOON-V1 | UP-088 | 候选制作/返工 |
| [UP-096](05-world-and-atmosphere.md#up-096) | ENV-ATMOSPHERE-001／ATM-FRONT-REGROUP-AFTERNOON-V1 | UP-084、UP-036 | 候选制作/返工 |
| [UP-097](05-world-and-atmosphere.md#up-097) | ENV-ATMOSPHERE-001／ATM-FRONT-ADVANCE-LATEAFTERNOON-V1 | UP-085、UP-037 | 候选制作/返工 |
| [UP-098](05-world-and-atmosphere.md#up-098) | ENV-ATMOSPHERE-001／ATM-EAST-CAVALRY-LATEAFTERNOON-V1 | UP-089、UP-044 | 候选制作/返工 |
| [UP-099](05-world-and-atmosphere.md#up-099) | ENV-ATMOSPHERE-001／ATM-FRONT-TURN-DUSK-V1 | UP-085、UP-098 | 候选制作/返工 |
| [UP-100](05-world-and-atmosphere.md#up-100) | ENV-ATMOSPHERE-001／ATM-FRONT-AFTERMATH-DUSK-V1 | UP-086、UP-039 | 候选制作/返工 |
| [UP-101](06-graphics.md#up-101) | GRAPHIC-HISTORICAL-ID-001／三人物身份字幕无字版式 | 现有参考 | 条件/版式 |
| [UP-102](06-graphics.md#up-102) | GRAPHIC-HISTORICAL-ID-001／片尾字幕无字留白 | UP-086 | 条件/版式 |
