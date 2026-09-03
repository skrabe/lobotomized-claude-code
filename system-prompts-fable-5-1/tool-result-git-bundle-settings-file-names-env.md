<!--
name: 'Tool Result: Git Bundle Settings File Names Env'
description: >-
  Git-bundle refusal when a cloud-reachable settings file names an env var that
  the upload's git runs would have to trust.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_ENV_VAR_0
-->
Not uploading this working tree this way: ${"a settings file a cloud session could reach (this repository’s .claude/settings.json or .claude/settings.local.json, or a --settings file)"} names ${TOOL_RESULT_GIT_BUNDLE_SETTINGS_FILE_NAMES_ENV_VAR_0.name}, and the upload's own git runs would have to trust what it names. Set it in your user settings (~/.claude/settings.json), managed settings or the shell instead (or pass the settings inline), then restart Claude Code.
