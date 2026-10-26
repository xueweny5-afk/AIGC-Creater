# GENERATION MANIFEST

## BATCH

- **Project ID：**
- **Batch ID：**
- **Prompt Package Version：**
- **Production Unit Card Version / Source Freshness：** CURRENT / STALE / BLOCKED / RECOMPILE
- **Adopted Method IDs / Versions / Pilot Status：**
- **Target Model / Version：**
- **Provider / Platform / Task Entry / Input Mode / Profile Evidence：**
- **Mode：** PLAN_ONLY / USER_HANDOFF / GENERATE / RESUME / RETRY
- **Batch Class：** TECHNICAL_PILOT / PRODUCTION
- **Pilot Gate：** NOT_REQUIRED / REQUIRED / RUNNING / PILOT_VALIDATED / PILOT_FAILED_RETURN / USER_ACCEPTED_RISK
- **Gate Evidence / Accepted Risks / Unit-Model-Entry Scope / Remaining Unvalidated Risks：**
- **Status：** PLANNED / RUNNING / PARTIAL / GENERATED_PENDING_QC / STOPPED / RETURN
- **Authorization / Budget：**
- **Stop Conditions：**
- **Model Routing Pilot Path / Status：** NOT_REQUIRED / PLANNED / RUNNING / QC_PENDING / VALIDATED / RETURN

## PREFLIGHT

| Unit ID | Package / Card Status | Prompt Review / Freshness | Profile Entry Match | File-Version / Approval Scope | Dependency / Pilot Evidence | Result / Blocking Reason |
|---|---|---|---|---|---|---|

CONTENT DRAFT、NOT_READY 和未满足依赖不可提交；计划不要求先回传媒体。

## BUDGET LEDGER

| Unit / Batch | Attempt Cap / Submitted Count | In-flight Requests | Authorized Cost Cap | Reported Actual Cost | In-flight Reservation / Basis | Unsettled-Unknown Charges | Remaining Safe Headroom | Currency / Credit Unit |
|---|---|---|---|---|---|---|---|---|

预留与结算分列、转换不双计，未知写 UNKNOWN；查询/下载不占生成尝试，独立费用仍入账。

## UNITS & TAKES

本阶段 QC Status 保持 NOT_EVALUATED；未人工批准的可用 Take 交 GENERATED_PENDING_QC，人工批准另记 USER-APPROVED 范围，不填 QC_PASS。

| Unit ID | Risk Hypothesis / Changed Variable | Held Constant / Confounds | Source Freshness | Depends On / State Change | Dependency Status | Take ID | Attempt | Model | Request ID | Seed | Inputs | Output Path | Integrity | QC Status | Generation Status |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|

## FAILURES & RETRIES

| Unit / Attempt | Failure Class / Symptom | Authoritative Task Evidence | Recovery Action | Diagnostic Hypothesis / Authorized Changed Fields | Budget Update | Stop / Return Basis |
|---|---|---|---|---|---|---|

Recovery Action: QUERY / RETRIEVE / NEW_SUBMISSION / NONE。

## USER HANDOFF & RETURNS

| Unit / Take / Version or Unmatched Return | Handoff / Returned File Path | Mapping Evidence / Gap | Provided Model-Parameter-Cost / UNKNOWN | Integrity | User Approval / Scope / Time | State Evidence / Dependent Release |
|---|---|---|---|---|---|---|

未回传保持 NOT_SUBMITTED，无法对应时不猜测 Unit；人工批准不冒充 QC_PASS 或整段通过。

## LEARNING CASE CANDIDATES

| Candidate ID | Baseline Take | Candidate Take | Hypothesis / Changed Variable | Unchanged Fields / Confounds | QC Status | Curator Route |
|---|---|---|---|---|---|---|

## NEXT STAGE

- **Primary Recommendation：** Generate / Resume / Continuity QC / Prompt Return / Stop
- **Reason：**
