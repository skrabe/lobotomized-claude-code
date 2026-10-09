<!--
name: 'Tool Description: AskUserQuestion (plan mode note)'
description: >-
  Plan mode note appended to the AskUserQuestion tool description when plan mode
  is available: switch modes with the enter tool, ask clarifying questions
  before the plan is final, and never ask whether the plan is ready
ccVersion: 2.1.295
variables:
  - ASKUSERQUESTION_BASE_DESCRIPTION
  - ENTER_PLAN_MODE_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
-->
${ASKUSERQUESTION_BASE_DESCRIPTION}
Plan mode: switch in with ${ENTER_PLAN_MODE_TOOL_NAME}, not this tool. Once in plan mode, use this to clarify requirements or choose between approaches before finalizing your plan. Don't ask "Is the plan ready?" or reference "the plan" — the user can't see it until you call ${EXIT_PLAN_MODE_TOOL_NAME} for approval.
