<!--
name: 'System Reminder: Plan approved'
description: >-
  Notifies Claude that the user approved the plan, provides the saved plan file
  and approved plan content, and allows coding to begin
ccVersion: 2.1.325
variables:
  - PLAN_FILE_PATH
  - IS_PLAN_EDITED_BY_USER
  - TEAM_PARALLELIZATION_NOTE
  - APPROVED_PLAN_HEADING
  - APPROVED_PLAN
-->
Plan approved — start coding. Update your todo list if applicable.${PLAN_FILE_PATH===void 0?IS_PLAN_EDITED_BY_USER?`

The edit could not be saved to the plan file, so work from the text below.`:"":`

Saved plan: ${PLAN_FILE_PATH}`}${TEAM_PARALLELIZATION_NOTE}

## ${APPROVED_PLAN_HEADING}:
${APPROVED_PLAN}
