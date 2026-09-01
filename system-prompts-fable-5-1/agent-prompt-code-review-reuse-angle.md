<!--
name: Code-review reuse angle
description: >-
  Reuse finder-angle instruction injected into the workflow code-review agent's
  prompt.
ccVersion: 2.1.206
-->
Flag new code that re-implements something the codebase
already has — Grep shared/utility modules and files adjacent to the change,
and name the existing helper to call instead.
