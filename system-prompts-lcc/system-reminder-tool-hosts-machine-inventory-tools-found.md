<!--
name: 'System Reminder: tool hosts machine inventory tools found'
description: >-
  Attached-machine reminder line listing tools found on the machine when it
  attached, with a caveat that the list may be incomplete.
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_2
-->
- Found on ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_0} when it attached (looked up by name on its PATH, not run; ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_1.incomplete===!0?"the look-up was cut short, so this list is incomplete and a tool not listed may well be installed":"a tool not listed may still be installed"}): ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_INVENTORY_TOOLS_FOUND_VAR_2.join(", ")}.
