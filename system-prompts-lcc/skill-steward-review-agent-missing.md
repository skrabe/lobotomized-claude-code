<!--
name: 'Skill: Steward review agent missing'
description: >-
  Reason no review runs under a watch when the built-in general-purpose agent is
  missing
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_REVIEW_AGENT_MISSING_VAR_0
-->
the review needs Claude Code's own general-purpose agent, which this session doesn't have (another agent has that name, or none has), and it would run with nobody watching. To watch without a review, run /${SKILL_STEWARD_REVIEW_AGENT_MISSING_VAR_0}
