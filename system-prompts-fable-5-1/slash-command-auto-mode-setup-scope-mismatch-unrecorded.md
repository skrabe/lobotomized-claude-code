<!--
name: 'Slash Command: /auto-mode-setup Scope Not Recorded'
description: >-
  Refusal reason returned by /auto-mode-setup --apply-file when the proposal
  predates scope recording, so --apply-target cannot be confirmed; surfaced to
  the model as the command's JSON result.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_UNRECORDED_VAR_0
  - SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_UNRECORDED_VAR_1
-->
This proposal was generated before save scope was recorded, so --apply-target ${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_UNRECORDED_VAR_0.target} can’t confirm it matches. Regenerate the proposal with --propose, answering scope=${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_UNRECORDED_VAR_1}.
