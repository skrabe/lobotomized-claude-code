<!--
name: 'System Reminder: Directory Sync Branch Switch Parked Work'
description: >-
  Explains that a directory-sync checkout followed the user's branch switch
  while preserving the agent's prior work at a separate ref.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0
  - SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_1
  - SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_2
  - SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_3
-->
${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.branch?.SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_1==="user"?"This checkout now holds the user's files as they are.":`The user switched branches${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.toBranch==null?"":` to ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_2(SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.toBranch)}`}; this checkout followed and now holds the user's files as they are.`} Your work from the previous branch — ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.count===0?"your uncommitted edits":`${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.count} commit(s) and any uncommitted edits`} — is kept at ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.ref} and is NOT on this branch or in the working tree: ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.count===0?"":`${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.ref}^1 (= ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_3(SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.tip)}) is your last commit there, and `}${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.ref}'s tree holds your working files, uncommitted edits included. Bring it over only if the user asks (e.g. ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.count===0?"":`git cherry-pick ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_3(SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.tip)}, or `}git checkout ${SYSTEM_REMINDER_DIRECTORY_SYNC_BRANCH_SWITCH_PARKED_WORK_VAR_0.agentCommits.ref} -- PATH).
