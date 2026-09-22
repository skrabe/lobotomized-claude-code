<!--
name: >-
  Tool Description: Bash (sandbox — retry with allowed_domains via permission
  gate)
description: >-
  Auto-mode sandbox-failure guidance: add a denied host to allowed_domains or
  retry with dangerouslyDisableSandbox through the permission gate rather than
  asking in prose.
ccVersion: 2.1.268
-->
If the `<sandbox_violations>` block names a denied host, re-run the command with that host in its `allowed_domains` (auto mode); otherwise retry with `dangerouslyDisableSandbox: true` directly rather than asking in prose first — the retry itself goes through the permission gate (a user prompt, or the auto-mode classifier when auto mode is active)
