<!--
name: 'Tool Result: Artifact Preview Chrome Writable Path'
description: >-
  checkPermissions deny message when every Chrome candidate sits in a
  session-writable location that commands could have planted.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_0
  - TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_3
  - TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_1
-->
preview will not launch a browser this session's commands could have planted or altered: each one it found sits somewhere they can write without asking (a working directory, a temp dir, a sandbox write root, or a path a Write or Edit allow rule covers) — ${TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_0===void 0?"install Chrome outside those places":TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_3?"install one outside those places with the command below":`install one outside those places (run via Bash, one-time, ~270 MB: ${TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_0})`}, or point BUN_CHROME_PATH at one from your shell. Refused: ${TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_1.join("; ")}${TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_3&&TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_0!==void 0?`
${TOOL_RESULT_ARTIFACT_PREVIEW_CHROME_WRITABLE_PATH_VAR_0}`:""}
