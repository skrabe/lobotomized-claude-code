<!--
name: 'Tool Result: Git Bundle Commondir Tampered'
description: >-
  Refuses the upload when the commondir file in the checkout's .git directory
  was written by something other than git and points to a directory git would
  not use.
ccVersion: 2.1.285
-->
Not uploading this working tree: the commondir file in this checkout’s .git directory was written by something other than git, and it sends git to a directory where git itself would not keep this checkout’s shared files. Look at that file (it names the directory) and delete it, then retry.
