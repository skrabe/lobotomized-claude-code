<!--
name: 'Tool Result: Git Bundle Shallow Link'
description: >-
  Remedy clause when a cloud bundle upload refuses because the shallow file is a
  symlink.
ccVersion: 2.1.280
-->
 Git never makes it a link: if you did not, something else did. Look at it first (ls -l) and remove the link before running any git command here. Then retry.
