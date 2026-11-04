<!--
name: 'Tool Result: Tool unavailable, REPL calls await script'
description: >-
  No-such-tool error in REPL mode explaining the dispatch tool is absent, calls
  wait for their script, and every tool call must be awaited.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_0
  - TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_1
-->
. ${TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_0} is not among your tools in this session. Each ${TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_1} call here waits for its script and returns its output; none returns a (dispatched #N) receipt and no ${TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_1} output arrives later. A tool call the script has not awaited when it returns is cancelled and may not finish, so await every tool call. Continue with ${TOOL_RESULT_TOOL_UNAVAILABLE_REPL_DISPATCH_AWAITS_SCRIPT_VAR_1}.
