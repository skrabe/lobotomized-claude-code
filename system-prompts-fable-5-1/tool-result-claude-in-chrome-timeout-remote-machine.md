<!--
name: 'Tool Result: Claude In Chrome Timeout Remote Machine'
description: >-
  Error tool_result when a Chrome tool times out after a routing ack, suggesting
  the remote computer may be asleep and to try a lighter operation.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_CLAUDE_IN_CHROME_TIMEOUT_REMOTE_MACHINE_VAR_0
-->
${TOOL_RESULT_CLAUDE_IN_CHROME_TIMEOUT_REMOTE_MACHINE_VAR_0} If Chrome is on another computer, that computer may be closed or asleep. The page may also be loading or unresponsive, or Chrome may be waiting for the user. Try a lighter operation (e.g., "get_page_text" instead of a screenshot) once. If that also gets no response, ask the user to check that the computer running Chrome is awake, that Chrome is open, and that nothing in Chrome is waiting for them.
