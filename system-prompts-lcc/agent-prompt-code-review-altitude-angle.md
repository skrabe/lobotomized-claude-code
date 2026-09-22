<!--
name: 'Agent Prompt: Code Review Altitude Angle'
description: >-
  Code-review agent angle that requires root-cause fixes at the right depth
  instead of symptom-level special cases.
ccVersion: 2.1.261
-->
### Altitude

Check that each change fixes the root cause at the right depth rather than
patching a symptom with a fragile bandaid. Special cases layered on shared
infrastructure are a sign the fix isn't deep enough — prefer the simpler, more
general change to the underlying mechanism over adding special cases, and name
that change.
