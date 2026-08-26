<!--
name: 'Tool Result: Served Write Cloud Unattested Sensitive Path'
description: >-
  Refuses a cloud-served write to a settings/dotfile/unusual path because this
  machine's approvals are not attested.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_SERVED_WRITE_CLOUD_UNATTESTED_SENSITIVE_PATH_VAR_0
-->
${TOOL_RESULT_SERVED_WRITE_CLOUD_UNATTESTED_SENSITIVE_PATH_VAR_0} can't be changed from a cloud session yet: this machine always asks a person before writing a path like this (a settings file, a dotfile, repository internals, or an unusual path shape), and approvals for calls to this machine aren't attested. Ask the user to change it on their machine.
