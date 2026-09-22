<!--
name: Doctor daemon diagnostic section
description: >-
  Daemon-status section assembled into the /doctor diagnostic prompt the model
  reads to explain and fix setup issues.
ccVersion: 2.1.206
variables:
  - SLASH_COMMAND_DOCTOR_DAEMON_SECTION_VAR_0
-->
## Daemon

No daemon lock or status file found — the background daemon does not appear to be running. If the issue involves background sessions or \`claude agents\`, the daemon log (if any) is at \`${SLASH_COMMAND_DOCTOR_DAEMON_SECTION_VAR_0}\`.
