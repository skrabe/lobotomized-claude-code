<!--
name: 'Tool Description: Bash (sandbox — retry with allowed_domains)'
description: >-
  Non-auto sandbox-failure guidance: re-run with the denied host in
  allowed_domains or retry with dangerouslyDisableSandbox without asking.
ccVersion: 2.1.268
-->
If the `<sandbox_violations>` block names a denied host, re-run the command with that host in its `allowed_domains` (auto mode); otherwise retry with `dangerouslyDisableSandbox: true` (don't ask, just do it)
