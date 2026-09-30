<!--
name: 'Tool Result: Git Bundle Git Dir Redirected'
description: >-
  Refuses the upload when git does not use this checkout's own .git directory
  because something in .git, usually HEAD, was emptied or overwritten by
  something other than git.
ccVersion: 2.1.285
-->
Not uploading this working tree: git does not use this checkout’s own .git directory, which happens only when something in .git (usually HEAD) was emptied or overwritten by something other than git. Look at .git and put back what was changed before retrying, or start from an ordinary clone of the repository instead.
