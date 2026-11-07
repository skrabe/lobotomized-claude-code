<!--
name: 'Tool result: browser_batch refused for page code'
description: >-
  Refusal telling the model a browser_batch was refused because it includes a
  page-code action that cannot combine with an earlier tool; resend the rest
  without it.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_BROWSER_BATCH_REFUSED_PAGE_CODE_VAR_0
  - TOOL_RESULT_BROWSER_BATCH_REFUSED_PAGE_CODE_VAR_1
-->
This browser_batch was refused and none of its actions ran, because it includes ${TOOL_RESULT_BROWSER_BATCH_REFUSED_PAGE_CODE_VAR_0}. ${TOOL_RESULT_BROWSER_BATCH_REFUSED_PAGE_CODE_VAR_1} Send the other actions again without ${TOOL_RESULT_BROWSER_BATCH_REFUSED_PAGE_CODE_VAR_0}. To run code in a page, ask the person to start a new session.
