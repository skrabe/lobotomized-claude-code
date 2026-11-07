<!--
name: 'Tool Result: Server classifier no verdict, thread unsupported, retry once'
description: >-
  Tail of the no-verdict denial when the server classifier does not support the
  thread: retry once, then continue and tell the user the tool could not be
  approved
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_THREAD_UNSUPPORTED_RETRY_ONCE_VAR_0
-->
and the next call can be checked: issue it again once. If it is denied again, continue with work that doesn't need it, and tell the user that ${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_THREAD_UNSUPPORTED_RETRY_ONCE_VAR_0.name} could not be approved here.
