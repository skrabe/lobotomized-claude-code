<!--
name: 'Tool Description: NotebookEdit'
description: Tool description for editing Jupyter notebook cells
ccVersion: 2.1.162
variables:
  - READ_TOOL_NAME
-->

Replaces, inserts, or deletes a single cell in a Jupyter notebook (.ipynb). You must use the ${READ_TOOL_NAME} tool on the notebook first or this fails. notebook_path must be absolute. cell_id is the id attribute from the ${READ_TOOL_NAME} tool's `<cell id="...">` output, required for replace and delete. edit_mode defaults to replace. Insert adds a cell after cell_id, or at the start when cell_id is omitted; every insert requires cell_type. Delete removes the cell.
