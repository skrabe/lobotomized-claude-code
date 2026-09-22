<!--
name: Dir Sync After Command Applied Summary
description: >-
  Applied-pull summary (updated/renamed/removed/not-taken counts) prefixed with
  Directory sync and attached as a session note on the forwarded tool result.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2
-->
${[`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_0===1?"1 file":`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_0} files`} updated here from ${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_1}`,...SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.filesRenamed>0?[`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.filesRenamed===1?"1 file you had edited was":`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.filesRenamed} files you had edited were`} renamed there (your edit is kept under the new name)`]:[],...SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.filesTrashed>0?[`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.filesTrashed} removed`]:[],...SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.notTaken>0?[`${SYSTEM_REMINDER_DIR_SYNC_AFTER_COMMAND_APPLIED_SUMMARY_VAR_2.notTaken} left as they are here (the next turn's report says which and why)`]:[]].join("; ")}.
