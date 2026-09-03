<!--
name: 'Data: Cross-Session Delivery Notice (Refused)'
description: >-
  Meta prompt injected when the recipient session refuses cross-session messages
  so this session must not wait or resend.
ccVersion: 2.1.238
variables:
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_0
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_1
  - DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_2
-->
[Cross-session delivery notice] ${DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_0} ${DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_1} refused${DATA_CROSS_SESSION_DELIVERY_NOTICE_REFUSED_VAR_2}: that session is not accepting cross-session messages (the feature is off there, or a setting or policy there refuses them). Not delivered to that session's Claude. Do not wait for a reply and do not resend; tell the user, or choose another approach.
