<!--
name: 'Tool Result: Steward refused sandbox bypass'
description: >-
  Steward hook refusal of a command that asks to run outside the sandbox,
  suggesting allowed_domains instead
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_STEWARD_REFUSED_SANDBOX_BYPASS_VAR_0
-->
it asks to run outside Claude Code's sandbox, which a watch never does. If the sandbox stood between git and ${TOOL_RESULT_STEWARD_REFUSED_SANDBOX_BYPASS_VAR_0}, run the same git fetch or git push again with allowed_domains: ["${TOOL_RESULT_STEWARD_REFUSED_SANDBOX_BYPASS_VAR_0}"] instead
