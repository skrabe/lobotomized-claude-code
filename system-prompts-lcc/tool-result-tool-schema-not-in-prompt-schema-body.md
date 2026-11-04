<!--
name: 'Tool Result: Unloaded tool schema body'
description: >-
  Appendix to a failed deferred-tool call giving the input schema and telling
  the model to correct and retry.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SCHEMA_BODY_VAR_0
  - TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SCHEMA_BODY_VAR_1
-->
The input schema is: ${TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SCHEMA_BODY_VAR_0}
If your input does not match this schema, correct it and call the tool again. If it matches, the error above has another cause. If the corrected call fails the same way, ${TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SCHEMA_BODY_VAR_1}
