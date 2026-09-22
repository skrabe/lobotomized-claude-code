<!--
name: 'Tool Description: TaskList'
description: List all tasks in the task list with status and ownership filters
ccVersion: 2.1.141
variables:
  - TOOL_DESCRIPTION_TASK_LIST_VAR_0
  - TOOL_DESCRIPTION_TASK_LIST_VAR_1
  - TOOL_DESCRIPTION_TASK_LIST_VAR_2
-->
Use this tool to list all tasks in the task list.

## When to Use This Tool

- To see what tasks are available to work on (status: 'pending', no owner, not blocked)
- To check overall progress on the project
- To find tasks that are blocked and need dependencies resolved
${TOOL_DESCRIPTION_TASK_LIST_VAR_0}- After completing a task, to check for newly unblocked work or claim the next available task
- **Prefer working on tasks in ID order** (lowest ID first) when multiple tasks are available, as earlier tasks often set up context for later ones

## Output

Returns a summary of each task:
${TOOL_DESCRIPTION_TASK_LIST_VAR_1}
- **subject**: Brief description of the task
- **status**: 'pending', 'in_progress', or 'completed'
- **owner**: Agent ID if assigned, empty if available
- **blockedBy**: List of open task IDs that must be resolved first (tasks with blockedBy cannot be claimed until dependencies resolve)

Use TaskGet with a specific task ID to view full details including description and comments.
${TOOL_DESCRIPTION_TASK_LIST_VAR_2}
