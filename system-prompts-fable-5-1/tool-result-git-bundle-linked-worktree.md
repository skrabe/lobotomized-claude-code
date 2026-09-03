<!--
name: 'Tool Result: Git Bundle Linked Worktree'
description: >-
  Teleport git-bundle refusal when the checkout is a linked worktree, submodule,
  or separate gitdir (.git is a file or link).
ccVersion: 2.1.246
-->
Not uploading this working tree: this checkout is a linked working tree, a submodule or a checkout with a separate git directory (its .git is a file or a link, not a directory), which this upload does not support yet. Start from an ordinary clone of the repository — its main checkout — instead.
