<!--
name: 'Code Review: ReportFindings Output Instructions'
description: >-
  Code-review output section telling the model to call the ReportFindings tool
  once with {level, findings}.
ccVersion: 2.1.218
variables:
  - SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_0
  - SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_1
-->
## Output

Call the ${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_0} tool once to report this review's results
with \`{level, findings}\`. \`findings\` is at most ${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_1} entries ranked
most-severe first; each entry has \`file\`, \`line\`, \`summary\`,
\`short_summary\` — the claim compressed to ≤60 characters, no rationale
or consequence clause — \`failure_scenario\`, and \`category\` — a short kebab-case slug for the angle
that produced it (\`correctness\`, \`simplification\`, \`efficiency\`,
\`reuse\`, \`altitude\`, \`conventions\`, or a more specific slug like
\`test-coverage\` when one fits better) — plus \`verdict\` when a verify pass
produced one. If more than ${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_1} survive, keep the ${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_1} most severe. If
nothing survives verification, call it with an empty array. Do not also print
the findings as text, and do not create or publish an artifact of the review -
the tool call is the report.
