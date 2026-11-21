<!--
name: 'Ship: Hosted Agent Label On At Start'
description: >-
  Message that a named hosted agent is running on the pull request because its
  watching/working label is on, used when /ship starts.
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_0
  - SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_1
  - SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_2
  - SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_3
-->
${SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_0(SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_1)} is running on pull request #${SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_2}: its label ${SKILL_SHIP_HOSTED_AGENT_LABEL_ON_AT_START_VAR_3} is on
