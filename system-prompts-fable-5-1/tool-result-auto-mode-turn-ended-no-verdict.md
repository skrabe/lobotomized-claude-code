<!--
name: Turn Ended No Verdict
description: >-
  Permission denial telling the model auto mode ended the turn and not to act
  until the next user message.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_AUTO_MODE_TURN_ENDED_NO_VERDICT_VAR_0
  - TOOL_RESULT_AUTO_MODE_TURN_ENDED_NO_VERDICT_VAR_1
-->
Auto mode is unavailable: the server returned no safety verdict for ${TOOL_RESULT_AUTO_MODE_TURN_ENDED_NO_VERDICT_VAR_0} responses in a row, so ${TOOL_RESULT_AUTO_MODE_TURN_ENDED_NO_VERDICT_VAR_1} was not run and this turn has ended. Wait for the user's next message before doing anything further.
