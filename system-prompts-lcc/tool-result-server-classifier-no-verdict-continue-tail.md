<!--
name: 'Tool Result: Server classifier no verdict continue tail'
description: >-
  Tail of the no-verdict denial that says whether retrying can help, then tells
  the model to continue with other work and tell the user the tool could not be
  approved
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_0
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_1
  - TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_2
-->
${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_0.errorKind===TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_1?"but retrying it now won't get a verdict.":"and a later call may get a verdict. Don't retry it now."} Continue with work that doesn't need it, and tell the user that ${TOOL_RESULT_SERVER_CLASSIFIER_NO_VERDICT_CONTINUE_TAIL_VAR_2.name} could not be approved here.
