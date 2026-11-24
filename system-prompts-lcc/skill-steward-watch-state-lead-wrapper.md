<!--
name: 'Skill: Steward watch state lead wrapper'
description: >-
  Lead-in that picks the not-watching text or the still-on stop hint, followed
  by a blank line, ahead of the usage text.
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_0
  - SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_1
  - SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_2
-->
${SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_0.on===void 0?SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_1(SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_2):`The watch is still on. To end it, type ${SKILL_STEWARD_WATCH_STATE_LEAD_WRAPPER_VAR_2} with nothing after it.`}

