<!--
name: 'Tool Result: Steward watch unlisted code host CLI call'
description: >-
  Hook refusal reason when a shell line looks like a call of a code host's
  command-line tool that is not one of the watch's listed commands
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_WATCH_UNLISTED_CODE_HOST_CLI_CALL_VAR_0
  - TOOL_RESULT_STEWARD_WATCH_UNLISTED_CODE_HOST_CLI_CALL_VAR_1
-->
\`${[TOOL_RESULT_STEWARD_WATCH_UNLISTED_CODE_HOST_CLI_CALL_VAR_0,...TOOL_RESULT_STEWARD_WATCH_UNLISTED_CODE_HOST_CLI_CALL_VAR_1].join(" ")} …\` looks like a call of a code host's command-line tool, which isn't one of this watch's listed commands
