<!--
name: 'Data: REPL tool signature truncated params'
description: >-
  Truncated parameter-object rendering of a REPL-only tool signature, listing
  kept params plus a not-shown count.
ccVersion: 2.1.318
variables:
  - DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_0
  - DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_1
  - DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_2
-->
{${[...DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_0,`…plus ${DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_1.length-DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_0.length} not shown${DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_2>0?`, ${DATA_REPL_TOOL_SIGNATURE_PARAMS_TRUNCATED_VAR_2} of them required`:""}`].join(", ")}}
