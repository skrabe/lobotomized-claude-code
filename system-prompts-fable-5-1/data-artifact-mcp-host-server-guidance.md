<!--
name: 'Data: Artifact MCP host server guidance'
description: >-
  Branch of the Artifact MCP connector guidance telling the model to declare a
  locally-configured MCP server as host:<server> and that only viewers with that
  same local server connected reach it
ccVersion: 2.1.261
variables:
  - DATA_ARTIFACT_MCP_HOST_SERVER_GUIDANCE_VAR_0
-->
 Locally-configured MCP servers connected in this session can also be declared, as host servers: set \`server\` to \`host:<server>\` where \`<server>\` is the segment between \`mcp__\` and the next \`__\` in that server's tool names (\`mcp__filesystem__read_file\` → \`host:filesystem\`). Only servers from the user's MCP configuration count, with one built-in exception: \`host:claude_browser\` is the Claude app's own browser — declare it, with the tools the page needs from \`read_page\`, \`get_page_text\`, \`find\`, \`preview_start\`, \`navigate\`, \`computer\` and \`form_input\`, when the page must read or act on other websites; it answers only when the viewer opens the page in a Cowork session of the desktop app, and the viewer is asked before each website. The app's other built-in servers (\`cowork\`, \`scheduled-tasks\`, \`session_info\`, \`workspace\` and the like) are never host servers, and a page that declares one is refused at publish.${DATA_ARTIFACT_MCP_HOST_SERVER_GUIDANCE_VAR_0>0?" The `mcp__<id>__` connectors above are claude.ai connectors, never host servers.":""} A host server only answers when the viewer opens the page in a Claude app that has that same local server connected — say so to the user when you publish.
