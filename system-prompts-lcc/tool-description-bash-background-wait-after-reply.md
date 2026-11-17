<!--
name: 'Tool Description: Bash background wait after reply'
description: >-
  Bash prompt clause: after the reply the session waits up to N minutes for a
  background command's end; later ends reach Claude only when the user writes,
  so say what is still running.
ccVersion: 2.1.326
variables:
  - TOOL_DESCRIPTION_BASH_BACKGROUND_WAIT_AFTER_REPLY_VAR_0
  - TOOL_DESCRIPTION_BASH_BACKGROUND_WAIT_AFTER_REPLY_VAR_1
-->
 After your reply, this session waits for a background command's end for up to ${TOOL_DESCRIPTION_BASH_BACKGROUND_WAIT_AFTER_REPLY_VAR_0} ${TOOL_DESCRIPTION_BASH_BACKGROUND_WAIT_AFTER_REPLY_VAR_1(TOOL_DESCRIPTION_BASH_BACKGROUND_WAIT_AFTER_REPLY_VAR_0,"minute")} from its start. An end after that, after a restart of the server behind this session, or after many such wake-ups with no message from the user reaches you only when the user writes again, so tell the user what is still running.
