<!--
name: Env Context File Truncation Marker
description: >-
  Suffix appended by the shared file reader (vHe) when a project file exceeds
  its char cap; the truncated body is packed by eCr/KSn/Ok into the '###
  CLAUDE.md files and project docs' markdown section handed to the model during
  auto-mode environment setup.
ccVersion: 2.1.221
variables:
  - DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_0
  - DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_1
  - DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_2
-->

${DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_0.slice(0,DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_1)}
…[truncated at ${DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_1} chars of ${DATA_ENV_CONTEXT_FILE_TRUNCATED_CHARS_VAR_2.size} bytes]
