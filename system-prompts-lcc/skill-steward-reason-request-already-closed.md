<!--
name: 'Steward reason: request already closed or merged'
description: >-
  Reason /steward gives for not starting: the branch's request on its host is
  already in a final state
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_0
  - SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_1
  - SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_2
-->
its ${SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_0(SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_1.host)} is ${SKILL_STEWARD_REASON_REQUEST_ALREADY_CLOSED_VAR_2.state} already
