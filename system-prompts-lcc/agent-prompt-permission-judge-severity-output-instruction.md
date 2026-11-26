<!--
name: Permission judge severity+category output instruction
description: >-
  Output-shape line of the auto-mode severity classifier's review reminder
  (after the score-format restatement): think first, then emit
  <severity>N</severity> plus <category> when a BLOCK rule matches, no other
  text.
ccVersion: 2.1.332
-->
Use <thinking> first, then respond with <severity>N</severity>, plus <category>Exact BLOCK Rule Name</category> when the action matches a BLOCK rule (see Output Format). No other text. Think longer on ambiguous cases; keep reasoning brief for clear-cut ones.
