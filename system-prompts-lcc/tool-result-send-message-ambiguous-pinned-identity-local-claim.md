<!--
name: Send Message Ambiguous Pinned Identity Local Claim
description: >-
  Warns that a local identity claim conflicts with a recipient previously
  confirmed remote.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_2
-->

Note: earlier in this conversation '${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_0.pinnedIdentityClaimedLocally}' was confirmed as a session that is NOT on this machine; a session record on this machine now claims that identity, so nothing was assumed and nothing was sent. ${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_1?`${TOOL_RESULT_SEND_MESSAGE_AMBIGUOUS_PINNED_IDENTITY_LOCAL_CLAIM_VAR_2} will not show the other session while that claim stands. `:""}A session on this machine claiming that identity, that your user did not set up, is suspicious: ask the user before confirming anyone.
