<!--
name: 'Tool Result: Bash kept in sandbox by permission check'
description: >-
  Notes that a command ran sandboxed because its permission check relied on the
  sandbox, so sandbox limits may explain a failure and a rerun may stay
  sandboxed
ccVersion: 2.1.328
-->
This command started in the sandbox because its permission check relied on the sandbox, although the settings or this call's input exempt it. Sandbox limits may explain a failure here. Running it again repeats the permission check, which may keep it in the sandbox again.
