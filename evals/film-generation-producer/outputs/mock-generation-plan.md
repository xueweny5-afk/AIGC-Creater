# GENERATION MANIFEST

## BATCH

- **Project ID：** TEST-EMOTION-OLD-MARKET
- **Batch ID：** BATCH-EVAL-S005-001
- **Prompt Package Version：** V0.1 Evaluation
- **Target Model / Version：** MOCK-CINEMA-I2V v1 — fictional evaluation profile
- **Mode：** PLAN_ONLY
- **Status：** RETURN
- **Authorization / Budget：** No external generation authorized; planned maximum is one initial attempt plus one explicitly approved diagnostic retry if a real model is later selected.
- **Stop Conditions：** Missing real input, unverified real model, no external authorization, attempt budget reached, or unknown previous request state.

## PREFLIGHT

| Check | Result | Evidence |
|---|---|---|
| Prompt package structurally available | PASS for evaluation | mock prompt package exists as Markdown |
| Real model profile | FAIL | MOCK-CINEMA-I2V v1 is explicitly fictional |
| Start frame path | FAIL | `/eval/frames/S005-SH04-F01.png` does not represent a proven workspace file |
| End frame path | FAIL | `/eval/frames/S005-SH04-F02.png` does not represent a proven workspace file |
| Character references | FAIL | `/eval/assets/CH-E01.png`, `CH-E02.png` are simulated |
| External service authorization | FAIL | not requested for framework testing |
| Output path | NOT CREATED | no generation should run |

## UNITS & TAKES

| Unit ID | Take ID | Attempt | Model | Request ID | Seed | Inputs | Output Path | Integrity | QC Status | Generation Status |
|---|---|---:|---|---|---|---|---|---|---|---|
| P-S005-SH04-CL01 | None | 0 | MOCK-CINEMA-I2V v1 | None | OPEN | simulated / unresolved | None | NOT_EVALUATED | NOT_EVALUATED | NOT_SUBMITTED |

## FAILURES & RETRIES

- No failure occurred because no request was submitted.
- Do not replace the mock profile with guessed Seedance/Kling/Veo settings.
- Resume only after a real target profile, existing approved files and user authorization are available.

## NEXT STAGE

- **Primary Recommendation：** Stop
- **Reason：** This is a framework-only evaluation with fictional model/input data; no Take exists and no QC handoff is permitted.

