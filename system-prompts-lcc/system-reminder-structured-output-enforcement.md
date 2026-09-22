<!--
name: 'System Reminder: Structured Output Call Enforcement'
description: >-
  Stop-hook nudge injected when the model must call the StructuredOutput tool to
  complete the request. Renamed from system-reminder-stop-call-required-tool in
  CC 2.1.187 (subagent variant consolidated in).
ccVersion: 2.1.187
variables:
  - SYSTEM_REMINDER_STRUCTURED_OUTPUT_ENFORCEMENT_VAR_0
  - SYSTEM_REMINDER_STRUCTURED_OUTPUT_ENFORCEMENT_VAR_1
-->
${SYSTEM_REMINDER_STRUCTURED_OUTPUT_ENFORCEMENT_VAR_0} Call the ${SYSTEM_REMINDER_STRUCTURED_OUTPUT_ENFORCEMENT_VAR_1} tool now to complete this request.
