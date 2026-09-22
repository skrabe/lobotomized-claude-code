<!--
name: 'Data: Cross-session delivery notice (denied)'
description: >-
  Meta prompt injected into the conversation when the recipient user declined
  one or more of this session's outbound cross-session messages.
ccVersion: 2.1.224
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_2
-->
[Cross-session delivery notice] ${DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_0} ${DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_1} denied by the recipient user${DATA_CROSS_SESSION_DELIVERY_NOTICE_DENIED_VAR_2}. Not delivered to that session's Claude.
