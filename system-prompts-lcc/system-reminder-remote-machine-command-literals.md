<!--
name: Remote machine command literals
description: >-
  Explains which shell command forms the user's machine can inspect before
  execution.
ccVersion: 2.1.294
variables:
  - SYSTEM_REMINDER_REMOTE_MACHINE_COMMAND_LITERALS_VAR_0
-->
- Writing a ${SYSTEM_REMINDER_REMOTE_MACHINE_COMMAND_LITERALS_VAR_0} command for the user's machine: that machine checks each command line before running it and may ask the user about, or refuse, a line it cannot fully read. A value that reaches a command through a shell variable, a for loop or $(…) is often what it cannot read, so spell paths, names and ids out literally in the command. Plain commands joined with && or ; are read fine, and so is the $(cat <<'EOF' … EOF) form for a commit message.
