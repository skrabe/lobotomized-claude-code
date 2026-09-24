<!--
name: 'System Reminder: Dir-sync Agent Commits Parked'
description: >-
  Cloud-session notice that the model's commits were taken off the work branch
  and kept at a ref, with their changes left as uncommitted edits. A
  published-commit variant limits re-commits to the model's own unpushed work.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_3
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_4
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_5
-->
${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.reason==="published"?`The ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.count} commit(s) up to ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.tip)} that stood ahead of the user's history here`:`Your ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.count} commit(s) up to ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.tip)}`} are no longer on the work branch because ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_2}. They are kept at ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.ref}; their changes are still in the working tree as uncommitted edits (merged with the user's, the user's lines winning). ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommits.reason==="published"?`Re-commit or cherry-pick only what is your own work among the ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_3} that no remote has (git branch -r --contains COMMIT lists the remote branches holding a commit) — not a merge commit a pull made, nor rebased copies of the user's commits; do not re-commit the ones already on a remote. ${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_4}`:"Re-commit or cherry-pick as appropriate."}${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommitsBookkeeping>0?` (${SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_5(SYSTEM_REMINDER_DIR_SYNC_AGENT_COMMITS_PARKED_VAR_0.agentCommitsBookkeeping)})`:""}
