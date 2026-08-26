<!--
name: 'System Reminder: Directory Sync Checkout Recreated'
description: >-
  Reminds the model that the cloud checkout was recreated from starting state
  and earlier-turn files are not present yet.
ccVersion: 2.1.246
-->
Directory sync: this checkout was RECREATED from the session's starting state (the cloud container was replaced). Commits and files from earlier turns of this session are NOT here until the user's machine resends its state — tell the user this plainly, do not redo earlier work from memory, and wait for their files to arrive (a later turn) before building on them: what you change here before then is merged under the user's files when they arrive and may be overwritten where they overlap.
