<!--
name: 'System Reminder: Directory Sync Branch Switch Parked Work'
description: >-
  Explains that a directory-sync checkout followed the user's branch switch
  while preserving the agent's prior work at a separate ref.
ccVersion: 2.1.247
variables:
  - DIRECTORY_SYNC_RESULT
  - BRANCH_MOVED_BY_FIELD
  - BRANCH_NAME_FORMATTER_FN
  - COMMIT_SHA_FORMATTER_FN
-->
${DIRECTORY_SYNC_RESULT.branch?.BRANCH_MOVED_BY_FIELD==="user"?"This checkout now holds the user's files as they are.":`The user switched branches${DIRECTORY_SYNC_RESULT.agentCommits.toBranch==null?"":` to ${BRANCH_NAME_FORMATTER_FN(DIRECTORY_SYNC_RESULT.agentCommits.toBranch)}`}; this checkout followed and now holds the user's files as they are.`} Your work from the previous branch — ${DIRECTORY_SYNC_RESULT.agentCommits.count===0?"your uncommitted edits":`${DIRECTORY_SYNC_RESULT.agentCommits.count} commit(s) and any uncommitted edits`} — is kept at ${DIRECTORY_SYNC_RESULT.agentCommits.ref} and is NOT on this branch or in the working tree: ${DIRECTORY_SYNC_RESULT.agentCommits.count===0?"":`${DIRECTORY_SYNC_RESULT.agentCommits.ref}^1 (= ${COMMIT_SHA_FORMATTER_FN(DIRECTORY_SYNC_RESULT.agentCommits.tip)}) is your last commit there, and `}${DIRECTORY_SYNC_RESULT.agentCommits.ref}'s tree holds your working files, uncommitted edits included. Bring it over only if the user asks (e.g. ${DIRECTORY_SYNC_RESULT.agentCommits.count===0?"":`git cherry-pick ${COMMIT_SHA_FORMATTER_FN(DIRECTORY_SYNC_RESULT.agentCommits.tip)}, or `}git checkout ${DIRECTORY_SYNC_RESULT.agentCommits.ref} -- PATH).
