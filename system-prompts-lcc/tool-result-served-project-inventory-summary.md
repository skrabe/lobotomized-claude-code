<!--
name: 'Tool Result: Served project inventory summary'
description: >-
  Summary line of a served project-inventory call counting the commands, skills
  and agents returned, with an optional note on items left out.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_0
  - TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_1
  - TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_2
-->
${TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_0.commands.length} commands, ${TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_0.skills.length} skills, ${TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_0.agents.length} agents${TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_1?.TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_2?`, ${TOOL_RESULT_SERVED_PROJECT_INVENTORY_SUMMARY_VAR_1.cut} left out: the answer has no room for them`:""}
