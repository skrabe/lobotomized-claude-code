<!--
name: 'Slash Command: Ultrareview PR-Reference Detected'
description: >-
  Precondition error from the /ultrareview | /code-review ultra launcher when
  the argument looks like a PR reference rather than a base ref, telling the
  caller to rerun with the PR number; surfaced to the model as local-command
  output.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_2
-->
Your request mentions what looks like a PR reference (${SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_0}). To review that PR, run \`${SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_1} ${SLASH_COMMAND_ULTRAREVIEW_PR_REFERENCE_DETECTED_VAR_2}\`. To review your current branch instead, rerun without the PR-style reference.
