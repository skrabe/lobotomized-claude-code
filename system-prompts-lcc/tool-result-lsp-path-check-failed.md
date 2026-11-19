<!--
name: 'Tool Result: LSP file path check failed'
description: >-
  LSP validateInput error when the path cannot be checked because of an
  unexaminable folder, ambiguous link target, or too many links
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LSP_PATH_CHECK_FAILED_VAR_0
-->
Cannot check file path: a folder on the way could not be examined, a link on the way has a target the operating system may read differently from the folder Claude Code checked (for example, not valid UTF-8, or on Windows ".." after a folder name), or there are too many links in a row: ${TOOL_RESULT_LSP_PATH_CHECK_FAILED_VAR_0.filePath}
