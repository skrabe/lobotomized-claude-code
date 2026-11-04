<!--
name: 'REPL: Read File Is Notebook'
description: >-
  Error for a REPL text-read helper on a notebook, pointing to the Read tool's
  cells or the raw JSON via cat.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_READ_FILE_IS_NOTEBOOK_VAR_0
  - TOOL_RESULT_REPL_READ_FILE_IS_NOTEBOOK_VAR_1
-->
${TOOL_RESULT_REPL_READ_FILE_IS_NOTEBOOK_VAR_0}: not a text file: ${TOOL_RESULT_REPL_READ_FILE_IS_NOTEBOOK_VAR_1} parses a notebook into its cells. For the cells, (await tools.${TOOL_RESULT_REPL_READ_FILE_IS_NOTEBOOK_VAR_1}({file_path: path})).file.cells; for the raw JSON, await $\`cat \${path}\`.json()
