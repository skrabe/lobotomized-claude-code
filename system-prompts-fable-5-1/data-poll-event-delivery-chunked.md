<!--
name: 'Data: Poll event delivery chunked notice'
description: >-
  System-tagged line appended to a poll-event delivery telling the model that
  more queued events follow in the next delivery, oldest first, and that nothing
  was dropped
ccVersion: 2.1.233
variables:
  - DATA_POLL_EVENT_DELIVERY_CHUNKED_VAR_0
-->
<system>delivery chunked: ${DATA_POLL_EVENT_DELIVERY_CHUNKED_VAR_0} more queued event(s) follow in the next delivery, oldest first; nothing was dropped.</system>
