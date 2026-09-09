<!--
name: 'Data: Import Warning MCP Literal Credential'
description: >-
  Warning on an importable MCP server whose url or args look like a literal
  credential; interpolated into the /import query prompt as a ⚠-flagged item.
ccVersion: 2.1.265
variables:
  - DATA_IMPORT_WARNING_MCP_LITERAL_CREDENTIAL_VAR_0
-->
Its url or args look like they carry a literal credential, which /import copies as-is into your Claude Code config. Move the value into an environment variable (\`\${env:VAR}\`) in ${DATA_IMPORT_WARNING_MCP_LITERAL_CREDENTIAL_VAR_0} first, or add the server manually with \`claude mcp add\`.
