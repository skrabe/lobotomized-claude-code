<!--
name: 'Tool result: git bundle seed ref unwritable'
description: Error when the temporary ref under .git/refs/seed could not be written.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_0
-->
Could not write the temporary ref this upload uses under .git/refs/seed (${TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_0}). If another git process is running here, let it finish, then retry; if it keeps failing, check that this checkout’s git directory is writable and its disk has room.
