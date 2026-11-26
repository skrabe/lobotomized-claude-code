<!--
name: 'Tool Result: SendUserFile upload limit, no remote open'
description: >-
  Per-file reason that the account's upload allowance is used up and the file
  cannot be opened remotely from its path; advises a scratchpad copy and to keep
  sending other files.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CANNOT_OPEN_REMOTELY_VAR_0
-->
this account has uploaded as many files as it is allowed for now, and this file cannot be opened remotely from its path instead (only files of up to 9.5 MiB in the working directories or the scratchpad can). Put a copy made only to show it in the scratchpad, not in the repository. Sending it again as it is will fail until the allowance resets, but keep sending other files with ${TOOL_RESULT_SENDUSERFILE_UPLOAD_LIMIT_CANNOT_OPEN_REMOTELY_VAR_0}
