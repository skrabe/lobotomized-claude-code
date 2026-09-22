<!--
name: 'System Reminder: Directory sync snapshot commit reset'
description: >-
  Warns that the work branch now points at one of directory sync's own
  bookkeeping snapshots rather than real history, explains how to tell whether
  the session caused it, and when to reset the branch versus leave it alone and
  tell the user
ccVersion: 2.1.277
variables:
  - SYNC_SNAPSHOT_COMMIT_MATCH
  - SNAPSHOT_RESET_GUIDANCE
-->
Directory sync: this checkout's HEAD reaches commit ${SYNC_SNAPSHOT_COMMIT_MATCH.found.slice(0,12)}, by the identity it carries one of directory sync's own bookkeeping snapshots — sync keeps them under refs/claude/… (turns/…, in/…, pre/…; a parked/… ref's tip is one too, your own commits sit beneath it) — not work of yours or the user's; a reset, checkout, merge or cherry-pick onto one of those does that, and such commits are never offered to the user's machine as history. If you did not point the branch at one of sync's refs yourself — the commit arrived with history you merged from elsewhere — leave the branch as it is and tell the user; the steps that follow do not apply. ${SNAPSHOT_RESET_GUIDANCE} If the sync notice at your next turn start says the work branch is already back on the user's commit, skip the reset — only the file check still applies. Do not use those snapshots as checkpoints.
