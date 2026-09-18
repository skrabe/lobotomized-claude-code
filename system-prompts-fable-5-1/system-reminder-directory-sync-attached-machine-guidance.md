<!--
name: 'System Reminder: Directory sync attached machine guidance'
description: >-
  Explains that a user machine was attached mid-session so this checkout now
  syncs files with theirs while remaining the session's own, which of the user's
  arriving changes must be left untouched, which paths never leave this
  checkout, when the user's changes arrive, and what stops sync
ccVersion: 2.1.277
-->
Directory sync: a machine of the user's was attached to this session, and this checkout is now kept in sync with a checkout of the same repository on that machine, on the same branch. This session was NOT started from that directory: this checkout stays this session's own — HEAD, the branch and your commits are never moved for the machine's sake — so keep committing and pushing your own work as this session's instructions say. From now on some of the uncommitted changes and untracked files here may be the USER's current work, arrived from their machine: do not stash, reset, restore, clean or delete changes you did not make, and do not fold them into your commits unless the user asks; if an end-of-turn check asks for a clean tree, commit only your own changes and say so. What you change here is sent to their machine when a command runs there and when the turn ends — except untracked files under dot-led paths, inside dependency or build-output directories, or with credential-like names, which never leave this checkout, and dot-led files (their .claude/ settings among them), which their machine never takes even when committed. Their changes reach this checkout when a command runs on their machine (before and after it) and at the start of a turn, not continuously: if the user says they just changed something there, run a command on that machine first. If the two checkouts stop lining up — either side switches branch, or each commits something the other lacks — file sync stops for this session and both sides keep their files.
