<!--
name: 'Tool Result: Git bundle settings file names env var'
description: >-
  Refusal to upload the working tree because a cloud-reachable settings file
  sets an environment variable the upload's git would have to trust; remove it
  or move it to user/managed settings or the shell
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_ENV_VAR_0
-->
Not uploading this working tree this way: ${"a settings file a cloud session could reach (this repository’s .claude/settings.json or .claude/settings.local.json, or a --settings file)"} names ${TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_ENV_VAR_0.name}, and the upload's own git runs would have to trust what it names. If you did not put it there yourself, remove it. If you did, move it to your user settings (~/.claude/settings.json), managed settings or your shell (or pass the settings inline). Then restart Claude Code.
