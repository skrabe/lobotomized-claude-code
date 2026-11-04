<!--
name: 'Poll status: evals pending'
description: >-
  REPL status poll event: no output yet, N evals pending with per-eval state;
  poll again.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_0
  - TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_1
  - TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_2
  - TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_3
-->
no output yet — ${TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_0.length} ${TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_1} pending: ${TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_2.join("; ")}${TOOL_RESULT_POLL_STATUS_EVALS_PENDING_VAR_3}. Poll again to keep waiting.
