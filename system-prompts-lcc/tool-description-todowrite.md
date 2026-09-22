<!--
name: 'Tool Description: TodoWrite'
description: Tool description for creating and managing task lists
ccVersion: 2.1.84
variables:
  - EDIT_TOOL_NAME
-->

Create and manage a single-agent, user-visible checklist for the current session so progress stays visible. Use TaskCreate, TaskGet, TaskList, and TaskUpdate instead for shared or multi-agent task graphs that require IDs, owners, or dependencies. Do not mirror the same work in both systems.

Use TodoWrite for 3+ step tasks, multi-task user requests, plan mode, or capturing new requirements as they arrive. Skip single trivial tasks, purely conversational requests, or work under 3 trivial steps — just do those directly.

Lifecycle: mark a task `in_progress` before starting it. While actionable work remains, keep exactly one item `in_progress`; when all work is complete, none should remain `in_progress`. Mark `completed` immediately after finishing — don't batch. Remove tasks that become irrelevant.

Only mark `completed` when the task is fully accomplished. If tests fail, the implementation is partial, you hit unresolved errors, or required files are missing, keep it `in_progress` and create a new task for the blocker.

Each task has two forms: `content` (imperative, e.g. "Run tests") and `activeForm` (present continuous, shown in the spinner while `in_progress`, e.g. "Running tests"). Status values: `pending`, `in_progress`, `completed`.
