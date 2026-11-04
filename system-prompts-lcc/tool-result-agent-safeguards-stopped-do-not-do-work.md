<!--
name: 'Tool Result: Agent safeguards stopped, do not take over'
description: >-
  Combines the safeguard stop notes and tells the parent agent not to do the
  stopped agent's work itself because safeguards cover this conversation too
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_0
  - TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_1
  - TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_2
-->
${TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_0} ${TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_1} Don't do the agent's work yourself: safeguards cover this conversation too.${TOOL_RESULT_AGENT_SAFEGUARDS_STOPPED_DO_NOT_DO_WORK_VAR_2}
