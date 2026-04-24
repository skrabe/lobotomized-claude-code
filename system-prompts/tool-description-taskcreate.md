<!--
name: 'Tool Description: TaskCreate'
description: Tool description for TaskCreate tool
ccVersion: 2.1.84
variables:
  - CONDTIONAL_TEAMMATES_NOTE
  - CONDITIONAL_TASK_NOTES
-->
Use this tool to create a structured task list for your current coding session. Tracks progress and organizes complex work so both you and the user can see where things stand.

## When to Use

Use for work that benefits from explicit tracking:

- Multi-step tasks — 3+ distinct steps or actions${CONDTIONAL_TEAMMATES_NOTE}
- Non-trivial work requiring planning or multiple operations
- Plan mode — create a task list to track the plan
- When the user asks for a todo list or provides multiple tasks
- After receiving new instructions — capture requirements as tasks
- Mark a task in_progress before starting it
- Mark a task completed right after finishing it, and add follow-ups you discover along the way

## When to Skip

- Single straightforward task
- Trivial work where tracking adds no value
- Fewer than 3 trivial steps
- Purely conversational or informational exchanges

## Task Fields

- **subject**: A brief, actionable title in imperative form (e.g., "Fix authentication bug in login flow")
- **description**: What needs to be done
- **activeForm** (optional): Present continuous form shown in the spinner when the task is in_progress (e.g., "Fixing authentication bug"). If omitted, the spinner shows the subject instead.

All tasks are created with status \`pending\`.

## Tips

- Create tasks with clear, specific subjects that describe the outcome
- After creating tasks, use TaskUpdate to set up dependencies (blocks/blockedBy) if needed
${CONDITIONAL_TASK_NOTES}- Check TaskList first to avoid creating duplicate tasks
