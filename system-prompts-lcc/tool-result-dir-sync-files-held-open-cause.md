<!--
name: 'Tool Result: Dir Sync Files Held Open Cause'
description: >-
  Directory-sync note that files this session changed are open in another
  program on the machine, so the changes have not landed there yet.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_0
  - TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_1
  - TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_2
  - TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_3
  - TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_4
-->
${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_0.length===0?"files this session changed":`${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_0.map((TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_1)=>`"${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_1}"`).join(", ")}${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_2>0?` and ${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_2} more`:""}`} ${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_3?"is":"are"} open in another program on ${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_4}, so this session's changes to ${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_3?"it":"them"} are not there yet; they land at the next sync after that program closes ${TOOL_RESULT_DIR_SYNC_FILES_HELD_OPEN_CAUSE_VAR_3?"it":"them"}
