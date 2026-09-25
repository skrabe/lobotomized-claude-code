<!--
name: 'Tool Result: Cloud session folder seed switched off after sync choice'
description: >-
  Cloud-session creation failure when the user chose to sync the folder but
  starting sessions from local files is switched off, with how to start without
  the folder's files or undo the choice
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_CLOUD_SESSION_FOLDER_SEED_BUNDLE_SEED_SWITCHED_OFF_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_FOLDER_SEED_BUNDLE_SEED_SWITCHED_OFF_VAR_1
-->
Cannot start a cloud session from this folder right now: you chose to sync this folder, and starting sessions from local files is switched off. Try again later, or run CLAUDE_CODE_DIR_SYNC_ENGINE=none claude --cloud to start without this folder’s files. To undo the choice, delete "remoteFileMode" from this folder’s entry under "projects" in ${TOOL_RESULT_CLOUD_SESSION_FOLDER_SEED_BUNDLE_SEED_SWITCHED_OFF_VAR_0(TOOL_RESULT_CLOUD_SESSION_FOLDER_SEED_BUNDLE_SEED_SWITCHED_OFF_VAR_1())}; a launch that can sync asks again.
