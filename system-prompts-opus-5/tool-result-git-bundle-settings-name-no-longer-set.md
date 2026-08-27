<!--
name: 'Tool Result: Git Bundle Settings Name No Longer Set'
description: >-
  Hardened git-bundle refusal when a settings-steered name was set by a
  cloud-reachable settings file that no longer names it.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_GIT_BUNDLE_SETTINGS_NAME_NO_LONGER_SET_VAR_0
-->
Not uploading this working tree this way: ${TOOL_RESULT_GIT_BUNDLE_SETTINGS_NAME_NO_LONGER_SET_VAR_0.name} was set by ${"a settings file a cloud session could reach (this repository’s .claude/settings.json or .claude/settings.local.json, or a --settings file)"} that no longer names it, and the upload's own git runs would still have to trust it. Keep it out of those files and restart Claude Code.
