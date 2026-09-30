<!--
name: Local-command caveat wrapper
description: >-
  Wraps output of !shell-command with anti-confusion framing. Empty .md body =
  no caveat (security-relevant; suppressing means the model may misinterpret
  command output as user input).
ccVersion: 2.1.285
placeholders:
  - tag_name
shadows:
  - system-prompt-local-command-caveat
-->
The command below was run directly in Claude Code, not sent to you as a request, and its output goes straight to the user. It's recorded here as context for later messages.