<!--
name: 'Tool result: computer use save panel folder not shown'
description: Refusal when the save sheet does not show which folder a save would go to.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_SAVE_PANEL_FOLDER_NOT_SHOWN_VAR_0
-->
${TOOL_RESULT_COMPUTER_USE_SAVE_PANEL_FOLDER_NOT_SHOWN_VAR_0==="click"?"This click":"This"} could confirm a save, and the sheet as it stands does not tell which folder it would go to: in the background that is read from the sheet's file list. If the sheet is compact, click the arrow button beside the folder pop-up to expand it (allowed), then retry. If it is already expanded, it shows an empty folder or search results: call request_full_control and confirm there, or click Cancel (allowed).
