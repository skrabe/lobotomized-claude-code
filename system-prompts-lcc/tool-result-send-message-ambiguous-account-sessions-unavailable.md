<!--
name: Send Message Ambiguous Account Sessions Unavailable
description: >-
  Warns that an ambiguous recipient list may omit account sessions whose
  discovery failed.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_ACCOUNT_SESSIONS_UNAVAILABLE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_ACCOUNT_SESSIONS_UNAVAILABLE_VAR_1
-->

Your account's other sessions (Remote Control and cloud) could not be checked just now, so this list may be missing one; if you meant one of them, retry${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_ACCOUNT_SESSIONS_UNAVAILABLE_VAR_0?` (or run ${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_ACCOUNT_SESSIONS_UNAVAILABLE_VAR_1} first)`:""}.
