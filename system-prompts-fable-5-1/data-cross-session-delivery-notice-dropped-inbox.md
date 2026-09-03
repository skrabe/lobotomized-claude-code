<!--
name: 'Data: Cross-Session Delivery Notice (Dropped Inbox)'
description: >-
  Meta prompt telling the model outbound messages were dropped at the recipient
  inbox and must not be retried in a loop.
ccVersion: 2.1.238
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_2
-->
[Cross-session delivery notice] Do not resend now: ${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_0===1?"one of your messages to another session was":`${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_0} of your messages to another session were`} dropped at that session's inbox${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_1} and NOT delivered${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_2?` (${DATA_CROSS_SESSION_DELIVERY_NOTICE_DROPPED_INBOX_VAR_2})`:""}. Treat them as unsent. If the content still matters, fold it into ONE later message after you have finished other work; never retry in a loop.
