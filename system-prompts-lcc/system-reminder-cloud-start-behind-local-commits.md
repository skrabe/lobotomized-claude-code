<!--
name: 'System Reminder: Cloud start behind local commits'
description: >-
  Tells Claude the cloud session started at an older commit and to open its
  first reply with one line saying so
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_0
  - SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_1
  - SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_2
-->
${SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_0} At the start of its first turn the checkout was at commit ${SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_1}, committed ${SYSTEM_REMINDER_CLOUD_START_BEHIND_LOCAL_COMMITS_VAR_2}. Before any tool call, start your first reply with one line that tells the user both. Then carry on with the task. Stop and ask only if the task needs work that isn't here. Leave the line out if you were asked for output in a fixed form, such as JSON only.
