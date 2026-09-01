<!--
name: 'Slash Command: Ultrareview Shallow Clone (Deepen Hint)'
description: >-
  Precondition error for a shallow clone with an explicit base arg; emitted by
  the /code-review ultra command as <local-command-stdout> and replayed to the
  model.
ccVersion: 2.1.214
variables:
  - SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_DEEPEN_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_DEEPEN_VAR_1
-->
Your clone is shallow and doesn't contain the point where your branch forked from ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_DEEPEN_VAR_0}. Run \`git fetch --deepen=100 origin ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_DEEPEN_VAR_0}\` (or \`git fetch --unshallow origin\`) and rerun ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_DEEPEN_VAR_1}.
