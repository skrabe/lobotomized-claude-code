<!--
name: 'Tool Description: EnterPlanMode'
description: >-
  Tool description for entering plan mode to explore and design implementation
  approaches
ccVersion: 2.1.215
variables:
  - ASK_USER_QUESTION_TOOL_NAME
  - CONDITIONAL_USE_AGENT_TOOL_INSTEAD_NOTE
  - WHAT_HAPPENS_IN_PLAN_MODE_FN
-->
Transition into plan mode to explore the codebase and design an implementation approach for user approval before writing code. Requires user approval to enter.

## When to use

Use for non-trivial implementation tasks — any with architectural or pattern/technology decisions, multiple valid approaches, changes touching more than 2-3 files, behavior-altering modifications, unclear scope needing exploration, or where the implementation could reasonably go several ways. Examples: "add user authentication", "optimize the database queries", "implement dark mode", "update the error handling in the API".

If you'd otherwise use ${ASK_USER_QUESTION_TOOL_NAME} to clarify the approach, use EnterPlanMode instead — explore first, then present options grounded in what's there.

## When not to use

Skip for:
- Single- or few-line fixes (typos, obvious bugs, small tweaks)
- A single function with clear requirements
- Tasks where the user gave specific, detailed instructions
- Pure research/exploration${CONDITIONAL_USE_AGENT_TOOL_INSTEAD_NOTE}

${WHAT_HAPPENS_IN_PLAN_MODE_FN()}
