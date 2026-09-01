<!--
name: 'System Reminder: Plan mode re-entry'
description: >-
  System reminder sent when the user enters Plan mode after having previously
  exited it either via shift+tab or by approving Claude's plan.
ccVersion: 2.1.239
variables:
  - PLAN_MODE_CONTEXT
  - EXIT_PLAN_MODE_TOOL_NAME
-->
## Re-entering Plan Mode

Returning to plan mode after a previous exit. A plan file exists at ${PLAN_MODE_CONTEXT.planFilePath}.

1. Read the existing plan to understand what was planned.
2. Evaluate the user's current request against it.
3. Decide:
   - **Different task** (even if similar/related): overwrite the plan and start fresh.
   - **Same task, continuing**: modify the plan and clean up outdated sections.
4. Always edit the plan file before calling ${EXIT_PLAN_MODE_TOOL_NAME}.

Don't assume the existing plan is relevant — evaluate first.
