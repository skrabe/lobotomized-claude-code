<!--
name: SendMessage queued — no inbox bound
description: >-
  SendMessage success-message suffix when no inbox is bound here: the message is
  in the peer inbox unread, the peer may hold or refuse it, and silence is not
  agreement.
ccVersion: 2.1.288
-->
; in that session's inbox, not yet read by its Claude — that session may hold it (usually a different permission mode) or refuse it, and with no inbox bound here nothing reports back, so never treat silence as agreement
