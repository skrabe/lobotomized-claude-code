<!--
name: 'Skill: Code Review (Angle C — cross-file tracer)'
description: >-
  The cross-file finder angle of the code-review skill — for each changed
  function, trace its callers to flag broken contracts
ccVersion: 2.1.160
-->
### Angle C — cross-file tracer

For each function the diff changes, find its callers (Grep for the symbol) and
check whether the change breaks any call site: a new precondition, a changed
return shape, a new exception, a timing/ordering dependency. Also check callees:
does a parallel change in the same PR make a call unsafe?
