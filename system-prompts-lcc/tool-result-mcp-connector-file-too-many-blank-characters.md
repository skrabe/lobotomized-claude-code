<!--
name: 'Tool Result: MCP connector path has too many blank characters'
description: >-
  Refuses a file whose path has too many invisible or blank characters for the
  credential-name check and explains renaming
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_2
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_0}: the file's path, or the path it lies at, holds more than ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_1} blank or invisible characters in all, not counting ordinary spaces (no-break spaces, for example; the quoted path writes each as a code like \\u00a0). Tell the user it was not sent, and that it can be sent once the file, and any folder in its path that has such characters, is renamed without them; an ordinary space can take the place of each. Before it sends a file Claude Code checks its path for a credential file's name in disguise, and it cannot finish that check for a path with this many such characters; that is a limit of the check and says nothing about this file. ${TOOL_RESULT_MCP_CONNECTOR_FILE_TOO_MANY_BLANK_CHARACTERS_VAR_2}
