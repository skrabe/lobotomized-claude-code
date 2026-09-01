<!--
name: 'Skill: Code Review (altitude dimension)'
description: >-
  Code-review dimension: check whether each change is implemented at the right
  depth rather than as a fragile special case
ccVersion: 2.1.178
-->
### Altitude

Check that each change is implemented at the right depth, not as a fragile
bandaid. Special cases layered on shared infrastructure are a sign the fix
isn't deep enough — prefer generalizing the underlying mechanism over adding
special cases.
