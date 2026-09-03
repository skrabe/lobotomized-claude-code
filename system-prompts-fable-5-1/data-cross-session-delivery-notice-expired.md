<!--
name: 'Data: Cross-session delivery notice (expired)'
description: >-
  Meta prompt injected when outbound cross-session messages expired before the
  recipient user approved them.
ccVersion: 2.1.224
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_2
-->
[Cross-session delivery notice] ${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_0} ${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_1} not approved before expiry${DATA_CROSS_SESSION_DELIVERY_NOTICE_EXPIRED_VAR_2}. Not delivered to that session's Claude. Do not wait for a reply; continue, or choose another approach.
