<!--
name: 'Bash: no output after timeout'
description: >-
  Note when a command killed by timeout (exit 124) returned no output,
  suggesting unbuffered output.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_BASH_NO_OUTPUT_EXIT_124_VAR_0
-->
(${TOOL_RESULT_BASH_NO_OUTPUT_EXIT_124_VAR_0} returned no output. A program that \`timeout\` stops can lose what it has printed but not yet written out. \`python -u\` writes at once.)
