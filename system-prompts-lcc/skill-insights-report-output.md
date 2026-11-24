<!--
name: 'Skill: /insights report output'
description: >-
  Formats and displays the insights usage report results after the user runs the
  /insights slash command
ccVersion: 2.1.331
variables:
  - SKILL_INSIGHTS_REPORT_OUTPUT_VAR_0
  - SKILL_INSIGHTS_REPORT_OUTPUT_VAR_1
  - REPORT_URL
  - HTML_FILE_PATH
  - FACETS_DIRECTORY
  - SKILL_INSIGHTS_REPORT_OUTPUT_VAR_5
  - SKILL_INSIGHTS_REPORT_OUTPUT_VAR_6
  - LEFT_OUT_LINE
  - RECOMMENDATION_TIP_LINE
-->
The user just ran /insights to generate a usage report analyzing their Claude Code sessions.

Here is the full insights data:
${SKILL_INSIGHTS_REPORT_OUTPUT_VAR_0(SKILL_INSIGHTS_REPORT_OUTPUT_VAR_1)}

Report URL: ${REPORT_URL}
HTML file: ${HTML_FILE_PATH}${FACETS_DIRECTORY===void 0?"":`
Facets directory: ${FACETS_DIRECTORY}`}

At-a-glance summary (for your context only — the user has not seen any output yet):
${SKILL_INSIGHTS_REPORT_OUTPUT_VAR_0(SKILL_INSIGHTS_REPORT_OUTPUT_VAR_5+SKILL_INSIGHTS_REPORT_OUTPUT_VAR_6)}

Respond with exactly the following, and nothing else. Do not add, omit, or reword any line:

Your shareable insights report is ready:
${REPORT_URL}
${LEFT_OUT_LINE?`
${LEFT_OUT_LINE}
`:""}${RECOMMENDATION_TIP_LINE?`
${RECOMMENDATION_TIP_LINE}
`:""}
Want to dig into any section or try one of the suggestions?
