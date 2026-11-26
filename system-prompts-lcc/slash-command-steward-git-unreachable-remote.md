<!--
name: 'Slash Command: Steward git couldn''t reach remote'
description: 'Steward refusal when git can''t reach the remote, with common causes'
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1
  - SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_2
-->
git couldn't reach ${SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0===void 0?SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1:SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_2(SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_0,"/")} (git ls-remote ${SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1}, run by hand, shows why. Often a VPN is off or a sign-in has expired. If it prints "warning: redirecting to ADDRESS", the host sends your address on to another, as GitLab does with one that lacks .git: run git remote set-url ${SLASH_COMMAND_STEWARD_GIT_UNREACHABLE_REMOTE_VAR_1} ADDRESS)
