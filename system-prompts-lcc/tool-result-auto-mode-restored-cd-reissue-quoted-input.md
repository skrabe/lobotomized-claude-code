<!--
name: 'Auto mode: reissue restored-cd call with quoted input'
description: >-
  Instruction to reissue the call with exactly the quoted input so auto mode
  reviews it.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_AUTO_MODE_RESTORED_CD_REISSUE_QUOTED_INPUT_VAR_0
  - TOOL_RESULT_AUTO_MODE_RESTORED_CD_REISSUE_QUOTED_INPUT_VAR_1
-->
In your next response, issue the ${TOOL_RESULT_AUTO_MODE_RESTORED_CD_REISSUE_QUOTED_INPUT_VAR_0} call once more with exactly this input so auto mode reviews it: ${TOOL_RESULT_AUTO_MODE_RESTORED_CD_REISSUE_QUOTED_INPUT_VAR_1.quote.json}. Put nothing else in that response but other calls whose denial quoted an input like this one.
