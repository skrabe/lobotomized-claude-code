<!--
name: Large-output read guidance (jq summarize)
description: >-
  Tool-result guidance fragment to extract full content with jq/python and
  summarize verbatim.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_READ_LARGE_FILE_JQ_SUMMARIZE_VAR_0
  - TOOL_RESULT_READ_LARGE_FILE_JQ_SUMMARIZE_VAR_1
-->
${TOOL_RESULT_READ_LARGE_FILE_JQ_SUMMARIZE_VAR_0} is ${TOOL_RESULT_READ_LARGE_FILE_JQ_SUMMARIZE_VAR_1}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.
