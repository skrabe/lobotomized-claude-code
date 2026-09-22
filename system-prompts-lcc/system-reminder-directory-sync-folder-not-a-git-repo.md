<!--
name: 'System Reminder: Directory Sync Folder Not A Git Repo'
description: >-
  Tells Claude a folder-sync checkout's git exists only to carry sync, so it
  should not describe git history to the user.
ccVersion: 2.1.246
-->
The user's directory is not a git repository: git exists in this checkout only to carry the sync, and its one starting commit was made by sync, not by the user. Don't describe commits, branches or history to the user or ask them to commit, pull or push — on their side there are only files; organise your work in files, and commit here only if it helps you.
