<!--
name: 'Tool Result: SendUserFile Placed File Chat Copy Note'
description: >-
  Parenthetical on each placed-in-project-folder line of the SendUserFile result
  saying the folder has the original and the chat shows a jpeg/png copy, as a
  plain file if it is not a picture.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_SENDUSERFILE_PLACED_FILE_CHAT_COPY_NOTE_VAR_0
  - TOOL_RESULT_SENDUSERFILE_PLACED_FILE_CHAT_COPY_NOTE_VAR_1
-->
 (the folder has the original; the chat shows a ${TOOL_RESULT_SENDUSERFILE_PLACED_FILE_CHAT_COPY_NOTE_VAR_0(TOOL_RESULT_SENDUSERFILE_PLACED_FILE_CHAT_COPY_NOTE_VAR_1)} copy of it${TOOL_RESULT_SENDUSERFILE_PLACED_FILE_CHAT_COPY_NOTE_VAR_1.isImage?"":" as a plain file, not a picture"})
