<!--
name: 'Data: Cross-session delivery notice (held)'
description: >-
  Meta prompt injected when outbound cross-session messages are held by the
  recipient session.
ccVersion: 2.1.288
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_2
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_3
-->
[Cross-session delivery notice] ${DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_0} ${DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_1} held by that session${DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_2}. NOT delivered: its Claude has not seen ${DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_3}. Do not report ${DATA_CROSS_SESSION_DELIVERY_NOTICE_HELD_VAR_3} as delivered, do not wait for a reply, and do not resend while held. The usual cause is that the two sessions run in different permission modes: a terminal session then asks its user to approve, but a Claude Desktop or non-interactive session cannot ask, so there the hold expires undelivered unless the modes come to match. A session can also be set to hold every message. Another notice follows on release, denial or expiry. Tell your user what is held and why, or choose another approach.
