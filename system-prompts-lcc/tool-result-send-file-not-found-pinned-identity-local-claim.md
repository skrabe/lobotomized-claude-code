<!--
name: Send File Pinned Identity Hidden By Local Claim
description: >-
  Warns that a pinned remote session is hidden by a conflicting local identity
  claim.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_0
  - TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_1
  - TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_2
-->

Note: '${TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_0.pinnedIdentityClaimedLocally}' was confirmed earlier as a session that is NOT on this machine; a session record on this machine now claims that identity, which hides it here — nothing was sent.${TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_1?` ${TOOL_RESULT_SEND_FILE_NOT_FOUND_PINNED_IDENTITY_LOCAL_CLAIM_VAR_2} will not show it while that claim stands.`:""} A session on this machine impersonating it is suspicious: ask the user.
