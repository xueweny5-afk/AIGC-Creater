# PROMPT MANIFEST

## PACKAGE

- **Project ID：** TEST-EMOTION-OLD-MARKET
- **Package Version：** V0.1 Evaluation
- **Target Model / Version：** MOCK-CINEMA-I2V v1
- **Profile Status：** VERIFIED WITHIN EVAL FIXTURE
- **Package Status：** READY FOR GENERATION within evaluation fixture only

## UNITS

| Unit ID | Task Type | Source ID | Inputs | Duration / Size | Prompt Package | Status |
|---|---|---|---|---|---|---|
| P-S005-SH04-CL01 | I2V | S005-SH04-CL01 | start/end + CH-E01/02 refs | 7s, 16:9, 1080p | `mock-s005-sh04-prompt-package.md` | READY — EVAL ONLY |

## GENERATION ORDER

1. Resolve and checksum inputs.
2. Run unit once with logged seed/settings.
3. Inspect output before any selection or retry.

## BLOCKING ISSUES

- None inside fixture; all paths and model capabilities are simulated and unavailable for real execution.

## NEXT STAGE

- **Primary Recommendation：** Generation
- **Reason：** Evaluation contract is complete; real projects must replace the mock profile and paths with verified current sources and existing files.

