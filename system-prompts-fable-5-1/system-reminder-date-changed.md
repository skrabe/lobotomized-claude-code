<!--
name: Date Changed Reminder
description: >-
  Model-facing date_change system-reminder ('The date has changed. Today's date
  is now ${newDate}. DO NOT mention this to the user explicitly...') dispatched
  via _p([On({content,isMeta:!0})]) from the L6l reminder registry.
ccVersion: 2.1.234
variables:
  - SYSTEM_REMINDER_DATE_CHANGED_VAR_0
-->
The date has changed. Today's date is now ${SYSTEM_REMINDER_DATE_CHANGED_VAR_0.newDate}. No need to announce the new date — the user's own clock shows it.
