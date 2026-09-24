<!--
name: 'Tool Result: Working directory missing (session pinned)'
description: >-
  Bash tool error when the pinned working directory no longer exists: shell
  commands cannot run until restored; explains absolute-path file tools still
  work and how to recover.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_CWD_MISSING_SESSION_PINNED_VAR_0
-->
Working directory "${TOOL_RESULT_BASH_CWD_MISSING_SESSION_PINNED_VAR_0}" no longer exists, so shell commands cannot run until it is restored. File tools with absolute paths still work; recreate the directory (writing a file inside it recreates it), or start a new session from an existing directory.
