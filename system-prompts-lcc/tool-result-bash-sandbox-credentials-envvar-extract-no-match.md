<!--
name: 'Tool Result: Bash sandbox credentials env var extract no match'
description: >-
  Error when a sandbox credentials.envVars entry with onExtractNoMatch "error"
  matched nothing while wrapping a sandboxed command
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_ENVVAR_EXTRACT_NO_MATCH_VAR_0
-->
credentials.envVars entry "${TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_ENVVAR_EXTRACT_NO_MATCH_VAR_0.name}": extract pattern "${TOOL_RESULT_BASH_SANDBOX_CREDENTIALS_ENVVAR_EXTRACT_NO_MATCH_VAR_0.extract}" matched nothing (onExtractNoMatch: "error"). Fix the regex, change to "warn"/"deny", or remove the entry.
