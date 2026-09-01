<!--
name: 'Tool Description: TaskCreate'
description: Tool description for TaskCreate tool
ccVersion: 2.1.84
variables:
  - CONDTIONAL_TEAMMATES_NOTE
  - CONDITIONAL_TASK_NOTES
-->
Create a structured task list for the current coding session so both you and the user can track progress on complex work.

## When to Use

- Multi-step tasks — 3+ distinct steps or actions${CONDTIONAL_TEAMMATES_NOTE}
- Non-trivial work requiring planning or multiple operations
- Plan mode — track the plan as tasks
- When the user asks for a todo list or provides multiple tasks
- After receiving new instructions — capture requirements as tasks
- Mark a task in_progress before starting it; mark it completed right after finishing, adding any follow-ups you discover

## When to Skip

A single straightforward task, trivial work where tracking adds no value, fewer than 3 trivial steps, or purely conversational exchanges — just do it directly.

## Task Fields

- **subject**: brief actionable title in imperative form (e.g. "Fix authentication bug in login flow")
- **description**: what needs to be done
- **activeForm** (optional): present-continuous form shown in the spinner when in_progress (e.g. "Fixing authentication bug"); falls back to subject if omitted

All tasks are created with status \`pending\`.

## Tips

- Use clear, specific subjects describing the outcome
- After creating tasks, use TaskUpdate to set dependencies (blocks/blockedBy) if needed
${CONDITIONAL_TASK_NOTES}- Check TaskList first to avoid duplicates
