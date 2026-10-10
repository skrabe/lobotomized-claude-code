<!--
name: 'Tool Result: Personal config hook event unsupported'
description: >-
  Explains personal hooks on certain events are not allowed in this session
  except command and http hooks
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_PERSONAL_CONFIG_HOOK_EVENT_UNSUPPORTED_VAR_0
  - TOOL_RESULT_PERSONAL_CONFIG_HOOK_EVENT_UNSUPPORTED_VAR_1
-->
these hooks in ${TOOL_RESULT_PERSONAL_CONFIG_HOOK_EVENT_UNSUPPORTED_VAR_0} are on ${TOOL_RESULT_PERSONAL_CONFIG_HOOK_EVENT_UNSUPPORTED_VAR_1.slice(0,-1).join(", ")} or ${TOOL_RESULT_PERSONAL_CONFIG_HOOK_EVENT_UNSUPPORTED_VAR_1.at(-1)}, where only command and http hooks are allowed in this session
