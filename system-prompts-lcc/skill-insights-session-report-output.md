<!--
name: 'Skill: /insights session report output'
description: >-
  Session-scoped /insights prompt giving the model the insights data and
  at-a-glance summary to relay without mentioning a report file
ccVersion: 2.1.314
variables:
  - SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_0
  - SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_1
  - SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_2
-->
The user just ran /insights to generate a usage report analyzing this Claude Code session.

Here is the full insights data:
${SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_0}

At-a-glance summary:
${SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_1}${SKILL_INSIGHTS_SESSION_REPORT_OUTPUT_VAR_2}

Give the user this summary in your own words. There is no report file to open, so don't mention one. End by asking whether they want to dig into any section or try one of the suggestions.
