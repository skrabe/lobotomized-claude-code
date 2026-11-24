<!--
name: 'Tool Result: SendUserFile upload limit card note'
description: >-
  Explains web/desktop still show a card for non-uploaded files and to tell the
  user once.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_0
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_1
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_2
-->

The Claude app on the web and desktop still shows a card for ${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_0(TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_1.length,"it","each")}, which opens the file from this machine while the machine is running. The phone app cannot open ${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_0(TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_1.length,"it","them")}. Tell the user this the first time only, not after each file, and keep sending files with ${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CARD_NOTE_VAR_2}.
