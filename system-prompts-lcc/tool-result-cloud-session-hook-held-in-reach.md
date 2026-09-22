<!--
name: 'Cloud session: in-reach hook not run'
description: >-
  Permission-ask message when a PreToolUse hook whose script lives in the synced
  project is skipped for a cloud-served call.
ccVersion: 2.1.246
-->
A hook whose script lives inside the synced project would normally judge this command — it is not run for a call from a cloud session, which can rewrite that script — approve running the command?
