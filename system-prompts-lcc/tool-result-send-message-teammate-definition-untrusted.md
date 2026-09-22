<!--
name: Send Message Teammate Definition Untrusted
description: >-
  Appended to the teammate-resume tool_result when the agent definition folder
  is not trusted.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_SEND_MESSAGE_TEAMMATE_DEFINITION_UNTRUSTED_VAR_0
-->
Its agent definition was not restored: the folder its definition file came from is not trusted (source: ${TOOL_RESULT_SEND_MESSAGE_TEAMMATE_DEFINITION_UNTRUSTED_VAR_0.source}), so the teammate is running with the team-essential tools and no custom instructions. To restore it, the user needs to run Claude Code in that folder once and accept the trust dialog (the --debug log names the folder); do not change trust settings on the user's behalf.
