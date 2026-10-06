<!--
name: 'Tool Result: Bash sandbox credentials file extract no match'
description: >-
  Error when a sandbox credentials.files entry with onExtractNoMatch "error"
  matched nothing while wrapping a sandboxed command
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_FILE_EXTRACT_NO_MATCH_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_FILE_EXTRACT_NO_MATCH_VAR_1
-->
credentials.files entry "${TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_FILE_EXTRACT_NO_MATCH_VAR_0.path}": ${TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_FILE_EXTRACT_NO_MATCH_VAR_1} (onExtractNoMatch: "error"). Fix the config, change to "warn"/"deny", or remove the entry.
