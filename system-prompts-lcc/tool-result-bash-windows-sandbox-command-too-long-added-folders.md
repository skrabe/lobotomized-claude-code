<!--
name: 'Tool Result: Bash Windows sandbox command too long (added folders)'
description: >-
  Explains that folders added since the sandbox started push a command past the
  Windows command-line limit, and suggests writing long commands to a file or
  running fewer sub-agents
ccVersion: 2.1.317
-->
Command is too long to run in the Windows sandbox. Folders added since the sandbox started, such as worktrees or /add-dir folders, each add file rules that are sent with every command, and those rules plus this command reach the Windows command-line limit. If the command is long, write it to a file and run that file (on PowerShell the script is base64-encoded first, ~2.7x). If it is short, splitting it will not help: the worktree rules of a sub-agent are removed when it finishes, so run fewer sub-agents at once, or restart Claude Code.
