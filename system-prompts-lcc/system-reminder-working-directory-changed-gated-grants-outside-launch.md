<!--
name: 'System Reminder: Working directory changed gated grants outside launch'
description: >-
  Notes the new directory's project permission rules are not applied while
  outside the launch directory unless both are trusted explicitly
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_GRANTS_OUTSIDE_LAUNCH_VAR_0
  - SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_GRANTS_OUTSIDE_LAUNCH_VAR_1
-->
Note: ${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_GRANTS_OUTSIDE_LAUNCH_VAR_0} declares project permission rules and/or additional directories in its settings, but they are NOT applied — while the session is outside ${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_GRANTS_OUTSIDE_LAUNCH_VAR_0}, they count only if both it and ${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_GRANTS_OUTSIDE_LAUNCH_VAR_1} have been trusted explicitly. Tool calls those rules would have pre-approved will ask for permission.
