<!--
name: 'Tool result: partial delivery stopped'
description: >-
  Rewrites a blocked result to say what was sent, warn against resending, and
  give why it stopped.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_PARTIAL_DELIVERY_STOPPED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_PARTIAL_DELIVERY_STOPPED_VAR_1
-->
${TOOL_RESULT_COMPUTER_USE_PARTIAL_DELIVERY_STOPPED_VAR_0}: those were sent and are not undone, the rest was not sent. The same call again would send them a second time, so take a screenshot first to see what is there. Why it stopped: ${TOOL_RESULT_COMPUTER_USE_PARTIAL_DELIVERY_STOPPED_VAR_1.text}
