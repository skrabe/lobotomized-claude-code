<!--
name: Tool Hosts Machine File Path On Host
description: >-
  Tells the model that file tools with the machine argument act on the user's
  current files there under that host's permission rules, and that searches
  without it only see this session's snapshot.
ccVersion: 2.1.259
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_4
-->
${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_0} ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_1} ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_2} on the user's current files there, under that machine's own permission rules — give paths (file_path, or a search's path) as absolute paths on that machine; without "${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3}" they act on this session's snapshot. Searches made without "${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3}" only see this session's snapshot: to search the user's current files ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_4}
