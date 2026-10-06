<!--
name: 'Tool Result: Git bundle trailing bytes'
description: >-
  Refusal when the bundle does not end with its pack, pointing to a damaged or
  foreign pack file and advising a fresh clone
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_TRAILING_BYTES_VAR_0
-->
Not uploading this working tree: the bundle git just made does not end with its pack (${TOOL_RESULT_GIT_BUNDLE_TRAILING_BYTES_VAR_0}). git does not write that on its own, so a pack file in this repository's .git/objects is most likely damaged or was not written by git. Clone the repository anew, then retry.
