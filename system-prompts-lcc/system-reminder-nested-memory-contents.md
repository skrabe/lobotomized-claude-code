<!--
name: 'System Reminder: Nested memory contents'
description: Contents of a nested memory file
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_NESTED_MEMORY_CONTENTS_VAR_0
-->
Contents of ${SYSTEM_REMINDER_NESTED_MEMORY_CONTENTS_VAR_0.content.path}${SYSTEM_REMINDER_NESTED_MEMORY_CONTENTS_VAR_0.replacesPath===void 0?"":` (in its worktree it replaces ${SYSTEM_REMINDER_NESTED_MEMORY_CONTENTS_VAR_0.replacesPath})`}:

${SYSTEM_REMINDER_NESTED_MEMORY_CONTENTS_VAR_0.content.content}
