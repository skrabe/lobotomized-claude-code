<!--
name: Coordinator subcommands still route note
description: >-
  Meta note in the coordinator command-block message explaining that listed
  subcommands still route to their own dedicated commands.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_0
  - TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_1
  - TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_2
  - TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_3
-->
Note: the subcommands ${TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_0.map((TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_1)=>`"/${TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_2(TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_3.name)} ${TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_2(TOOL_RESULT_COORDINATOR_SUBCOMMANDS_ROUTE_NOTE_VAR_1)}"`).join(", ")} route to their own dedicated commands and DO still work when the user types them directly in the terminal (remote-control clients gate some commands separately).
