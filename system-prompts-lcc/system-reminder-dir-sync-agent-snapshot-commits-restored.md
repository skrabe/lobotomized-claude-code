<!--
name: 'System Reminder: Dir Sync Agent Snapshot Commits Restored'
description: >-
  Cloud-session notice that the work branch had been pointed at directory sync's
  own snapshot commits rather than the agent's work, is back on the user's head
  with the working tree unchanged, and no reset is needed.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_1
-->
The work branch had been pointed at ${SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0.agentCommits.count} of directory sync's own snapshot commits (up to ${SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0.agentCommits.tip)}) rather than work of yours; it is back on ${"to"in SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0.head?`the user's ${SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0.head.to)}`:"the user's head"} now and the working tree is as it was. Nothing of yours was set aside — no reset is needed any more; the file check in that directory-sync notice still applies, against the user's files as last taken in (snapshot in/${SYSTEM_REMINDER_DIR_SYNC_AGENT_SNAPSHOT_COMMITS_RESTORED_VAR_0.generation}).
