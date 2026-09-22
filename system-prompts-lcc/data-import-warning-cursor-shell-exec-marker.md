<!--
name: 'Data: Import Warning Cursor Shell-Exec Marker'
description: >-
  Warning attached to an importable Cursor rule/skill that contains a Claude
  Code shell-exec marker; included on the /import item line sent to the model.
ccVersion: 2.1.265
variables:
  - DATA_IMPORT_WARNING_CURSOR_SHELL_EXEC_MARKER_VAR_0
-->
Line ${DATA_IMPORT_WARNING_CURSOR_SHELL_EXEC_MARKER_VAR_0} has a Claude Code shell-exec marker (\`\`\`! or !\`…\`), inert in Cursor but run when the skill loads; if imported it is written escaped, so nothing runs — review the file.
