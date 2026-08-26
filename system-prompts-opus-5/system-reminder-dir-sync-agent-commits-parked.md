<!--
name: 'System Reminder: Dir-sync Agent Commits Parked'
description: >-
  Cloud-session notify that the model's commits were taken off the work branch
  and kept at a ref as uncommitted edits.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_2
-->
Your ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.count} commit(s) up to ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.tip)} are no longer on the work branch because ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_2}. They are kept at ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.ref}; their changes are still in the working tree as uncommitted edits (merged with the user's, the user's lines winning). Re-commit or cherry-pick as appropriate.
