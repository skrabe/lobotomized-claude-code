<!--
name: 'Tool Description: Bash (sandbox — retry via permission gate)'
description: >-
  Auto-mode sandbox-failure guidance to retry with dangerouslyDisableSandbox
  through the permission gate when no denied host is named.
ccVersion: 2.1.268
-->
Retry with `dangerouslyDisableSandbox: true` directly rather than asking in prose first — the retry itself goes through the permission gate (a user prompt, or the auto-mode classifier when auto mode is active)
