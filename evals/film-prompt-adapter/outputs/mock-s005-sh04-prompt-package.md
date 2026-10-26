# PROMPT PACKAGE

> EVALUATION ONLY：使用虚构模型与模拟路径，不能提交真实平台。

## PACKAGE IDENTITY

- **Project ID：** TEST-EMOTION-OLD-MARKET
- **Package Version：** V0.1 Evaluation
- **Package Status：** READY FOR GENERATION within evaluation fixture only
- **Unit：** P-S005-SH04-CL01

## MODEL PROFILE RECEIPT

- **Target Model / Version：** MOCK-CINEMA-I2V v1
- **Task Type：** Image-to-Video
- **Source / URL：** Local evaluation fixture; not a real model
- **Access Date：** 2026-09-18
- **Profile Status：** VERIFIED WITHIN EVAL FIXTURE
- **Confirmed Capabilities：** 5–8s, 16:9, 1080p, start/end frame, up to two identity refs, natural-language camera motion, negative prompt, integer seed.
- **Unknown / Account-dependent：** None inside fixture; no real-world claim.

## SOURCE VERSION LOCK

- Motion Spec: `emotional-old-market-s005-motion-spec.md` V0.1, `READY FOR PROMPT ADAPTATION`
- Shot: S005-SH04, 7s
- Frames: S005-SH04-F01 / F02, evaluation READY fixture
- Assets: LOC-E01, CH-E01, CH-E02, PROP-E01, PROP-E02 v001 evaluation fixture

## INPUT FILE MAP

| Input | Fixture Path | Role |
|---|---|---|
| Start frame | `/eval/frames/S005-SH04-F01.png` | 锁定许可后扫帚刚进入共享通道的起始状态 |
| End frame | `/eval/frames/S005-SH04-F02.png` | 锁定通道清理、卷帘门下降与半量夹子保留的结束状态 |
| CH-E01 identity | `/eval/assets/CH-E01.png` | 保持西侧长期经营者身份 |
| CH-E02 identity | `/eval/assets/CH-E02.png` | 保持东侧邻摊经营者身份 |

## PROMPT UNITS

### P-S005-SH04-CL01

- **Task Type：** Image-to-Video
- **Source IDs：** S005-SH04-CL01, S005-SH04-F01/F02
- **Input Files：** 上述四个 fixture inputs
- **Copy-ready Prompt：**

  `Preserve the exact identities, clothing, adjacent-stall layout, south shared aisle, half-set of clips, evening light direction, and start-frame composition. The older stall keeper remains inside the west stall on screen-left; the neighboring vendor remains inside the east stall on screen-right. From 0 to 2.5 seconds, the neighboring vendor completes two grounded broom strokes only across the shared aisle, with the broom head maintaining contact and never entering the west private work area; the older stall keeper performs one small packing action as secondary motion. From 2.5 to 4 seconds, the neighboring vendor stops sweeping and returns fully to the east work area while both people settle. From 4 to 6 seconds, the shutters descend one after another as both people make one final check of their own stalls. From 6 to 7 seconds, both briefly look toward the remaining half-set of clips and hold, without looking at each other. Camera stays locked from 0 to 4 seconds; when the shutters begin descending at 4 seconds, make one slow straight backward camera translation, stopping by 6.5 seconds when both stalls, the clean shared aisle, and the clips are visible together; hold to the end. End exactly in the supplied end-frame state. No dialogue or generated audio.`

- **Negative Prompt / Exclusions：**

  `no identity change, no age change, no clothing change, no extra people entering, no tray, no full set of clips, no market closure notice, no farewell, no smiling reconciliation, no broom entering the west work area, no floating broom, no hand deformation, no mirrored stalls, no axis reversal, no pan, no tilt, no zoom, no camera orbit, no text, no logo, no watermark`

- **Parameters & Provenance：**
  - duration: `7s` — `USER/CREATIVE_MASTER_LOCKED`
  - aspect ratio: `16:9` — `ADAPTER_DEFAULT` within fixture profile
  - resolution: `1080p` — `OFFICIAL_PROFILE` inside fixture
  - start/end frame: enabled — `OFFICIAL_PROFILE` inside fixture
  - identity references: 2 — `OFFICIAL_PROFILE` inside fixture
  - seed: OPEN — supported by fixture; Generation stage may set and log it
- **Expected Start / Action / End：** Start at approved crossing state → clean shared aisle in two strokes → return to own spaces → shutters descend → brief shared-object glance → approved end frame.
- **Continuity Anchors：** CH-E01 west/screen-left; CH-E02 east/screen-right; half clips remain; tray absent; broom only in shared aisle; same light direction.
- **Unsupported / Degraded：** Audio generation unsupported. All production sound and shutter/sweeping audio must be created or synchronized in post-production; prompt explicitly requests no generated audio.
- **Fallback：** If camera translation destabilizes layout, rerun with camera locked for all 7s. If hand/broom contact fails, preserve the start/end frames and simplify secondary CH-E01 packing, never remove the broom boundary rule.
- **Verification Checklist：** Identity, west/east topology, broom contact, two strokes, no private-area crossing, clips count, tray absence, shutter timing, camera only after 4s, final state match.

## COMPATIBILITY & DEGRADATION

- All required visual inputs and 7s duration are supported by the mock profile.
- Audio is deliberately routed out of generation; creative sound intent remains in Motion Spec for post-production.
- Optional camera movement has an approved locked-camera fallback that preserves story meaning.

## REVERSE-CHECK

- **Subject：** Two approved vendors in fixed west/east stalls.
- **Start：** Permission already given; broom begins entering only the shared aisle.
- **Trigger：** The prior permission and resumed sweeping.
- **Action order：** Two sweeps → return to own spaces → shutters descend → glance to shared clips → hold.
- **Camera：** Locked first 4s; optional straight backward translation from shutter trigger to stable two-stall end; no rotation or zoom.
- **End：** Clean shared aisle, people in own stalls, shutters mostly down, half clips remain, tray absent.
- **Protected continuity：** Identities, topology, axis, props, light and no farewell behavior.
- **Result：** PASS within evaluation fixture.

## GENERATION ORDER

1. Verify all four fixture inputs resolve.
2. Run one locked-camera diagnostic take if desired.
3. Run the designed conditional-backward-move take.
4. Generation Producer records seed, settings, output IDs and failures; no result is implied here.

## DECISION REGISTER

- **LOCKED：** 7s, start/end states, primary action, axis, prop state.
- **OPEN：** generation seed; whether fallback locked camera becomes selected take.
- **EVAL ONLY：** model profile and paths are simulated.

## NEXT STAGE

- **Primary Recommendation：** Generation
- **Reason：** Within the isolated evaluation fixture, target capability, input mapping, compact prompt, parameters, fallback and reverse-check are complete; no generation has been run.

