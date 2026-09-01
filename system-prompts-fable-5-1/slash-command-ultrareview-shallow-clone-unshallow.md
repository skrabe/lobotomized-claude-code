<!--
name: 'Slash Command: Ultrareview Shallow Clone (Unshallow Hint)'
description: >-
  Precondition error for a shallow clone with no explicit base arg; emitted by
  the /code-review ultra command as <local-command-stdout> and replayed to the
  model.
ccVersion: 2.1.214
variables:
  - SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_1
-->
Your clone is shallow and doesn't contain the point where your branch forked from ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_0}. Run \`git fetch --unshallow origin\` and rerun ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_1}. If your base branch isn't ${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_0}, pass it explicitly (\`${SLASH_COMMAND_ULTRAREVIEW_SHALLOW_CLONE_UNSHALLOW_VAR_1} <branch>\`).
