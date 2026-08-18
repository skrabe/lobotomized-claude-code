<!--
name: Async REPL dispatched
description: >-
  REPL tool result for an async dispatch with an empty queue, telling Claude the
  script is queued and its outcome arrives later as a repl-eval poll event.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_REPL_ASYNC_DISPATCHED_VAR_0
-->
(dispatched #${TOOL_RESULT_REPL_ASYNC_DISPATCHED_VAR_0} — the script is queued, not run; its outcome arrives later as an <event kind="repl-eval"> poll event. Do not re-issue this code.)
