<!--
name: 'System Reminder: ToolSearch no room for definitions'
description: >-
  Meta note after a ToolSearch result that matched tool definitions did not fit
  in this result; search for fewer at a time.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_0
  - SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_1
  - SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_2
-->
These tools match, but ${SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_0} did not load them, because their definitions do not fit in this result: ${SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_1(SYSTEM_REMINDER_TOOLSEARCH_NO_ROOM_FOR_DEFINITIONS_VAR_2)}. They cannot be called until a search loads them. Search for fewer of them at a time. If that loads none, tell the user that the conversation has no room left for them.
