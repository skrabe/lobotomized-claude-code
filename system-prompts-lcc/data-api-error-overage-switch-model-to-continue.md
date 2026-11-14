<!--
name: 'Data: API error overage switch model to continue'
description: >-
  Suffix of the seven-day overage rate-limit API error telling to switch models
  or manage usage credits to continue.
ccVersion: 2.1.325
variables:
  - DATA_API_ERROR_OVERAGE_SWITCH_MODEL_TO_CONTINUE_VAR_0
  - DATA_API_ERROR_OVERAGE_SWITCH_MODEL_TO_CONTINUE_VAR_1
-->
. Switch to another model${DATA_API_ERROR_OVERAGE_SWITCH_MODEL_TO_CONTINUE_VAR_0?`, or manage usage credits at ${DATA_API_ERROR_OVERAGE_SWITCH_MODEL_TO_CONTINUE_VAR_1()},`:""} to continue.
