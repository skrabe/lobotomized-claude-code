<!--
name: 'Slash Command: /auto-mode-setup Scope Mismatch'
description: >-
  Refusal reason returned by /auto-mode-setup --apply-file when the proposal's
  saved scope disagrees with --apply-target; surfaced to the model as the
  command's JSON result.
ccVersion: 2.1.218
variables:
  - SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_0
  - SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_1
  - SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_2
-->
This proposal was generated for a different save scope (${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_0.proposal.scope}) than --apply-target ${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_1.target} expects (${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_2}). Regenerate the proposal with --propose, answering scope=${SLASH_COMMAND_AUTO_MODE_SETUP_SCOPE_MISMATCH_VAR_2}.
