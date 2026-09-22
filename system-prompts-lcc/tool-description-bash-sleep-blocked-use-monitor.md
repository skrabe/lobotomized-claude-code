<!--
name: 'Tool Description: Bash Leading Sleep Blocked'
description: >-
  Bash tool description fragment: leading sleep commands are blocked; poll with
  Monitor until-loop instead.
ccVersion: 2.1.178
-->

Long leading `sleep` commands are blocked. To poll until a condition is met, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). Do not chain shorter sleeps to work around the block.
