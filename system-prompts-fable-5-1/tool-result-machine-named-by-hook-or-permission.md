<!--
name: 'Tool Result: Machine Named By Hook Or Permission Handler'
description: >-
  Refusal returned when a hook or permission handler adds a machine name to a
  tool call; only the model's own input may name a machine.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_MACHINE_NAMED_BY_HOOK_OR_PERMISSION_VAR_0
-->
A hook or permission handler added "${TOOL_RESULT_MACHINE_NAMED_BY_HOOK_OR_PERMISSION_VAR_0}" to this call; only the model's own input can name a machine, so it was not run.
