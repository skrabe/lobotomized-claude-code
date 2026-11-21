<!--
name: 'Tool result: git bundle own filter file hint'
description: >-
  Remedy hint when files use a repository filter: inspect config, commit real
  changes, retry; don't remove encryption filters.
ccVersion: 2.1.330
-->
git status and git add run that filter with your access, so if you don't recognize it, look at the repository's git config first. Then run git status, commit the files you really changed (git add <file>, then git commit), and retry. Don't remove a filter that encrypts these files: they would upload unencrypted.
