<!--
name: 'Tool Description: TaskCreate'
description: Tool description for TaskCreate tool
ccVersion: 2.1.328
variables:
  - CONDITIONAL_TEAMMATES_NOTE
  - SUBJECT_FIELD_GUIDANCE
  - DESCRIPTION_FIELD_GUIDANCE
  - ACTIVE_FORM_FIELD_GUIDANCE
  - SUBJECT_WRITING_TIP
  - CONDITIONAL_TASK_NOTES
-->

Create an ID-addressable task graph for shared or multi-agent work with owners and dependencies${CONDITIONAL_TEAMMATES_NOTE}.

Use TaskCreate, TaskGet, TaskList, and TaskUpdate for this shared task graph. Use TodoWrite for a single-agent user-visible checklist. Do not mirror the same work in both systems.

## Task Fields

- **subject**: ${SUBJECT_FIELD_GUIDANCE}
- ${DESCRIPTION_FIELD_GUIDANCE}
- **activeForm** (optional): ${ACTIVE_FORM_FIELD_GUIDANCE}

All tasks are created with status \`pending\`.

${SUBJECT_WRITING_TIP}.
After creating tasks, use TaskUpdate to set dependencies (blocks/blockedBy) if needed.
${CONDITIONAL_TASK_NOTES}Check TaskList first to avoid duplicates.
