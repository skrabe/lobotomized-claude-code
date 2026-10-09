<!--
name: Start directory gone with fallback
description: >-
  Requests a fresh call after switching from a missing start directory to the
  launch directory.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_0
  - TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_1
  - TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_2
-->
${TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_0} was not run: the directory it was to start in is gone (deleted, moved, replaced by a link, or unreadable). The next call starts in ${TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_1}. Check that this call still does what you mean there, then send it again. What is gone: ${TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_NEXT_DIRECTORY_VAR_2}
