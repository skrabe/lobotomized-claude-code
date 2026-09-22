<!--
name: 'Tool Result: Git Bundle Settings Runtime Change'
description: >-
  Git-bundle refusal when an env var that locates settings was changed by a
  settings file after process start.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_GIT_BUNDLE_SETTINGS_RUNTIME_CHANGE_VAR_0
-->
Not uploading this working tree this way: ${TOOL_RESULT_GIT_BUNDLE_SETTINGS_RUNTIME_CHANGE_VAR_0.name} was changed by a settings file after Claude Code started; it decides where your own settings are found, so the upload only trusts the value the process was started with. Set it in the shell rather than in a settings file, then restart Claude Code.
