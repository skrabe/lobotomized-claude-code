<!--
name: 'Skill: Code review re-report findings with outcome'
description: >-
  Model-facing code-review skill fragment instructing the model to call
  ReportFindings again with each finding carrying an outcome
  (fixed/no_change_needed/skipped) after applying fixes, and not to repeat the
  findings as text.
ccVersion: 2.1.206
variables:
  - SKILL_CODE_REVIEW_RE_REPORT_FINDINGS_WITH_OUTCOME_VAR_0
-->
call ${SKILL_CODE_REVIEW_RE_REPORT_FINDINGS_WITH_OUTCOME_VAR_0} again with the same findings, each
carrying an \`outcome\`: \`fixed\`, \`no_change_needed\` (the finding was wrong or
already handled), or \`skipped\` (real but not applied). Do not repeat the
findings as text
