<!--
name: 'System Reminder: Dir Sync Rewrite Uncommitted Guidance'
description: >-
  Tells the cloud agent the working tree still holds its rewrite as uncommitted
  changes that will sync back, and to commit as NEW or restore.
ccVersion: 2.1.246
-->
The working tree here still holds your rewrite as uncommitted changes, which go to the user's machine with this turn's result like any other change: commit them as a NEW commit if that was the intent (git revert for an undo), or restore the files
