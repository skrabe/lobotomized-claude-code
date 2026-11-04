<!--
name: 'System Reminder: Code Mode auto mode agent message refusal'
description: >-
  Explains auto mode cannot inspect a message that Code Mode code sends to an
  agent and directs the user to leave auto mode to retry
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_CODE_MODE_AUTO_MODE_AGENT_MESSAGE_REFUSAL_VAR_0
-->
This ${SYSTEM_REMINDER_CODE_MODE_AUTO_MODE_AGENT_MESSAGE_REFUSAL_VAR_0} call was NOT run. In this session, your code can't send a message to an agent while auto mode is on, because auto mode checks the code before it runs and can't read the text that the code then sends. This is not a judgment that the message is unsafe. Tell the user that they can leave auto mode with Shift+Tab, for example for Manual mode, and then ask you to try again.
