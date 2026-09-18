<!--
name: 'Cloud session: project-configured hook not run'
description: >-
  Permission-ask message when a PreToolUse hook not defined in user/managed
  settings is skipped for a cloud-served call.
ccVersion: 2.1.277
-->
A command check that your own settings don't define (this project's, usually) isn't run by this computer for a cloud session, because the session could edit it. Approve this command? (To stop these, review the check and copy it into ~/.claude/settings.json.)
