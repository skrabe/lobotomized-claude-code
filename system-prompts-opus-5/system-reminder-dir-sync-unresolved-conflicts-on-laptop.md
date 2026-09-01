<!--
name: Dir Sync Unresolved Conflicts On Laptop
description: >-
  Model reminder that the user's machine has unresolved
  merge/rebase/cherry-pick/revert/stash conflicts whose markers are present in
  this checkout.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_2
-->
Directory sync: the user has unresolved conflicts on their machine (a merge, rebase, cherry-pick, revert or stash pop in progress) — ${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_0} ${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_0===1?"file here holds":"files here hold"} their conflict markers exactly as they stand there${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_1.length===0?"":`: ${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_1.join(", ")}${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_2>0?` and ${SYSTEM_REMINDER_DIR_SYNC_UNRESOLVED_CONFLICTS_ON_LAPTOP_VAR_2} more`:""}`}. They are the user's work in progress and will change when the user resolves them or aborts that operation.
