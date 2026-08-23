<!--
name: 'Tool Description: ReadMcpResourceDirTool prompt'
description: >-
  Tool prompt for listing direct children of an MCP directory resource and
  explaining the required server and uri parameters
ccVersion: 2.1.187
variables:
  - DIRECTORY_MIME_TYPE
-->

List the direct children of a directory resource on an MCP server (\`resources/directory/read\`).

Each entry carries its own \`uri\`; subdirectories appear with mimeType "${DIRECTORY_MIME_TYPE}" — call this tool again on a subdirectory's \`uri\` to descend.

Only usable against a server that has declared support for directory listing; other servers return an error.
