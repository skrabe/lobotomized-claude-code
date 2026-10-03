<!--
name: 'Tool Result: Git bundle settings file names settings path'
description: >-
  Refusal to upload the working tree because a cloud-reachable settings file
  names a variable that decides where the user's own settings are found; remove
  it or set it in the shell
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_SETTINGS_PATH_VAR_0
-->
Not uploading this working tree this way: ${"a settings file a cloud session could reach (this repository’s .claude/settings.json or .claude/settings.local.json, or a --settings file)"} names ${TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_SETTINGS_PATH_VAR_0.name}, which decides where your own settings are found. Remove it there; if you put it there yourself and need it, set it in your shell instead. Then restart Claude Code.
