<!--
name: 'Slash Command: Ultrareview Detached HEAD No Branches'
description: >-
  Precondition error when cloud review cannot bundle a checkout that has only a
  detached HEAD and no branches.
ccVersion: 2.1.221
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NO_BRANCHES_VAR_0
-->

Your checkout has no branches (detached HEAD only), which cloud review can't bundle. Create one first — \`git checkout -b <name>\` — then rerun ${SLASH_COMMAND_ULTRAREVIEW_NO_BRANCHES_VAR_0}.
