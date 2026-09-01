<!--
name: 'Skill: Code Review Findings Prioritization'
description: >-
  Code-review skill prompt fragment on findings shape and that correctness bugs
  outrank cleanup/altitude/conventions when the output cap forces a cut.
ccVersion: 2.1.178
-->
Cleanup, altitude, and conventions candidates use the same
`file`/`line`/`summary` shape; in `failure_scenario`, state the concrete
cost (what is duplicated, wasted, harder to maintain, or which CLAUDE.md rule
is broken) instead of a crash. Correctness bugs always outrank cleanup,
altitude, and conventions findings when the output cap forces a cut.
