<!--
name: 'Tool Result: Hooks Worker Reloading Refusal'
description: >-
  Reports that a hook with a catch handler cannot run while its worker is being
  replaced.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_HOOKS_WORKER_RELOADING_REFUSAL_VAR_0
  - TOOL_RESULT_HOOKS_WORKER_RELOADING_REFUSAL_VAR_1
-->
${TOOL_RESULT_HOOKS_WORKER_RELOADING_REFUSAL_VAR_0} refused: the hooks worker is being replaced, and a hook on it with a .catch (${TOOL_RESULT_HOOKS_WORKER_RELOADING_REFUSAL_VAR_1.join(", ")}) cannot be asked until the reload is in
