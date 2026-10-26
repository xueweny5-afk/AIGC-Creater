# Motion Specification｜v1

- Clip：`SH01 / UNIT01`，8.0s / 24 fps / 760×950，来源 `PLATE01/v1`、`CG01/v1`、`NLA01/LL01/AM01`。
- Camera：图生视频中的连续镜头。`0–1.5s` 稳定观察；`1.5–6.5s` 缓慢 dolly-in 并小幅 truck-right，保持原图可见区域与地标关系；`6.5–8s` 缓缓减速并停在灯塔与海岸。禁止突然变焦、摇晃、绕到人物正面或揭示图外空间。
- Source coverage：人物可逐渐退至左缘；栏杆、海岸和灯塔必须保持可见，不要求灯塔移到正中央。
- Performance：人物身体与视线保持；围巾边缘随画内风轻微摆动。Environment：海面浪花低幅连续翻涌，礁石和建筑固定；云层近乎静止。Light：灯塔灯光持续稳定，不闪烁。
- Failure hypothesis：图生视频可能重绘人物、移动灯塔、扭曲栏杆、制造突然变焦或新增图外空间；这些进入后续真实 Take 的 QC。当前没有生成 Take，不宣称 G5 已验证。
- Handoff：交给 Stage 13 的模型中立提示词包；目标模型未指定，执行状态保持 `MODEL VERIFICATION REQUIRED`。
