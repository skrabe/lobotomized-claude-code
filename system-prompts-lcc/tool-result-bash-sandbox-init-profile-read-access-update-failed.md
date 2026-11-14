<!--
name: 'Tool result: Bash sandbox init profile read access update failed'
description: >-
  Init failure reason that updating read access to the user profile failed or
  was ended, with retry guidance and details
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_1
  - TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_2
-->
Bringing the read access to your user profile up to date ${TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_0}. The next start of Claude Code tries it again, as does /sandbox install (see https://code.claude.com/docs/en/sandboxing)${TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_1===""?"":`. (Details: ${TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_2(TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_UPDATE_FAILED_VAR_1)})`}
