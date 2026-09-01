<!--
name: 'Skill: Code Review (Angle B — removed-behavior auditor)'
description: >-
  The removed-behavior finder angle of the code-review skill — for every
  deleted/replaced line, name the invariant it enforced and check it is
  re-established
ccVersion: 2.1.160
-->
### Angle B — removed-behavior auditor

For every line the diff deletes or replaces, name the invariant or behavior it
enforced, then search the new code for where that invariant is re-established.
If you can't find it, that's a candidate: a removed guard, a dropped error
path, a narrowed validation, a deleted test that was covering a real case.
