<!--
name: 'Tool Result: ToolSearch Schema Missing Guidance'
description: >-
  Error tool_result telling the model the tool's schema wasn't sent to the API
  and to load it via ToolSearch select:<name> before retrying.
ccVersion: 2.1.178
variables:
  - TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_0
  - TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_1
  - TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_2
-->

Load the tool first: call ${TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_0} with query "select:${TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_1.name}", then retry this call.${TOOL_RESULT_TOOLSEARCH_SCHEMA_MISSING_GUIDANCE_VAR_2}
