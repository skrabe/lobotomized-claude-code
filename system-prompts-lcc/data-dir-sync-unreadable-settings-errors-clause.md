<!--
name: Dir Sync Unreadable Settings Errors Clause
description: >-
  Parenthetical list of settings files with parse errors, interpolated into
  directory-sync refusals the model reads.
ccVersion: 2.1.261
variables:
  - DATA_DIR_SYNC_UNREADABLE_SETTINGS_ERRORS_CLAUSE_VAR_0
  - DATA_DIR_SYNC_UNREADABLE_SETTINGS_ERRORS_CLAUSE_VAR_1
-->
 (errors in ${DATA_DIR_SYNC_UNREADABLE_SETTINGS_ERRORS_CLAUSE_VAR_0.join(", ")}${DATA_DIR_SYNC_UNREADABLE_SETTINGS_ERRORS_CLAUSE_VAR_1>0?` and ${DATA_DIR_SYNC_UNREADABLE_SETTINGS_ERRORS_CLAUSE_VAR_1} more`:""})
