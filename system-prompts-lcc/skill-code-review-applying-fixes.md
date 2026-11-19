<!--
name: 'Skill: Code Review (--fix applying fixes)'
description: >-
  Appended to the code-review prompt when --fix is passed; instructs applying
  each finding to the working tree, skipping behavior-changing or out-of-scope
  fixes
ccVersion: 2.1.328
variables:
  - IS_BUGS_ONLY_REVIEW
  - FIX_REPORT_CLOSING_INSTRUCTION
-->


## Applying fixes (--fix)

The \`--fix\` flag was passed. After producing the findings list, apply the
findings to the working tree instead of stopping at the report: fix each one
directly${IS_BUGS_ONLY_REVIEW?", whatever its kind or severity":" — correctness bugs and reuse/simplification/efficiency cleanups alike"}.
Skip any finding whose fix would change intended behavior, require changes well
outside the reviewed diff, or that you judge to be a false positive — note the
skip rather than arguing with it. ${FIX_REPORT_CLOSING_INSTRUCTION}
