<!--
name: SendMessage Pinned Identity Conflict
description: >-
  SendMessage refusal note warning the model that a local session now claims an
  identity previously confirmed as belonging to another machine.
ccVersion: 2.1.226
variables:
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_2
-->

Note: earlier in this conversation '${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_0.pinnedIdentityClaimedLocally}' was confirmed as a session that is NOT on this machine; a session record on this machine now claims that identity, so nothing was assumed and nothing was sent. ${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_1?`${TOOL_RESULT_SEND_MESSAGE_PINNED_IDENTITY_CONFLICT_VAR_2} will not show the other session while that claim stands. `:""}A same-named session on this machine that your user did not start is suspicious: ask the user before confirming anyone.
