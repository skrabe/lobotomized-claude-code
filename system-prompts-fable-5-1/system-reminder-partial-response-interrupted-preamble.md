<!--
name: Partial-response continuation preamble
description: >-
  Injected as meta message content when an interrupted/refused response is
  salvaged; frames the quoted partial text for the model to continue from.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_PARTIAL_RESPONSE_INTERRUPTED_PREAMBLE_VAR_0
-->
The previous attempt at this response was interrupted before it could complete. The text it had produced so far is quoted below${SYSTEM_REMINDER_PARTIAL_RESPONSE_INTERRUPTED_PREAMBLE_VAR_0?" (earlier part omitted)":""}:
