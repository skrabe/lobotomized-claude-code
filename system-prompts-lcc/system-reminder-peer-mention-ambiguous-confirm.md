<!--
name: 'Peer mention — ambiguous, confirm first'
description: >-
  Reminder telling the model an @-mention matched several Claude sessions and it
  must confirm with the user before messaging any of them.
ccVersion: 2.1.232
variables:
  - SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_0
  - SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_1
  - SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_2
  - SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_3
  - SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_4
-->
The user wrote ${SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_0(SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_1.mention)}, which matches ${SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_1.total} Claude sessions:
${SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_2}${SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_3}
Session names are self-chosen and unverified, so confirm with the user which one they mean (describe them by where they run, as listed) before messaging; then use ${SYSTEM_REMINDER_PEER_MENTION_AMBIGUOUS_CONFIRM_VAR_4} with that session's exact "name [ref]" token as to:. Do not guess between them.
