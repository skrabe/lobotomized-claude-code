<!--
name: '/import: MCP server write did not reach config file'
description: >-
  /import MCP item failure when the MCP server was not saved to (or removed
  from) the global config file, suggesting another Claude Code process may hold
  the lock (retry with CLAUDE_CODE_CONFIG_LOCK_WAIT_MS=60000) or the file may be
  read-only or sandboxed.
ccVersion: 2.1.318
variables:
  - SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_0
  - SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_1
  - SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_2
  - SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_3
  - SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_4
-->
MCP server "${SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_0}" ${SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_1}${SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_2(SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_3)}. If other Claude Code processes use that file, they may have kept it locked: ${SLASH_COMMAND_IMPORT_MCP_ADD_WRITE_NOT_SAVED_VAR_4}, with CLAUDE_CODE_CONFIG_LOCK_WAIT_MS=60000 set to wait up to a minute. If that file is read-only or protected by a sandbox, make it writable or run the command outside the sandbox first.
