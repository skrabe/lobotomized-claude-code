<!--
name: 'Tool Result: Cloud session — remote on another forge, upload without file sync'
description: >-
  Cloud-session start refusal saying the project's remote is on a forge that
  cloud sessions cannot clone from, and how to upload without file sync instead.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_2
-->
This project directory's remote is on ${TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_0.forge}, which cloud sessions can't clone from yet. To upload ${TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_1} without file sync instead (${TOOL_RESULT_CLOUD_SESSION_OTHER_FORGE_UPLOAD_WITHOUT_FILE_SYNC_VAR_2}), run CLAUDE_CODE_DIR_SYNC_ENGINE=none claude --cloud.
