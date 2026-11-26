<!--
name: 'Tool result: NotebookEdit cell with attachments'
description: >-
  NotebookEdit refusal when converting a cell with attachments to code, with
  guidance on insert or edit.
ccVersion: 2.1.332
-->
The notebook was not changed: this cell has attachments (such as pasted images), and a code cell cannot hold attachments. To add code after this cell, use edit_mode=insert with cell_type=code and the same cell_id. To edit this cell's text, leave out cell_type and keep any `attachment:` links in new_source. Deleting this cell loses the attachments, so do that only if the user agrees.
