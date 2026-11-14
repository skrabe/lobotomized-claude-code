<!--
name: 'Skill: /insights no sessions qualified'
description: >-
  /insights command prompt when no session qualified for analysis, telling
  Claude to reply with a fixed nothing-to-report message.
ccVersion: 2.1.325
variables:
  - SKILL_INSIGHTS_NO_SESSIONS_QUALIFIED_VAR_0
  - SKILL_INSIGHTS_NO_SESSIONS_QUALIFIED_VAR_1
-->
The user just ran /insights, but no session qualified for analysis, so there is no report to share.

Respond with exactly the following, and nothing else. Do not add, omit, or reword any line:

There's nothing to report yet (${SKILL_INSIGHTS_NO_SESSIONS_QUALIFIED_VAR_0.toLocaleString()} ${SKILL_INSIGHTS_NO_SESSIONS_QUALIFIED_VAR_1(SKILL_INSIGHTS_NO_SESSIONS_QUALIFIED_VAR_0,"session")} found).
/insights needs a session with at least two of your messages, lasting about a minute or more.
