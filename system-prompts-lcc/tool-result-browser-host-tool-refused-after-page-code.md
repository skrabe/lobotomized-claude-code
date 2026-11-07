<!--
name: 'Tool Result: Browser host tool refused after page code'
description: >-
  Error saying a host tool was refused because page code already ran this
  session, warning against private input in those tabs and suggesting a new
  session
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_BROWSER_HOST_TOOL_REFUSED_AFTER_PAGE_CODE_VAR_0
-->
${TOOL_RESULT_BROWSER_HOST_TOOL_REFUSED_AFTER_PAGE_CODE_VAR_0} was refused: this session has already run code in a page, and the two can't be combined in one session. Don't ask the person to send anything private in this chat or type it in this session's tabs instead: code already run in those tabs could capture it. If they want to do it themselves, ask them to open a new tab on their own. To use ${TOOL_RESULT_BROWSER_HOST_TOOL_REFUSED_AFTER_PAGE_CODE_VAR_0}, ask the person to start a new session.
