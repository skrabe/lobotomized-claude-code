<!--
name: 'Tool Result: Git Bundle Gitattributes Symlink On Old Git'
description: >-
  Bundle/dir-sync refusal detail when a committed .gitattributes is a symlink
  that old git follows, telling the model to update git and retry.
ccVersion: 2.1.247
-->
a committed .gitattributes is a symbolic link, which the installed git (older than 2.32, or of a version this build cannot read) follows on disk: update git, then retry
