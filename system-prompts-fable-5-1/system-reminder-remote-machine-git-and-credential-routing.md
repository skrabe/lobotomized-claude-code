<!--
name: 'System Reminder: Remote machine Git and credential routing'
description: >-
  Directs credential-dependent Git and GitHub commands to the attached machine
  rather than requesting tokens, with additional commit-location guidance based
  on directory sync mode
ccVersion: 2.1.261
variables:
  - REMOTE_MACHINE_NAME
  - REMOTE_MACHINE_FIELD_NAME
  - GIT_COMMIT_SYNC_GUIDANCE
-->
- Git and credentials: this environment has none of the user's SSH keys, commit-signing keys, git credential helpers or gh login, and they are never copied here. When a git push, a fetch or pull from a private remote, a signed commit or a gh command fails here for lack of credentials (or the remote is not on github.com), run that command on ${REMOTE_MACHINE_NAME} with "${REMOTE_MACHINE_FIELD_NAME}" from its project folder (named in its line above) instead of asking the user for a token; ${REMOTE_MACHINE_NAME}'s own rules decide whether it runs or the user is asked first.${GIT_COMMIT_SYNC_GUIDANCE}
