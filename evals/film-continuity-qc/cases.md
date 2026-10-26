# Film Continuity QC V1 Cases

## CASE-Q01｜Manifest 声称成功但文件缺失

- **Expected：** 实际路径检查优先于日志；状态 MISSING_MEDIA / NOT_EVALUATED；不得引用 Prompt 推断通过。

## CASE-Q02｜完整视频存在

- **Expected：** 正常速度完整播放，再检查边界与问题区间；记录确切文件和工具证据。

## CASE-Q03｜漂亮首帧但运动穿模

- **Expected：** QC_FAIL_REWORK；静态美感不能掩盖手/道具接触和动作错误。

## CASE-Q04｜跨镜轴线或道具状态错误

- **Expected：** 记录前镜尾帧和后镜首帧证据，路由至 Generation/Prompt/Shot 的最早责任层。

## CASE-Q05｜轻微后期可修问题

- **Expected：** 只有不改变身份、动作和故事的稳定、裁切、颜色或声音问题可以 QC_PASS_WITH_NOTES 并交后期。

## CASE-Q06｜无动机灯光变化

- **Expected：** 同一 Look/Light State 的相邻镜头若光向、冷暖或材料响应无触发漂移，记录可见证据并退回最早责任层，不能以“更好看”接受。

## CASE-Q07｜模型能力伪支持

- **Expected：** Profile/覆盖回执标明不支持音频或负向提示，而执行包却声称已生效时，判 Prompt/Model Verification 返工，不以最终画面碰巧可用掩盖。
