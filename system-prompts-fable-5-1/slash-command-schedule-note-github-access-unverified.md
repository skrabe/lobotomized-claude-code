<!--
name: 'Schedule note: GitHub access unverified'
description: >-
  Environment/context note injected into the /schedule (routine) prompt when
  GitHub access for a repo couldn't be verified temporarily, suggesting
  installing the Claude GitHub App.
ccVersion: 2.1.210
variables:
  - SLASH_COMMAND_SCHEDULE_NOTE_GITHUB_ACCESS_UNVERIFIED_VAR_0
-->
Couldn't verify GitHub access for ${SLASH_COMMAND_SCHEDULE_NOTE_GITHUB_ACCESS_UNVERIFIED_VAR_0.owner}/${SLASH_COMMAND_SCHEDULE_NOTE_GITHUB_ACCESS_UNVERIFIED_VAR_0.name} (the check failed in a way that may be temporary) — if your routine needs this repo and this persists, install the Claude GitHub App at https://claude.ai/code/onboarding?magic=github-app-setup.
