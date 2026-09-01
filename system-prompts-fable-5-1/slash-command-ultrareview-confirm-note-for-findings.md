<!--
name: 'Ultrareview: Confirmation Note For Findings'
description: >-
  Suffix of the ultrareview confirmation scope line that echoes the user's
  review-note argument; reaches the model as /ultrareview local-command output.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_ULTRAREVIEW_CONFIRM_NOTE_FOR_FINDINGS_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_CONFIRM_NOTE_FOR_FINDINGS_VAR_1
-->
 Note for findings (not a base branch): "${SLASH_COMMAND_ULTRAREVIEW_CONFIRM_NOTE_FOR_FINDINGS_VAR_0(SLASH_COMMAND_ULTRAREVIEW_CONFIRM_NOTE_FOR_FINDINGS_VAR_1.scope.instructions)}"
