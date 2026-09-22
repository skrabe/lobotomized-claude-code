<!--
name: 'Tool Result: Git Bundle Split Index'
description: >-
  d6.shared_index remedy for split-index files, including removing links before
  any git command and running git update-index --no-split-index.
ccVersion: 2.1.280
-->
 Look at the split-index files (sharedindex.*) first (ls -l): where one is a link, remove it before running any git command here — git reads the index through it — then retry. Otherwise `git update-index --no-split-index` makes the index whole (a split index keeps part of itself in those files), after which they can all be deleted; then retry.
