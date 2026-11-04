<!--
name: 'Tool Result: REPL shell output cut, spill file refused'
description: >-
  Marker that output was cut and the saved file failed the check so was not read
  back
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SHELL_CUT_SPILL_REFUSED_VAR_0
  - TOOL_RESULT_REPL_SHELL_CUT_SPILL_REFUSED_VAR_1
-->
... [output cut at ${TOOL_RESULT_REPL_SHELL_CUT_SPILL_REFUSED_VAR_0.length} chars; the rest was saved to ${TOOL_RESULT_REPL_SHELL_CUT_SPILL_REFUSED_VAR_1??"a file"}, but a check that this is the file the shell tool saved did not pass, so it was not read back]
