<!--
name: Notebook too large jq hint
description: >-
  Tool_result hint returned to the model on using jq to read portions of an
  oversized .ipynb.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_IPYNB_TOO_LARGE_JQ_HINT_VAR_0
-->
Use ${TOOL_RESULT_IPYNB_TOO_LARGE_JQ_HINT_VAR_0} with jq to read specific portions:
  cat <notebook_path> | jq '.cells[:20]' # First 20 cells
  cat <notebook_path> | jq '.cells[100:120]' # Cells 100-120
  cat <notebook_path> | jq '.cells | length' # Count total cells
  cat <notebook_path> | jq '.cells[] | select(.cell_type=="code") | .source' # All code sources
