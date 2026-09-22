<!--
name: 'Slash Command: Ultrareview Empty Diff Generic Hint'
description: >-
  Remedy clause of the ultrareview empty_diff precondition error when the diff
  against the base is empty for no more specific reason: stage or commit local
  edits, or pass a different base.
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_GENERIC_HINT_VAR_0
-->
If you have local edits, stage or commit them first. If your branch was already merged or you meant a different base, ${SLASH_COMMAND_ULTRAREVIEW_EMPTY_DIFF_GENERIC_HINT_VAR_0}.
