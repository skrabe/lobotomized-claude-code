<!--
name: 'System Reminder: Directory sync turn overcap'
description: >-
  dir_sync_notice telling the model this turn's work exceeded the sync size cap,
  nothing reaches the user until the named blobs are removed, and how to drop
  committed vs uncommitted files.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_2
-->
Directory sync: this turn's work (${SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_0(SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_1)} MiB) is too large to send to the user's machine; the largest files in it: ${SYSTEM_REMINDER_DIR_SYNC_TURN_OVERCAP_VAR_2}. NOTHING from this turn reaches the user until those blobs are out of what is sent. For a file a commit brought in: git rm --cached FILE, add it to .gitignore (or delete it), then git commit --amend (or an interactive rebase if the commit is older) — deleting it in a NEW commit does not help, the blob stays in history. For an uncommitted or staged file: unstage it (git rm --cached) or delete it, and add it to .gitignore.
