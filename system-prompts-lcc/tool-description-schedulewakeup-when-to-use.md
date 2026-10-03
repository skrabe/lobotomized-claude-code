<!--
name: 'Tool Description: ScheduleWakeup when to use'
description: >-
  whenToUse text for the ScheduleWakeup tool: schedules when the session resumes
  work, 60–3600 seconds out, used instead of cron to pace an interval-less /loop
ccVersion: 2.1.288
variables:
  - TOOL_DESCRIPTION_SCHEDULEWAKEUP_WHEN_TO_USE_VAR_0
-->
schedules when this session resumes work, 60 to 3600 seconds from now. Use it, not ${TOOL_DESCRIPTION_SCHEDULEWAKEUP_WHEN_TO_USE_VAR_0}, to pace a /loop that has no interval.
