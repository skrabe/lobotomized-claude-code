<!--
name: 'Data: Cross-session delivery notice (expired)'
description: >-
  Meta prompt injected when outbound cross-session messages expired before the
  recipient user approved them.
ccVersion: 2.1.288
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_2
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_3
-->
[Cross-session delivery notice] ${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_0} ${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_1} not approved before expiry${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_2}. Not delivered to that session's Claude, and nothing is waiting there. Do not wait for a reply, and do not resend unprompted: while the two sessions' permission modes differ a resend is only held again. Tell your user what was not delivered and why; send ${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_3} again, edited if that helps, when they ask.
