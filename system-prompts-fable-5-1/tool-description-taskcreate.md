<!--
name: 'Tool Description: TaskCreate'
description: Tool description for TaskCreate tool
ccVersion: 2.1.84
variables:
  - CONDTIONAL_TEAMMATES_NOTE
  - CONDITIONAL_TASK_NOTES
-->

Create an ID-addressable task graph for shared or multi-agent work with owners and dependencies.${CONDTIONAL_TEAMMATES_NOTE}

Use TaskCreate, TaskGet, TaskList, and TaskUpdate for this shared task graph. Use TodoWrite for a single-agent user-visible checklist. Do not mirror the same work in both systems.

## Task Fields

- **subject**: brief actionable title in imperative form (e.g. "Fix authentication bug in login flow")
- **description**: what needs to be done
- **activeForm** (optional): present-continuous form shown in the spinner when in_progress (e.g. "Fixing authentication bug"); falls back to subject if omitted

All tasks are created with status \`pending\`.

After creating tasks, use TaskUpdate to set dependencies (blocks/blockedBy) if needed.
${CONDITIONAL_TASK_NOTES}Check TaskList first to avoid duplicates.
