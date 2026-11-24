<!--
name: 'System reminder: tool hosts correction background task stopped'
description: >-
  Tool-hosts correction saying the remote machine started an unfollowed
  background task that this session asked to stop and that may have done part of
  its work.
ccVersion: 2.1.331
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_2
-->
${SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_0} That machine now reports that it started a background task there, which this session is not following: its result won't arrive here. This session has asked for it to be stopped. It may have done part of its work. ${SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_1(SYSTEM_REMINDER_TOOL_HOSTS_CORRECTION_BACKGROUND_TASK_STOPPED_VAR_2)}
