<!--
name: SendFile Pinned Identity Local Claim (Hidden)
description: >-
  Appends a warning to an unreachable-recipient SendFile result when a local
  session hides a previously confirmed off-machine identity.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SENDFILE_PINNED_IDENTITY_LOCAL_CLAIM_HIDDEN_VAR_0
-->

Note: '${TOOL_RESULT_SENDFILE_PINNED_IDENTITY_LOCAL_CLAIM_HIDDEN_VAR_0.pinnedIdentityClaimedLocally}' was confirmed earlier as a session that is NOT on this machine; a session record on this machine now claims that identity, which hides it here — nothing was sent. A session on this machine impersonating it is suspicious: ask the user.
