<!--
name: 'Tool Result: Git Bundle Git Dir Unreadable After Capture'
description: >-
  Refuses the upload when the git directory cannot be re-read after the capture,
  so the pack cannot be vouched for.
ccVersion: 2.1.280
-->
Not uploading this working tree: its git directory could not be re-read after the capture ran, so what was packed cannot be vouched for. Inspect the checkout’s .git, then retry.
