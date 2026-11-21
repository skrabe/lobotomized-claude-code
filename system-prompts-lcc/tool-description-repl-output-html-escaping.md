<!--
name: 'Tool Description: REPL output HTML escaping'
description: >-
  Explains that &, < and > are shown HTML-escaped in REPL output while files and
  values are unchanged
ccVersion: 2.1.330
variables:
  - TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_0
  - TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_1
-->
 In ${TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_0?"a call's own result":"what a script returns, logs or throws"}, ${TOOL_DESCRIPTION_REPL_OUTPUT_HTML_ESCAPING_VAR_1()?"some ":""}\`&\`, \`<\` and \`>\` are shown to you as \`&amp;\`, \`&lt;\` and \`&gt;\`. That's only how output is shown: your files and values aren't changed, so write the plain characters in your code.
