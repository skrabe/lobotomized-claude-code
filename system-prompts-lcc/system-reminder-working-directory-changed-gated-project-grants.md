<!--
name: Working-Directory-Changed Notice (Gated Project Grants)
description: >-
  modelMessage note that the new directory's project permission rules and
  additional directories are not applied because the workspace is only trusted
  via a parent grant.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_PROJECT_GRANTS_VAR_0
-->
Note: ${SYSTEM_REMINDER_WORKING_DIRECTORY_CHANGED_GATED_PROJECT_GRANTS_VAR_0} declares project permission rules and/or additional directories in its settings, but they are NOT applied — the workspace is trusted only through a parent directory's grant, and project-scoped grants require trusting this directory explicitly. Tool calls those rules would have pre-approved will ask for permission.
