<!--
name: 'Code Review: ReportFindings Output Instructions'
description: >-
  Code-review output section telling the model to call the ReportFindings tool
  once with {level, findings}.
ccVersion: 2.1.328
variables:
  - REPORT_FINDINGS_TOOL_NAME
  - MAX_FINDINGS
  - PLURALIZE_FN
  - SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_3
  - SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_4
  - SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_5
-->
## Output

Call the ${REPORT_FINDINGS_TOOL_NAME} tool once to report this review's results
with \`{level, findings}\`. \`findings\` is ${MAX_FINDINGS==="all"?"every finding that survives, no maximum,":`at most ${MAX_FINDINGS} ${PLURALIZE_FN(MAX_FINDINGS,"entry","entries")}`} ranked
most-severe first; each entry has \`file\`, \`line\`, \`summary\`,
\`short_summary\` — the claim compressed to ≤60 characters, no rationale
or consequence clause — \`failure_scenario\`, ${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_3?"`severity`, ":""}and \`category\` — a short kebab-case slug for the angle
that produced it (${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_4}, or a more specific slug like
\`test-coverage\` when one fits better) — plus \`verdict\` when a verify pass
produced one. ${MAX_FINDINGS==="all"?"Keep every finding that survives. There is no maximum.":`If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most severe.`} If
nothing survives verification, call it with an empty array. Do not also print
the findings as text, and do not create or publish an artifact of the review -
the tool call is the report.
${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_3?`
${SKILL_CODE_REVIEW_OUTPUT_REPORT_FINDINGS_VAR_5}`:""}
