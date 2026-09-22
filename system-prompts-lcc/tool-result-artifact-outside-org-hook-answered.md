<!--
name: Artifact Outside Org Hook Answered
description: >-
  Outside-org deny fragment when a PermissionRequest hook answered instead of
  the user.
ccVersion: 2.1.274
-->
a PermissionRequest hook answered the permission prompt in the user's place; only the user's own approval allows this read — nothing was returned; do not retry it here, and tell the user their hook answered for them (to approve it themselves they would narrow the hook so it no longer answers this prompt)
