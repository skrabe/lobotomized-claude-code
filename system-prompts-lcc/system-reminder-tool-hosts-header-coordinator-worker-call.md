<!--
name: Delegate Machine Work To Workers
description: >-
  Tool-hosts header telling a coordinator to hand attached-machine work to
  spawned workers and how a worker addresses a machine.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_3
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_4
-->
Machines attached to this session${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_0} Hand work on an attached machine to the workers you spawn with ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_1} rather than doing it yourself. A worker runs a call there like this: ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_2}; without it the call runs here ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_3}. Each worker is shown this list of machines too; what it is not told is where you want its work done: ${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_COORDINATOR_WORKER_CALL_VAR_4.sayWhere}:
