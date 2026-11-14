<!--
name: 'Tool Description: REPL output HTML escaping'
description: >-
  REPL tool description note that &, < and > appear escaped in shown output
  only, so code should use the plain characters.
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_0
-->
 In ${TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_0?"a call's own result":"what a script returns, logs or throws"}, \`&\`, \`<\` and \`>\` are shown to you as \`&amp;\`, \`&lt;\` and \`&gt;\`. That's only how output is shown: your files and values aren't changed, so write the plain characters in your code.
