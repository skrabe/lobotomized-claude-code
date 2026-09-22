<!--
name: 'Tool Description: NotebookEdit'
description: Tool description for editing Jupyter notebook cells
ccVersion: 2.1.162
variables:
  - READ_TOOL_NAME
-->
Replaces, inserts, or deletes a single cell in a Jupyter notebook (.ipynb). You must use the ${READ_TOOL_NAME} tool on the notebook first or this fails. notebook_path must be absolute. cell_id is the id attribute from the ${READ_TOOL_NAME} tool's `<cell id="...">` output, required for replace and delete. edit_mode defaults to replace; insert adds a cell after cell_id (or at the start if omitted, requires cell_type); delete removes the cell.
