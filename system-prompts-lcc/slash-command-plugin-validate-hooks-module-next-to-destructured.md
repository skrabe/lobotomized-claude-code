<!--
name: 'Slash Command: Plugin Validate Hooks Module Next To Destructured'
description: >-
  Hooks-module scan refusal when next.to is destructured from next instead of
  called as next.to(e, tier).
ccVersion: 2.1.267
-->
next.to is destructured from next; it is reached only as next.to(e, "<tier>") on the hook's own next
