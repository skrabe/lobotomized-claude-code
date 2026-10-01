<!--
name: 'Tool Result: remote control-request not actioned'
description: >-
  Text explaining that a control-request sent to an attached/remote target was
  not actioned, that resending will not help, and instructing Claude to tell the
  user rather than retry
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_REMOTE_CONTROL_REQUEST_NOT_ACTIONED_RETRY_REFUSED_VAR_0
  - TOOL_RESULT_REMOTE_CONTROL_REQUEST_NOT_ACTIONED_RETRY_REFUSED_VAR_1
-->
${TOOL_RESULT_REMOTE_CONTROL_REQUEST_NOT_ACTIONED_RETRY_REFUSED_VAR_0({status:n,payloadType:"control_request",subtype:t})} Nothing was done for it on ${TOOL_RESULT_REMOTE_CONTROL_REQUEST_NOT_ACTIONED_RETRY_REFUSED_VAR_1}. Sending it again will not change that: tell the user instead of retrying.
