<!--
name: 'System reminder: steward merge shared library refused'
description: >-
  Refusal reason when a base merge brings or changes a shared library loadable
  via LD_LIBRARY_PATH: leave the merge to the user, tell them once, do not retry
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_STEWARD_MERGE_SHARED_LIBRARY_REFUSED_VAR_0
  - SYSTEM_REMINDER_STEWARD_MERGE_SHARED_LIBRARY_REFUSED_VAR_1
-->
this merge brings, changes or removes a shared library (such as a .so file), which the programs that start in this checkout could load through this session's LD_LIBRARY_PATH or a variable like it${SYSTEM_REMINDER_STEWARD_MERGE_SHARED_LIBRARY_REFUSED_VAR_0()==="macos"?" (for libxcrun.dylib that variable is DEVELOPER_DIR)":""}. Leave this merge to the user: tell them so once, and to look at that file before they merge (git diff --name-only HEAD...${SYSTEM_REMINDER_STEWARD_MERGE_SHARED_LIBRARY_REFUSED_VAR_1} lists it), go on with the rest, and don't try it again in this watch
