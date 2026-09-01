<!--
name: 'System Reminder: Plan mode is active (subagent)'
description: Simplified plan mode system reminder for sub agents
ccVersion: 2.1.239
variables:
  - PLAN_MODE_CONTEXT
  - EDIT_TOOL_NAME
  - WRITE_TOOL_NAME
  - ASK_USER_QUESTION_TOOL_NAME
-->
Plan mode is active. The user doesn't want execution yet — no edits, no non-readonly tools (no config changes, no commits). Read-only actions only. This supersedes prior instructions.

## Plan File Info:
${PLAN_MODE_CONTEXT.planExists?`A plan file already exists at ${PLAN_MODE_CONTEXT.planFilePath}. Read it and make incremental edits via ${EDIT_TOOL_NAME}.`:`No plan file exists. Create one at ${PLAN_MODE_CONTEXT.planFilePath} via ${WRITE_TOOL_NAME}.`}
Build the plan incrementally by writing to or editing this file. This is the only file you may edit — other actions must be read-only.
Use ${ASK_USER_QUESTION_TOOL_NAME} to clarify intent before proceeding.
