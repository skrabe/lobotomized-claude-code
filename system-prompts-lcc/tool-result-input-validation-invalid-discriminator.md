<!--
name: 'Tool Result: input validation invalid discriminator'
description: >-
  Default schema issue message for a discriminated union whose tag matches no
  option.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_INPUT_VALIDATION_INVALID_DISCRIMINATOR_VAR_0
  - TOOL_RESULT_INPUT_VALIDATION_INVALID_DISCRIMINATOR_VAR_1
-->
Invalid discriminator value. Expected ${TOOL_RESULT_INPUT_VALIDATION_INVALID_DISCRIMINATOR_VAR_0.options.map((TOOL_RESULT_INPUT_VALIDATION_INVALID_DISCRIMINATOR_VAR_1)=>`'${TOOL_RESULT_INPUT_VALIDATION_INVALID_DISCRIMINATOR_VAR_1}'`).join(" | ")}
