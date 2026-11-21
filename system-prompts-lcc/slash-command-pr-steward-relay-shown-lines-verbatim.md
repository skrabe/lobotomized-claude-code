<!--
name: 'Slash command: PR Steward relay after shown lines'
description: >-
  Tells Claude that Claude Code already showed some lines and to relay the given
  text in those words only
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_RELAY_SHOWN_LINES_VERBATIM_VAR_0
  - SLASH_COMMAND_PR_STEWARD_RELAY_SHOWN_LINES_VERBATIM_VAR_1
-->
${SLASH_COMMAND_PR_STEWARD_RELAY_SHOWN_LINES_VERBATIM_VAR_0} Tell the user this, in these words, and do nothing else:

${SLASH_COMMAND_PR_STEWARD_RELAY_SHOWN_LINES_VERBATIM_VAR_1}
