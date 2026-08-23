<!--
name: Selected diff lines reminder
description: >-
  System reminder injecting lines the user selected from the diff view into the
  model's context.
ccVersion: 2.1.234
variables:
  - SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0
  - SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_1
  - SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_2
-->
The user selected the following ${SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0.lineCount} ${SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0.lineCount===1?"line":"lines"} from the diff view${SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0.filePath?` (in ${SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_1(SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0.filePath)})`:""}:
${SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_2(SYSTEM_REMINDER_SELECTED_LINES_IN_DIFF_VAR_0.content)}
