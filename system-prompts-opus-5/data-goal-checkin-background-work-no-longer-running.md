<!--
name: Goal check-in — background work no longer running
description: >-
  Goal check-in text injected as a meta user message when the deferred goal
  evaluation resumes because the background work that blocked it has stopped.
ccVersion: 2.1.234
variables:
  - DATA_GOAL_CHECKIN_BACKGROUND_WORK_NO_LONGER_RUNNING_VAR_0
  - DATA_GOAL_CHECKIN_BACKGROUND_WORK_NO_LONGER_RUNNING_VAR_1
-->
Goal check-in: «${DATA_GOAL_CHECKIN_BACKGROUND_WORK_NO_LONGER_RUNNING_VAR_0}» is still active. Its evaluation was deferred for ${DATA_GOAL_CHECKIN_BACKGROUND_WORK_NO_LONGER_RUNNING_VAR_1} min while background work ran, and that work is no longer running (it finished or was stopped without reporting back). Continue toward the goal.
