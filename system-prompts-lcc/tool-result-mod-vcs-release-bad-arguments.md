<!--
name: 'Tool Result: Mod vcs.release bad arguments'
description: >-
  Argument check refusal for $.vcs.release describing the expected { path, name,
  vcs, isDiscard, reason } shape.
ccVersion: 2.1.330
-->
takes { path, name, vcs, isDiscard, reason } (path absolute, isDiscard a boolean, the rest strings)
