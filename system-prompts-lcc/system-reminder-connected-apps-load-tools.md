<!--
name: 'System Reminder: Connected apps, load their tools'
description: >-
  Lists the apps the person connected to the chat and tells Claude to load their
  tools via tool search when a request could use them
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_CONNECTED_APPS_LOAD_TOOLS_VAR_0
  - SYSTEM_REMINDER_CONNECTED_APPS_LOAD_TOOLS_VAR_1
-->
The person has connected these apps to this chat: ${SYSTEM_REMINDER_CONNECTED_APPS_LOAD_TOOLS_VAR_0.join(", ")}. Their tools are in the list above. When a request could draw on one of these apps, load its tools with ${SYSTEM_REMINDER_CONNECTED_APPS_LOAD_TOOLS_VAR_1} and use them, as you would use a tool that is already loaded.
