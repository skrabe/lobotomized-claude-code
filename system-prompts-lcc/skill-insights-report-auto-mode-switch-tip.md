<!--
name: 'Skill: /insights report — Auto Mode Switch Tip'
description: >-
  Recommendation line the /insights report-output prompt tells the model to
  repeat verbatim. It estimates how many permission prompts auto mode could have
  handled in recent non-auto sessions and says how to turn auto mode on.
ccVersion: 2.1.281
variables:
  - SKILL_INSIGHTS_REPORT_AUTO_MODE_SWITCH_TIP_VAR_0
  - SKILL_INSIGHTS_REPORT_AUTO_MODE_SWITCH_TIP_VAR_1
-->
Tip: auto mode could have handled up to ~${SKILL_INSIGHTS_REPORT_AUTO_MODE_SWITCH_TIP_VAR_0(SKILL_INSIGHTS_REPORT_AUTO_MODE_SWITCH_TIP_VAR_1.estimatedPrompts).toLocaleString()} permission prompts across ${SKILL_INSIGHTS_REPORT_AUTO_MODE_SWITCH_TIP_VAR_1.nonAutoSessions.toLocaleString()} of your recent sessions — press Shift+Tab until the mode indicator shows auto.
