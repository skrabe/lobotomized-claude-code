<!--
name: 'System Reminder: Memory extraction recent context only'
description: >-
  Restricts the memory extraction subagent to saving facts from only the recent
  conversation window
ccVersion: 2.1.178
variables:
  - RECENT_MESSAGE_COUNT
-->
Use only the last ~${RECENT_MESSAGE_COUNT} messages to update your persistent memories. Don't spend turns verifying that content — no grepping source files, no reading code, no git commands.
