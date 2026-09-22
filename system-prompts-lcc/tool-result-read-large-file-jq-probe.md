<!--
name: Large-output read guidance (jq probe)
description: >-
  Tool-result guidance fragment to probe structure with jq before extracting
  slices.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_READ_LARGE_FILE_JQ_PROBE_VAR_0
-->
first probe the structure (e.g., jq 'type, length, keys?' ${TOOL_RESULT_READ_LARGE_FILE_JQ_PROBE_VAR_0}), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
