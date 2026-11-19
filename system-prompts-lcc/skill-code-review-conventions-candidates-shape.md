<!--
name: 'Skill: Code review conventions candidates shape'
description: >-
  Code review note that conventions candidates use the file/line/summary shape,
  and correctness outranks them at the cap
ccVersion: 2.1.328
variables:
  - SKILL_CODE_REVIEW_CONVENTIONS_CANDIDATES_SHAPE_VAR_0
-->
Conventions candidates use ${SKILL_CODE_REVIEW_CONVENTIONS_CANDIDATES_SHAPE_VAR_0} \`file\`/\`line\`/\`summary\` shape; in
\`failure_scenario\`, state which CLAUDE.md rule is broken instead of a crash.
Correctness bugs always outrank conventions findings when the output cap
forces a cut.
