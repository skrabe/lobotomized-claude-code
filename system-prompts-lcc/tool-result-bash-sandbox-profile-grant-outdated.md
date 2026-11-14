<!--
name: Profile read grant outdated
description: The recorded profile read grant cannot be used; grant or forget it again.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_1
-->
The recorded read grant on your user profile cannot be used (${TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_0.state}${TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_0.reason?`: ${TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_0.reason}`:""}). Call grantWindowsProfileRead() (\`srt-win profile grant\`, or \`${TOOL_RESULT_BASH_SANDBOX_PROFILE_GRANT_OUTDATED_VAR_1}\` again) as the user who starts sessions to bring it up to date, or forgetWindowsProfileRead() (\`srt-win profile forget\`) to run without reading the profile. initialize() does neither itself for a grant in this state.
