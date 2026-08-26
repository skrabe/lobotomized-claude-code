<!--
name: 'Cloud session: project-configured hook not run'
description: >-
  Permission-ask message when a PreToolUse hook not defined in user/managed
  settings is skipped for a cloud-served call.
ccVersion: 2.1.246
-->
A hook that your own user or managed settings do not define as it stands (this project or an agent defines it, or it changed since launch) would normally judge this command — it is not run for a call from a cloud session, which can rewrite this project — approve running the command?
