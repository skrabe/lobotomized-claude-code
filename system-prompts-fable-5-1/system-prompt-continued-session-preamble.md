<!--
name: Continued Session Compaction Preamble
description: >-
  Model-facing preamble injected at the start of a compacted/continued session
  ("This session is being continued from a previous conversation that ran out of
  context..."); conditional on resuming after auto-compaction.
ccVersion: 2.1.191
variables:
  - SYSTEM_PROMPT_CONTINUED_SESSION_PREAMBLE_VAR_0
  - SYSTEM_PROMPT_CONTINUED_SESSION_PREAMBLE_VAR_1
-->
This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

${SYSTEM_PROMPT_CONTINUED_SESSION_PREAMBLE_VAR_0(SYSTEM_PROMPT_CONTINUED_SESSION_PREAMBLE_VAR_1)}
