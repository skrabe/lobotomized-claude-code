<!--
name: 'Skill: insights sessions left out under org sign-in'
description: >-
  Note that some sessions were excluded from /insights because they ran under a
  different organization sign-in.
ccVersion: 2.1.330
variables:
  - SKILL_INSIGHTS_SESSIONS_LEFT_OUT_ORG_SIGN_IN_VAR_0
-->
${SKILL_INSIGHTS_SESSIONS_LEFT_OUT_ORG_SIGN_IN_VAR_0} ${SKILL_INSIGHTS_SESSIONS_LEFT_OUT_ORG_SIGN_IN_VAR_0===1?"session is":"sessions are"} not included, because Claude Code could not confirm that this session may use ${SKILL_INSIGHTS_SESSIONS_LEFT_OUT_ORG_SIGN_IN_VAR_0===1?"it":"them"}. A session that ran under an organization sign-in (not a claude.ai login) shows only in a report that runs under the same sign-in.
