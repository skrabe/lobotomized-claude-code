<!--
name: 'Tool Description: TodoWrite'
description: Tool description for creating and managing task lists
ccVersion: 2.1.84
variables:
  - EDIT_TOOL_NAME
-->
Create and manage a task list for the current coding session. Helps track progress on multi-step work and shows the user where you are.

## When to use
- Work has 3+ distinct steps
- Multi-operation tasks that need planning
- User explicitly asks for a todo list
- User gives a comma-separated list of tasks
- You start working on a new task (mark in_progress BEFORE beginning)
- You finish a task (mark completed IMMEDIATELY — don't batch)

## When not to use
- Single, trivial tasks
- Pure Q&A or informational requests
- Tasks completable in under 3 trivial steps

For a single trivial task, just do it — tracking adds no value.

## Task fields
- \`content\`: imperative form — "Fix authentication bug"
- \`activeForm\`: present continuous — "Fixing authentication bug"

## States
- \`pending\`: not started
- \`in_progress\`: working on now — exactly ONE at a time
- \`completed\`: fully done (tests pass, no unresolved errors, implementation complete)

## Keep the list current
- Update status in real-time as you work
- Mark completed immediately after finishing
- Remove tasks that are no longer relevant
- If blocked on a task, keep it in_progress and add a new task describing the blocker
- Don't mark completed if tests fail, implementation is partial, or errors are unresolved

Be proactive but right-sized: track real work, skip trivial work.
