<!--
name: 'Skill: Explain Usage Caveat Replies Without Usage'
description: >-
  Caveat item in the /explain-usage prompt giving the number of earlier replies
  with no recorded usage that are therefore not counted.
ccVersion: 2.1.288
variables:
  - SKILL_EXPLAIN_USAGE_CAVEAT_REPLIES_WITHOUT_USAGE_VAR_0
-->
the number of earlier replies with no usage on record, and so not counted, is ${SKILL_EXPLAIN_USAGE_CAVEAT_REPLIES_WITHOUT_USAGE_VAR_0.responsesWithoutUsage}
