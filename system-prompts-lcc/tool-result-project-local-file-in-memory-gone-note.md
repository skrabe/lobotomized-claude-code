<!--
name: 'Tool Result: Project local_file in memory note'
description: >-
  Project read/memory-read notice that local_file lives in memory and disappears
  when the sandbox stops, telling Claude to call the named tool again to get it
  back.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PROJECT_LOCAL_FILE_IN_MEMORY_GONE_NOTE_VAR_0
-->
local_file is in memory and is gone once this session's sandbox stops. To get it again, call ${TOOL_RESULT_PROJECT_LOCAL_FILE_IN_MEMORY_GONE_NOTE_VAR_0} again.
