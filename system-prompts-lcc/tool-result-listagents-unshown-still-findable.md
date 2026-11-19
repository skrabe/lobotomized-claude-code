<!--
name: 'Tool Result: ListAgents unshown agents still findable'
description: >-
  Clause telling Claude that SendMessage can still reach unshown agents by name
  or a unique 3+ character prefix
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_0
  - TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_1
  - TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_2
-->
; ${TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_0} still finds ${TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_1===TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_2.length?"all":TOOL_RESULT_LISTAGENTS_UNSHOWN_STILL_FINDABLE_VAR_1} of them by name, or by a unique prefix of 3+ characters
