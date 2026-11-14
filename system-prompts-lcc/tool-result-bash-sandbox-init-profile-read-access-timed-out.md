<!--
name: 'Tool result: Bash sandbox init profile read access timed out'
description: >-
  Init failure reason that updating read access to the user profile did not
  finish in time and is recorded as incomplete
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_TIMED_OUT_VAR_0
-->
Bringing the read access to your user profile up to date did not finish in time, and it is recorded as incomplete. The next start of Claude Code tries it again, as does /sandbox install (see https://code.claude.com/docs/en/sandboxing). ${TOOL_RESULT_BASH_SANDBOX_INIT_PROFILE_READ_ACCESS_TIMED_OUT_VAR_0().replace(/\.$/,"")}
