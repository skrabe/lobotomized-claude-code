<!--
name: 'Send Message: Pinned Identity Hidden, Nothing Sent'
description: >-
  Appended to a SendMessage result when the named recipient was earlier
  confirmed to live on another machine and a local session record now claims
  that identity, hiding it; tells the model nothing was sent and the local claim
  is suspicious.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_2
-->

Note: earlier in this conversation '${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_0.pinnedIdentityClaimedLocally}' was confirmed as a session that is NOT on this machine; a session record on this machine now claims that identity, which hides it here — nothing was sent.${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_1?` ${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_HIDDEN_NOTHING_SENT_VAR_2} will not show it while that claim stands.`:""} A session on this machine impersonating it is suspicious: ask the user.
