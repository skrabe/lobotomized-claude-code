<!--
name: 'System Reminder: Peer session mention resolved'
description: >-
  Injected notice that the user @-mentioned a specific Claude session, giving
  the exact name-and-ref token to use with SendMessage and forbidding
  unsolicited sends
ccVersion: 2.1.232
variables:
  - SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_0
  - SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_1
  - SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_2
  - SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_3
-->
The user @-mentioned the Claude session "${SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_0(SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_1.token)}" (${SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_1.where}) as ${SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_0(SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_2.mention)}. If their message asks you to tell or ask that session something, use ${SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_3} with to: "${SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_0(SYSTEM_REMINDER_PEER_SESSION_MENTION_RESOLVED_VAR_1.token)}" — that exact name-and-ref token. Do not message it unless the user's message actually asks you to.
