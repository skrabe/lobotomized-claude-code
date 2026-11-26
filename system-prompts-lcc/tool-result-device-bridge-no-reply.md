<!--
name: 'Tool result: device bridge no reply'
description: >-
  Desktop-bridge tool error when the device's reply timed out; warns against
  blind retries.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_0
  - TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_1
  - TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_2
-->
Device '${TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_0}' did not respond within ${TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_1.round(TOOL_RESULT_DEVICE_BRIDGE_NO_REPLY_VAR_2/1000)}s.
 This call was sent to the user's computer and only the wait for its reply timed out: the tool may still be running there, may already have finished, or may never have started. Do not run it again unless you know that running it twice is harmless and you have not already retried it; otherwise tell the user it may still finish and ask before running it again.
