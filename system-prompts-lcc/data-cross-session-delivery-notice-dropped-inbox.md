<!--
name: 'Data: Cross-Session Delivery Notice (Dropped Inbox)'
description: >-
  Meta prompt telling the model outbound messages were dropped at the recipient
  inbox and must not be retried in a loop.
ccVersion: 2.1.328
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_2
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_3
-->
${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_0} Do not resend now: ${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_1} dropped at that session's inbox${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_2} and NOT delivered${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_3?` (${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_3})`:""}. Treat them as unsent. If the content still matters, fold it into ONE later message after you have finished other work; never retry in a loop.
