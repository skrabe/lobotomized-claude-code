<!--
name: 'System Reminder: Steward text holds setting value'
description: >-
  Refuses a comment or commit message holding an exact setting value and asks
  Claude to rewrite it
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_TEXT_HOLDS_SETTING_VALUE_VAR_0
-->
the comment or commit message holds the exact value of ${SYSTEM_REMINDER_STEWARD_TEXT_HOLDS_SETTING_VALUE_VAR_0.name}. It may be a secret, or only a setting such as an address. Write it again without that value, and tell the user which setting it was
