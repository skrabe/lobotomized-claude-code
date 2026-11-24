<!--
name: 'Slash Command: Steward .claude settings set gh/git variable'
description: >-
  Steward refusal when the checkout's .claude settings set a gh/git/proxy
  variable
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_CLAUDE_SETTINGS_SET_GH_GIT_VARIABLE_VAR_0
  - SLASH_COMMAND_STEWARD_CLAUDE_SETTINGS_SET_GH_GIT_VARIABLE_VAR_1
-->
this checkout's .claude settings set ${/^\w{1,40}$/.test(SLASH_COMMAND_STEWARD_CLAUDE_SETTINGS_SET_GH_GIT_VARIABLE_VAR_0)?SLASH_COMMAND_STEWARD_CLAUDE_SETTINGS_SET_GH_GIT_VARIABLE_VAR_0:"a variable for gh or git"}, ${SLASH_COMMAND_STEWARD_CLAUDE_SETTINGS_SET_GH_GIT_VARIABLE_VAR_1}
