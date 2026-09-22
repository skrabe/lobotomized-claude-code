<!--
name: 'Inline blob: tool task list'
description: 'TaskList tool description (task management toolset).'
inlineBlobAnchor: "`Use this tool to list all tasks in the task list\\."
inlineBlobKind: 'template'
injectionGate: 'task management toolset loaded'
ccVersion: '2.1.138'
shadows:
  - tool-description-task-list
-->

Use this tool to list all tasks in the task list.

## When to Use This Tool

- To see what tasks are available to work on (status: 'pending', no owner, not blocked)
- To check overall progress on the project
- To find tasks that are blocked and need dependencies resolved
${H}- After completing a task, to check for newly unblocked work or claim the next available task
- **Prefer working on tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones

## Output

Returns a summary of each task:
${_}
- **subject**: Brief description of the task
- **status**: 'pending', 'in_progress', or 'completed'
- **owner**: Agent ID if assigned, empty if available
- **blockedBy**: List of open task IDs that must be resolved first (tasks with blockedBy cannot be claimed until dependencies resolve)

Use TaskGet with a specific task ID to view full details including description and comments.
${q}
