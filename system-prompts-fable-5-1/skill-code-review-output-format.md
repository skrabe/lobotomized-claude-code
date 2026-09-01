<!--
name: 'Skill: Code Review (findings JSON output)'
description: >-
  Shared output spec for the code-review skill — findings as a JSON array with
  file/line/summary/failure_scenario
ccVersion: 2.1.218
variables:
  - MAX_FINDINGS
  - SKILL_CODE_REVIEW_OUTPUT_FORMAT_VAR_1
-->
## Output

Return findings as a JSON array of at most ${MAX_FINDINGS} objects:

\`\`\`json
[
  {
    "file": "path/to/file.ext",
    "line": 123,
    "summary": "one-sentence statement of the bug",
    "failure_scenario": "concrete inputs/state → wrong output/crash"
  }
]
\`\`\`

Ranked most-severe first. If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most
severe. If nothing survives verification, return \`[]\`.
