<!--
name: 'Tool Result: Artifact DB Write Unsupported if_version or replace_all'
description: >-
  Suffix on an artifact_db_write invalid_argument error telling the model the
  server may not accept if_version or replace_all, nothing was written, and to
  retry without that parameter only if an unconditional write is acceptable.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_UNSUPPORTED_IF_VERSION_OR_REPLACE_ALL_VAR_0
-->
. If this server does not yet accept \`${TOOL_RESULT_ARTIFACT_DB_WRITE_UNSUPPORTED_IF_VERSION_OR_REPLACE_ALL_VAR_0!==void 0?"if_version":"replace_all"}\`, that alone explains the refusal — nothing was written; retry without it only if an unconditional ${TOOL_RESULT_ARTIFACT_DB_WRITE_UNSUPPORTED_IF_VERSION_OR_REPLACE_ALL_VAR_0!==void 0?"write":"single replacement"} is acceptable here
