<!--
name: 'System Reminder: Dir Sync Rewrite Reparented Guidance'
description: >-
  Tells the cloud agent that rewritten commits were re-created or left as
  uncommitted changes and to make a NEW commit rather than reset/amend/rebase
  user history.
ccVersion: 2.1.246
-->
What your rewrite changed is now either in the re-created commit(s) below (an amended commit) or still in the working tree as uncommitted changes showing as reverted against HEAD (a removed commit's changes); both go to the user's machine with this turn's result like any other change — check git status, then commit as a NEW commit if that was the intent (git revert for an undo), or restore the files
