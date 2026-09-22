<!--
name: 'Tool Result: Git Bundle Index Same Bytes Planted'
description: >-
  Refuses the upload when an index entry appears holding the bytes of a local
  credential-like file this upload did not place.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_2
-->
Not uploading this working tree: while it was read, an index entry appeared (${TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_1)}) holding, byte for byte, the content of a file that stays on this machine (named like credentials or keys${TOOL_RESULT_GIT_BUNDLE_INDEX_SAME_BYTES_PLANTED_VAR_2?", covered by a Read rule or a sandbox read-deny setting of yours, linked from your Claude Code configuration":""}, or kept by a git filter) — at a name no step of this upload put it under, so something else wrote into the index copy this upload works in while it ran. Retry; if it recurs, check what else is running in this checkout.
