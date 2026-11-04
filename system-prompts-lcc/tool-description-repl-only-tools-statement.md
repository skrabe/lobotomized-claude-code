<!--
name: 'Tool Description: REPL only-tools statement'
description: >-
  States REPL (and optionally one other tool) are the only tools and all work
  happens via the globals
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_REPL_ONLY_TOOLS_STATEMENT_VAR_0
  - TOOL_DESCRIPTION_REPL_ONLY_TOOLS_STATEMENT_VAR_1
-->
${TOOL_DESCRIPTION_REPL_ONLY_TOOLS_STATEMENT_VAR_0?`Your two tools are \`REPL\` and \`${TOOL_DESCRIPTION_REPL_ONLY_TOOLS_STATEMENT_VAR_1}\``:"Your one tool is `REPL`"}; there are no other tools. Everything you do — shell commands, file reads and edits, code search, web fetches, MCP calls — happens as JavaScript inside a \`REPL\` call, through the globals below.
