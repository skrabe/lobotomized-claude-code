<!--
name: 'System reminder: REPL hook messages left out'
description: >-
  hook_additional_context note that repeated or over-limit hook messages from a
  script's tool calls were left out
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_REPL_HOOK_MESSAGES_LEFT_OUT_VAR_0
  - SYSTEM_REMINDER_REPL_HOOK_MESSAGES_LEFT_OUT_VAR_1
-->
Claude Code left out hook messages from this code's tool calls that repeated one already sent, or that went past the limit of ${SYSTEM_REMINDER_REPL_HOOK_MESSAGES_LEFT_OUT_VAR_0} messages or ${SYSTEM_REMINDER_REPL_HOOK_MESSAGES_LEFT_OUT_VAR_1.toLocaleString("en-US")} characters in one run of code. Block reasons and stops are always sent.
