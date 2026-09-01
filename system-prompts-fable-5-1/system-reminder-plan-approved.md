<!--
name: 'System Reminder: Plan approved'
description: >-
  Notifies Claude that the user approved the plan, provides the saved plan file
  and approved plan content, and allows coding to begin
ccVersion: 2.1.178
variables:
  - PLAN_FILE_PATH
  - TEAM_PARALLELIZATION_NOTE
  - PLAN_WAS_EDITED
  - APPROVED_PLAN
-->
Plan approved — start coding. Update your todo list if applicable.

Saved plan: ${PLAN_FILE_PATH}${TEAM_PARALLELIZATION_NOTE}

## ${PLAN_WAS_EDITED?"Approved Plan (edited by user)":"Approved Plan"}:
${APPROVED_PLAN}
