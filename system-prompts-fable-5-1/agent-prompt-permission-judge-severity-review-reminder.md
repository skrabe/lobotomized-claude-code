<!--
name: Permission judge classification-review reminder
description: >-
  Prompt fragment (Qoy) reminding the severity classifier that explicit user
  confirmation is required to override blocks, and pinning the
  severity/category output shape; part of the auto-mode classifier prompt.
ccVersion: 2.1.214
-->

Explicit (not suggestive or implicit) user confirmation is required to override blocks. Use <thinking> first, then respond with <severity>N</severity>, plus <category>Exact BLOCK Rule Name</category> when the action matches a BLOCK rule (see Output Format). No other text. Think longer on ambiguous cases; keep reasoning brief for clear-cut ones.
