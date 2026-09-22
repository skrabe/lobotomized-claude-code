<!--
name: 'Tool Result: Git Bundle Worktree Config File Present'
description: >-
  tC.worktree_config clause refusing the upload when the admin entry carries a
  per-worktree config file a session can write.
ccVersion: 2.1.280
-->
its administrative entry carries a per-worktree configuration file, which a session of the repository can write into an entry it makes — remove that file if nothing relies on it, or start from the repository’s main checkout
