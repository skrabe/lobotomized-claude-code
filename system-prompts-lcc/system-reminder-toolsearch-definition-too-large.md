<!--
name: 'System Reminder: ToolSearch definition too large'
description: >-
  Meta note after a ToolSearch result that matched tools were not loaded because
  each definition alone exceeds the context window.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_0
  - SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_1
  - SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_2
-->
These tools match, but ${SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_0} did not load them, because each definition is too large for the context window by itself: ${SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_1(SYSTEM_REMINDER_TOOLSEARCH_DEFINITION_TOO_LARGE_VAR_2)}. They cannot be called here, and another search will not load them. If the task needs one, tell the user that its definition is too large to load.
