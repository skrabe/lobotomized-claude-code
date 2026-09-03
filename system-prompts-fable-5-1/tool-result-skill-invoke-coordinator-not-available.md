<!--
name: 'Skill Invoke: Coordinator Session, Tell User Unavailable'
description: >-
  Suffix on Skill-tool denials in a coordinator session telling the model to
  report that /command is not available here.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_SKILL_INVOKE_COORDINATOR_NOT_AVAILABLE_VAR_0
  - TOOL_RESULT_SKILL_INVOKE_COORDINATOR_NOT_AVAILABLE_VAR_1
-->
It cannot be invoked via the ${TOOL_RESULT_SKILL_INVOKE_COORDINATOR_NOT_AVAILABLE_VAR_0} tool in this session, by the coordinator or by workers — tell the user /${TOOL_RESULT_SKILL_INVOKE_COORDINATOR_NOT_AVAILABLE_VAR_1} is not available here.
