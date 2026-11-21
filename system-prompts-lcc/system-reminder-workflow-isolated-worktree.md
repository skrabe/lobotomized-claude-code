<!--
name: 'System Reminder: Workflow isolated worktree'
description: >-
  Tells a workflow subagent it is running in an isolated git worktree separate
  from the main working directory
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_2
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_3
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_4
  - SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_5
-->
${SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_0}

---
You are running in an isolated ${SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_1.copy.madeBy==="mod"||(await SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_2(SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_1.worktreePath))?.SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_3?"":"git "}worktree at \`${SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_4(SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_1.worktreePath)}\` (a separate working copy of the ${SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_1.copy.madeBy==="mod"?"project":"repo"}). Changes here do not affect the main working directory (\`${SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_4(SYSTEM_REMINDER_WORKFLOW_ISOLATED_WORKTREE_VAR_5())}\`) or other agents. The worktree is cleaned up automatically if you made no changes, or preserved for review if you did.
