<!--
name: 'Tool result: Send to project threads wait on setup card'
description: Result line giving how many threads wait for the user on the setup card.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_1
-->
${TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_0} ${TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_1(TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_0,"thread")} ${TOOL_RESULT_SEND_TO_PROJECT_THREADS_WAIT_ON_SETUP_CARD_VAR_0===1?"waits":"wait"} for you on the setup card.
