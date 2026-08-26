<!--
name: 'Tool Hosts Notice: File Path Must Be On The Host'
description: >-
  tool_hosts_notice clause for off-sync: file tools with the machine argument
  use absolute paths there; without it they see only this session's snapshot.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3
  - SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_4
-->
${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_0} ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_1} ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_2} on the user's current files in its project folder — give file_path as an absolute path on that machine; without "${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3}" they act on this session's snapshot. Searches made without "${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_3}" only see this session's snapshot: to search the user's current files run grep or find with ${SYSTEM_REMINDER_TOOL_HOSTS_MACHINE_FILE_PATH_ON_HOST_VAR_4} there
