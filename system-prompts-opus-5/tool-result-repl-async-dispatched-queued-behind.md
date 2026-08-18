<!--
name: Async REPL dispatched — queued behind
description: >-
  REPL tool result for an async dispatch that is queued behind other evals,
  telling Claude its outcome arrives later as a repl-eval poll event and not to
  re-issue the code.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_REPL_ASYNC_DISPATCHED_QUEUED_BEHIND_VAR_0
  - TOOL_RESULT_REPL_ASYNC_DISPATCHED_QUEUED_BEHIND_VAR_1
-->
(dispatched #${TOOL_RESULT_REPL_ASYNC_DISPATCHED_QUEUED_BEHIND_VAR_0}, queued behind ${TOOL_RESULT_REPL_ASYNC_DISPATCHED_QUEUED_BEHIND_VAR_1} — the script is queued, not run; its outcome arrives later as an <event kind="repl-eval"> poll event. Do not re-issue this code.)
