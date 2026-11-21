<!--
name: 'System Reminder: Steward base merge changed control files'
description: >-
  Reports that merging the base changed files that run by themselves or control
  the session
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_0
  - SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_1
  - SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_2
  - SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_3
-->
the merge of ${SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_0.baseRemote}/${SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_0.baseBranch} changed files that run by themselves in this session or control it: ${SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_1.join("; ")}. They are in force now, and stay so unless that merge is undone.${SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_2.ended?"":` The watch goes on. ${SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_3(SYSTEM_REMINDER_STEWARD_BASE_MERGE_CHANGED_CONTROL_FILES_VAR_0)} ends it.`}
