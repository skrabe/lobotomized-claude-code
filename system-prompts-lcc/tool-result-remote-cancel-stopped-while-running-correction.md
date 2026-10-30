<!--
name: 'Tool Result: Remote cancel stopped while running correction'
description: >-
  Tool result appended to the rejection text when a remote cancel stopped a call
  mid-run, correcting that the call may have partly or fully run and that
  started work may still be running.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_REMOTE_CANCEL_STOPPED_WHILE_RUNNING_CORRECTION_VAR_0
-->
${TOOL_RESULT_REMOTE_CANCEL_STOPPED_WHILE_RUNNING_CORRECTION_VAR_0} Correction to the text above: this call was stopped while running, not refused before it ran. It may have run in part or in full, and its changes may have been written. No permission prompt was involved. Work it started elsewhere (a remote command, a background process) may still be running, so check before starting the same work again. The instruction to stop and wait still stands.
