<!--
name: 'Tool Result: Glob Before Dotdot Read Block Ask'
description: >-
  Permission-ask reason when a glob before '..' makes a path uncheckable against
  the outside-working-directory read block or Read deny rules.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_GLOB_BEFORE_DOTDOT_READ_BLOCK_ASK_VAR_0
-->
A glob before the '..' in '${TOOL_RESULT_GLOB_BEFORE_DOTDOT_READ_BLOCK_ASK_VAR_0}' is expanded by the shell before the path is opened, so the target cannot be checked against the read block (permissions.blockReadsOutsideWorkingDirectories) or the Read deny rules. Spell the path without the glob.
