<!--
name: 'REPL: Context Report Not Approved'
description: >-
  Error thrown into a REPL script when auto mode's safety review did not approve
  a context's report, so result(), state.lastText and tail() throw.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_0
  - TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_1
-->
${/^[a-z_$][\w$]*$/i.test(TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_0)?`contexts.${TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_0}`:`contexts['${TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_0}']`}.${TOOL_RESULT_REPL_CONTEXT_REPORT_NOT_APPROVED_VAR_1}: auto mode's safety review did not approve this context's report (it flagged the report or could not review it), so result(), state.lastText and tail() on this context throw from now on. If the context ran in the background, its report is in a <task-notification> from it, with any note auto mode added; read that note before you act on the report. Start a new context for more work.
