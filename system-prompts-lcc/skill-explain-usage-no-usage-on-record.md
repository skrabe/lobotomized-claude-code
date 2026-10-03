<!--
name: 'Skill: Explain Usage No Usage On Record'
description: >-
  Prompt variant of /explain-usage used when the session has no recorded usage:
  tell the user so in one line and make no chart.
ccVersion: 2.1.288
variables:
  - SKILL_EXPLAIN_USAGE_NO_USAGE_ON_RECORD_VAR_0
-->
Show me where this session's tokens went.

No usage is on record ${SKILL_EXPLAIN_USAGE_NO_USAGE_ON_RECORD_VAR_0.startsAtSummary?"since this conversation was last summarized":"for this conversation yet"}. Say so in a line, and make no chart.
