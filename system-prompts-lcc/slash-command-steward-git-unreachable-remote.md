<!--
name: 'Slash Command: Steward git couldn''t reach remote'
description: 'Steward refusal when git can''t reach the remote, with common causes'
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_2
-->
git couldn't reach ${SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0===void 0?SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1:SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_2(SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0,"/")} (git ls-remote ${SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1}, run by hand, shows why; often a VPN that is off, a sign-in that has expired, or an address that the host sends on to another, as GitLab does with one that lacks .git)
