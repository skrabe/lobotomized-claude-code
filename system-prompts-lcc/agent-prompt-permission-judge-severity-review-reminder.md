<!--
name: Permission judge classification-review reminder
description: >-
  Prompt fragment (Qoy) reminding the severity classifier that explicit user
  confirmation is required to override blocks, and pinning the severity/category
  output shape; part of the auto-mode classifier prompt.
ccVersion: 2.1.214
-->

Explicit (not suggestive or implicit) user confirmation is required to override blocks. Use <thinking> first, then respond with <severity>N</severity>, plus <category>Exact BLOCK Rule Name</category> when the action matches a BLOCK rule (see Output Format). No other text. For ambiguous cases, identify the applicable BLOCK rule and ALLOW exception before scoring; stop once the classification is supported. Keep reasoning brief for clear-cut cases.
