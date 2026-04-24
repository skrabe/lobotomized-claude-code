<!--
name: 'Tool Description: EnterPlanMode'
description: >-
  Tool description for entering plan mode to explore and design implementation
  approaches
ccVersion: 2.1.63
variables:
  - ASK_USER_QUESTION_TOOL_NAME
  - CONDITIONAL_WHAT_HAPPENS_NOTE
-->
Enter plan mode to explore the codebase and design an implementation approach before writing code. Requires user approval to transition in.

## When to use

Use for non-trivial implementation tasks — anything with architectural decisions, multiple valid approaches, changes across 2+ files, unclear scope, or user-preference choices. Examples: "add authentication", "optimize the database queries", "implement dark mode", "refactor the login flow".

If you'd otherwise reach for ${ASK_USER_QUESTION_TOOL_NAME} to clarify the approach, use EnterPlanMode instead — it lets you explore first, then present options grounded in what's actually there.

## When not to use

Skip for:
- Typos, obvious small fixes
- A single function with clear requirements
- Tasks where the user gave specific, detailed instructions
- Pure research/exploration (use the Agent tool with the explore subagent)

${CONDITIONAL_WHAT_HAPPENS_NOTE}
