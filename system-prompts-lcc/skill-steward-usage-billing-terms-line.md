<!--
name: 'Skill: Steward usage billing terms line'
description: >-
  Terms line saying the command runs on the plan's usage limits or API/cloud
  bill
ccVersion: 2.1.330
variables:
  - SKILL_STEWARD_USAGE_BILLING_TERMS_LINE_VAR_0
  - SKILL_STEWARD_USAGE_BILLING_TERMS_LINE_VAR_1
-->
${SKILL_STEWARD_USAGE_BILLING_TERMS_LINE_VAR_0?"/ship runs in this session, on your plan's usage limits":`/${SKILL_STEWARD_USAGE_BILLING_TERMS_LINE_VAR_1} runs in this session, on your plan's usage limits`} or your API or cloud bill.
