<!--
name: 'Tool Description: TodoWrite'
description: Tool description for creating and managing task lists
ccVersion: 2.1.84
variables:
  - EDIT_TOOL_NAME
-->
Create and manage a structured task list for the current session so progress stays visible. Use it for 3+ step tasks, multi-task user requests, plan mode, or capturing new requirements as they arrive. Skip single trivial tasks, purely conversational requests, or work under 3 trivial steps — just do those directly.

Lifecycle: mark a task \`in_progress\` before starting it, keeping exactly one \`in_progress\` at a time. Mark \`completed\` immediately after finishing — don't batch. Remove tasks that become irrelevant.

Only mark \`completed\` when the task is fully accomplished. If tests fail, the implementation is partial, you hit unresolved errors, or required files are missing, keep it \`in_progress\` and create a new task for the blocker.

Each task has two forms: \`content\` (imperative, e.g. "Run tests") and \`activeForm\` (present continuous, shown in the spinner while \`in_progress\`, e.g. "Running tests"). Status values: \`pending\`, \`in_progress\`, \`completed\`.
