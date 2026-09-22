<!--
name: Parameter type validation summary
description: Aggregated tool-input parameter-type validation error returned to the model.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_PARAM_TYPE_VALIDATION_SUMMARY_VAR_0
  - TOOL_RESULT_PARAM_TYPE_VALIDATION_SUMMARY_VAR_1
-->
${TOOL_RESULT_PARAM_TYPE_VALIDATION_SUMMARY_VAR_0} failed due to the following ${TOOL_RESULT_PARAM_TYPE_VALIDATION_SUMMARY_VAR_1.length>1?"issues":"issue"}:
${TOOL_RESULT_PARAM_TYPE_VALIDATION_SUMMARY_VAR_1.join(`
`)}
