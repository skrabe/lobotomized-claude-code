<!--
name: 'Data: Import MCP Env Var Not Copied Suffix'
description: >-
  Suffix on /import MCP apply results listing env vars the user must set because
  literal values were not copied.
ccVersion: 2.1.265
variables:
  - DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_0
  - DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_1
  - DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_2
-->
 — set ${DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_0(DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_1.length,"env var")} ${DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_1.join(", ")} (literal ${DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_0(DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_1.length,"value")} in ${DATA_IMPORT_MCP_ENV_VAR_NOT_COPIED_SUFFIX_VAR_2} not copied)
