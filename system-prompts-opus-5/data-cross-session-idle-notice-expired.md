<!--
name: 'Data: Cross-Session Idle Notice Expired'
description: >-
  Model-injected notice that the idle subscription expired with no signal from
  the peer.
ccVersion: 2.1.237
variables:
  - DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_0
  - DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_1
  - DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_2
-->
[Cross-session idle notice] No idle signal arrived from "${DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_0.label}" within ${DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_1/3600000} hours; the subscription has expired (it may still be busy, be waiting on its user, refuse inbound requests, run a version without idle notices, or have ended abruptly). Do not keep waiting for it; if you still need to know, ask your user or list the sessions to check its status. ${DATA_CROSS_SESSION_IDLE_NOTICE_EXPIRED_VAR_2}
