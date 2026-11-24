<!--
name: 'Slash Command: Steward no saved sign-in'
description: >-
  Reason the host can't be asked: git has no saved sign-in for it, with a GitLab
  path clause
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_HOST_NO_SAVED_SIGN_IN_VAR_0
-->
git has no saved sign-in for it${SLASH_COMMAND_STEWARD_HOST_NO_SAVED_SIGN_IN_VAR_0.kind==="gitlab"?", or keeps it for one path alone (credential.useHttpPath), and such a sign-in isn't sent to the API":""}
