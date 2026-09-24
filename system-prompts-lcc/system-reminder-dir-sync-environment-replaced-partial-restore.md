<!--
name: 'System Reminder: dir sync environment replaced, partial restore'
description: >-
  Directory-sync notice that the cloud container was recreated and earlier work
  was only partly restored (up to an earlier turn, with the reason), telling the
  model to check files rather than redo work from memory and to tell the user
  what is missing.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_ENVIRONMENT_REPLACED_PARTIAL_RESTORE_VAR_0
-->
Directory sync: this session's cloud environment was REPLACED (the container was recreated) and your earlier work could be RESTORED into this checkout only IN PART — up to the end of an earlier turn; your work after that could not be brought back (${SYSTEM_REMINDER_DIR_SYNC_ENVIRONMENT_REPLACED_PARTIAL_RESTORE_VAR_0[e.why]}) and is NOT here. It comes back only through the user's machine, if it had reached it (its upload for this turn may already have brought it) — check the files before building on them rather than redoing that work from memory, and tell the user plainly which recent changes are missing if they matter now. Not restored either: untracked files sync never carries, installed tools and background processes of the earlier environment.
