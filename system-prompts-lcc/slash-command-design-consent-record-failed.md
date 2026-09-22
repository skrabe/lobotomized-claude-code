<!--
name: 'Slash Command: Design consent record failed'
description: 'Type:text result of /design consent when recording Design agent access throws.'
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_DESIGN_CONSENT_RECORD_FAILED_VAR_0
  - SLASH_COMMAND_DESIGN_CONSENT_RECORD_FAILED_VAR_1
-->
Couldn't record Design agent access for ${"your Claude Design projects"} — ${SLASH_COMMAND_DESIGN_CONSENT_RECORD_FAILED_VAR_0(SLASH_COMMAND_DESIGN_CONSENT_RECORD_FAILED_VAR_1)}. Try again, or run /design-login to authorize Claude Design for this account.
