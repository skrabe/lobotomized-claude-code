<!--
name: 'Slash Command: /model — fast mode turned off'
description: >-
  Tells the model fast mode was switched off as a side effect of the model
  change, the sibling state fact to the fast-mode-on notice; now adds a '(/fast
  turns it on)' hint when fast mode is available.
ccVersion: 2.1.322
variables:
  - SLASH_COMMAND_MODEL_FAST_MODE_OFF_SUFFIX_VAR_0
  - SLASH_COMMAND_MODEL_FAST_MODE_OFF_SUFFIX_VAR_1
-->
 · Fast mode OFF${SLASH_COMMAND_MODEL_FAST_MODE_OFF_SUFFIX_VAR_0(SLASH_COMMAND_MODEL_FAST_MODE_OFF_SUFFIX_VAR_1)?" (/fast turns it on)":""}
