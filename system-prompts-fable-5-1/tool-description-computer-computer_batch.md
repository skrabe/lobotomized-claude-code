<!--
name: 'Tool Description: Computer computer_batch'
description: >-
  Describes the computer-use computer_batch tool for executing a sequence of
  computer actions in one call
ccVersion: 2.1.246
-->
e.g. click a field, type into it, press Return. Actions execute sequentially and stop on the first error. ${FRONTMOST_APPLICATION_ALLOWLIST_GUARD} The frontmost check runs before EACH action inside the batch — if an action opens a non-allowed app, the next action's gate fires and the batch stops there. 
