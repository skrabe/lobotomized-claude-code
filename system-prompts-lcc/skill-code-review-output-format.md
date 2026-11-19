<!--
name: 'Skill: Code Review (findings JSON output)'
description: >-
  Shared output spec for the code-review skill: findings as a JSON array with
  file/line/summary/failure_scenario, optionally with no maximum
ccVersion: 2.1.328
variables:
  - MAX_FINDINGS
  - PLURALIZE_FN
  - SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_2
  - SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_3
  - REPORT_FINDINGS_TOOL_NAME
-->
## Output

Return findings as a JSON array ${MAX_FINDINGS==="all"?"with one object for every finding that survives, no maximum":`of at most ${MAX_FINDINGS} ${PLURALIZE_FN(MAX_FINDINGS,"object")}`}:

\`\`\`json
[
  {
    "file": "path/to/file.ext",
    "line": 123,
    "summary": "${SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_2?"the problem, where it happens and what sets it off. Fix: the change to make":"one-sentence statement of the bug"}",
    "failure_scenario": "concrete inputs/state → wrong output/crash"${SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_2?`,
    "severity": "one of: important, nit, pre_existing"`:""}
  }
]
\`\`\`

${SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_2?`${SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_3}
`:""}Ranked most-severe first. ${MAX_FINDINGS==="all"?"Keep every finding that survives. There is no maximum.":`If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most
severe.`} If nothing survives verification, return \`[]\`. Do not call the
${REPORT_FINDINGS_TOOL_NAME} tool even if it is available - this review's
output contract is the JSON block above.
