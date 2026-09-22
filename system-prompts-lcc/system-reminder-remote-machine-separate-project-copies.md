<!--
name: 'System Reminder: Remote machine separate project copies'
description: >-
  Tells the session that its own checkout is the primary copy and the folder on
  the user's machine is a separate unsynced copy that may sit at another commit,
  hold uncommitted work, or not even be the same repository, and to state which
  copy any report refers to
ccVersion: 2.1.277
variables:
  - REMOTE_MACHINE_NAME
-->
- The folder on ${REMOTE_MACHINE_NAME} is the user's own separate copy: it may be at a different commit or hold uncommitted work that is not here (it need not even be the same repository — check before assuming it is). When you report what you read or changed, say which copy it was.
