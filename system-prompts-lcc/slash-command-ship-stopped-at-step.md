<!--
name: 'Ship: you stopped it at step'
description: Ship outcome line telling which step the user stopped the run at.
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_SHIP_STOPPED_AT_STEP_VAR_0
  - SLASH_COMMAND_SHIP_STOPPED_AT_STEP_VAR_1
-->
You stopped ${SLASH_COMMAND_SHIP_STOPPED_AT_STEP_VAR_0} ${["before it did anything","during the commit","before it pushed anything","during the push"][SLASH_COMMAND_SHIP_STOPPED_AT_STEP_VAR_1-1]}.
