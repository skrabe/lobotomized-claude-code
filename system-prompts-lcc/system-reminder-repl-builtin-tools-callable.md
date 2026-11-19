<!--
name: 'System reminder: REPL built-in tools callable'
description: >-
  Note listing built-in tools that a REPL script can call, and how to call them
  and get their schemas.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_REPL_BUILTIN_TOOLS_CALLABLE_VAR_0
-->
These built-in tools can be called from a script too: ${SYSTEM_REMINDER_REPL_BUILTIN_TOOLS_CALLABLE_VAR_0.join(", ")}. Call one as \`tools.<name>(input)\`; \`describeTool(name)\` returns its input schema.
