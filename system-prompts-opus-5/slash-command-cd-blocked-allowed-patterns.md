<!--
name: 'Slash Command: /cd — only listed directory patterns allowed'
description: >-
  Tells the model the exact allow-list of directory patterns /cd is restricted
  to, which is the information it needs to pick a legal target on the next
  attempt.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_0
  - SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_1
  - SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_2
  - SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_3
-->
Can't move to ${SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_0(SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_1)} — /cd is limited to directories matching ${SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_2.allowedPatterns.map((SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_3)=>SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_0(SLASH_COMMAND_CD_BLOCKED_ALLOWED_PATTERNS_VAR_3)).join(", ")}. Pick a matching directory, or add a Cd rule in /permissions.
