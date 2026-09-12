<!--
name: 'Data: Goal Check-In Last Turn Ended Early'
description: >-
  Goal-check-in body telling the model the goal is still active after a turn
  ended before the goal could be evaluated.
ccVersion: 2.1.269
variables:
  - DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_0
  - DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_1
  - DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_2
-->
${DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_0(DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_1.condition)} is still active. The last turn ended before the goal could be evaluated: ${DATA_GOAL_CHECKIN_LAST_TURN_ENDED_EARLY_VAR_2.cause}. Continue toward the goal.
