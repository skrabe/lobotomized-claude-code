<!--
name: 'Tool Result: GetGoal session goal'
description: >-
  GetGoal result stating the session goal condition, with optional paused and
  evaluator-reason lines
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_GETGOAL_SESSION_GOAL_VAR_0
-->
Session goal: ${TOOL_RESULT_GETGOAL_SESSION_GOAL_VAR_0.condition}${TOOL_RESULT_GETGOAL_SESSION_GOAL_VAR_0.paused===!0?`
It is paused until the user's next message.`:""}${TOOL_RESULT_GETGOAL_SESSION_GOAL_VAR_0.lastReason===void 0?"":`
The evaluator's last reason it isn't met: ${TOOL_RESULT_GETGOAL_SESSION_GOAL_VAR_0.lastReason}`}
