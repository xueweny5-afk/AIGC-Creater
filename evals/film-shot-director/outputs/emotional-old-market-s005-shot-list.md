# SHOT LIST

## SHOT PLAN IDENTITY

- **Project ID：** TEST-EMOTION-OLD-MARKET
- **Version：** V0.1 Evaluation
- **Scene Design Version：** EVAL FIXTURE S005 READY
- **Asset Manifest Version：** EVAL FIXTURE APPROVED v001
- **Scope：** S005 only
- **Aspect Ratio：** [ASSUMED] 16:9

## COVERAGE & STATUS

- **Status：** READY FOR STORYBOARD
- **Covered Scenes：** S005
- **Blocking Issues：** None within evaluation fixture。

## SCENE SHOT SENTENCES

- **S005：** 先在同一空间中看见两人各自收摊，让扫帚抵达分界并停住；随后把注意力交给老摊主的看见、移筐和允许；最后回到两人共享但不相互接管的空间，让卷帘门和半量夹子结束场景。

## WORLD COORDINATES & AXIS RULES

- 两摊沿东西方向相邻；CH-E01 固定在西侧工作面，CH-E02 固定在东侧工作面；共享通道位于南侧。
- 主关系轴连接东西两摊。摄影机默认位于通道南侧，向北观察；因此 CH-E01 投影在画面左侧，CH-E02 投影在画面右侧。
- 本镜头链不越轴。扫帚从东侧向西抵达分界，只在许可后进入共享通道；不进入 CH-E01 工作面。
- 主要实用光源与收摊时间状态保持一致；不得在反向镜头中翻转来源方向。

## SHOT LIST

| Shot ID | Duration | Function | Framing / Angle | Camera / Lens Intent | Blocking & Visible Action | Movement | Dialogue / Sound | Cut Motive | Continuity | Assets | Risk |
|---|---:|---|---|---|---|---|---|---|---|---|---|
| S005-SH01 | 6s | 建立两人仍各自工作的空间和新边界 | 双人全景，正常视高，保留两摊分界与通道 | 通道南侧中央；自然透视，空间关系优先，不压缩两摊距离 | CH-E01 在西侧扎纸袋；CH-E02 在东侧取下夹单、拿起扫帚，从自己摊前扫向分界；半量夹子可见，托盘缺席 | 静止；让人物动作完成空间建立 | 纸袋、夹子、扫地声；无对白 | 扫帚抵达分界并停止，产生信息转折 | In：两摊收摊；Out：扫帚停在分界，CH-E01 尚未回应 | LOC-E01, CH-E01, CH-E02, PROP-E01, PROP-E02 | 双人手部动作并行；必须控制但不省略夹子状态 |
| S005-SH02 | 5s | 让“停住并等待”成为可读的请求，而不是操作失误 | CH-E02 中近景偏侧，扫帚和分界同时在可读范围 | 通道南偏东，仍在轴线南侧；适度压缩背景但保留分界深度 | CH-E02 扫到分界后停住，身体不跨入西侧；视线转向 CH-E01；扫帚保持静止 | 静止；不推近，让等待时长承担意义 | 扫地声中断；其余收摊声继续 | CH-E01 看见停顿，注意力转移到接收者 | In：扫帚停住；Out：CH-E02 等待，CH-E01 已看到 | CH-E02, LOC-E01, PROP-E02 | 扫帚与分界接触关系需稳定；避免把停顿演成羞怯 |
| S005-SH03 | 5s | 展示许可由可见行动和一句话完成 | CH-E01 中景，保留脚边小筐与画面右缘等待的扫帚 | 通道南偏西，仍在同侧；自然透视，让提筐和扫帚边缘同处关系空间 | CH-E01 看向分界，提走脚边小筐，腾出共享通道；动作完成后说“扫吧” | 静止；提筐是注意和关系变化的主体 | CH-E01：“扫吧。”随后扫地声重新开始 | 允许已经明确，切回空间验证其后果 | In：CH-E01 已看到；Out：小筐移开，许可完成，扫帚开始越界 | CH-E01, LOC-E01, PROP-E02 | 提筐、对白和扫帚重启的时序需清楚；避免夸张反应 |
| S005-SH04 | 7s | 验证新规则并收束为继续的日常 | 双人全景，回到 S005-SH01 的空间关系，稍多保留卷帘门与共享通道 | 通道南侧中央；与 SH01 相同透视基准，允许轻微后移以容纳卷帘门状态，但不改变轴线 | CH-E02 只扫过共享通道；CH-E01 完成自己的收纳。卷帘门陆续落下。两人各自检查摊位，视线短暂停在半量夹子处；托盘仍缺席 | 若空间允许，人物完成主要动作后摄影机缓慢后移；触发是共享通道清扫完成，终点是两摊与半量夹子同时留在完整关系中；无条件则保持静止 | 清扫、收纳、卷帘门声；无对白，不加告别性音乐提示 | 卷帘门声与两人短暂停顿共同结束场景，不再切反应特写 | In：许可后扫帚越界；Out：通道清理完成，半量夹子保留，日常结束但关系继续 | 全部 P0/P1 | 后移可能增加空间漂移风险；若生成稳定性不足，采用静止版本 |

## TIMING SUMMARY

| Scene | Target | Shot Total | Difference | Status |
|---|---:|---:|---:|---|
| S005 | [ASSUMED ESTIMATE] 23s | 23s | 0s | Closed for evaluation |

## COVERAGE AUDIT

- 停住：S005-SH01 尾部与 SH02 全程。
- 看见：SH02 尾部至 SH03 开始。
- 提走小筐与明确允许：SH03。
- 扫帚经许可后跨入共享通道：SH03 声音重启、SH04 可见结果。
- 半量夹子与托盘缺席：SH01 建立、SH04 回收。
- 卷帘门与沉默收束：SH04。
- 未加入市场关闭、拥抱、告别或未来说明。

## PRODUCTION RISKS

- SH01 同时包含双人手部动作和小道具状态，Storyboard 阶段应分别确认主注意与背景连续性。
- SH04 可选后移需验证场景拓扑；如实际生成造成空间漂移，保留静止方案，不改变场景意义。
- 半量夹子属于小尺寸连续性锚点，需要批准参考图或后期可控方案。

## DECISION REGISTER

### LOCKED

- 世界坐标、关系轴、分界停顿、提筐许可、共享通道清扫、半量夹子与托盘缺席。

### OPEN

- 最终片长、确切摄影格式、是否采用 SH04 后移版本。

### ASSUMED

- 16:9；S005 目标约 23 秒；使用 Lens Intent 而不编造焦距数值。

## NEXT STAGE

- **Primary Recommendation：** Storyboard Design
- **Reason：** S005 的动作、信息、时长、轴线、连续性与镜头功能已闭合，可将四个镜头转为可审核画面板。

