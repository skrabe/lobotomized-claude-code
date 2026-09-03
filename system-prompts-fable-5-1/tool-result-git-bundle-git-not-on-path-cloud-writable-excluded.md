<!--
name: 'Tool Result: Git Bundle Git Not On Path Cloud Writable Excluded'
description: >-
  Hardened git-bundle refusal when git is missing from PATH after cloud-writable
  directories are left out.
ccVersion: 2.1.247
-->
Not uploading this working tree: git was not found on the PATH this process was started with once the directories a cloud session can write here were left out (those inside this checkout or a checkout enclosing it, such as a worktree’s main checkout; a session temp directory; or one whose git links into them). Install git outside those, or put that directory on PATH, then retry.
