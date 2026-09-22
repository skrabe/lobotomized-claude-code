<!--
name: 'Tool Hosts Notice: Say Where Machine'
description: >-
  Coordinator instruction to say, in the prompt given to a worker, that project
  work runs on the host that holds the user's current files.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_SAY_WHERE_MACHINE_VAR_0
-->
when a task needs the user's current files, say in the prompt you give the worker that it runs on ${SYSTEM_REMINDER_TOOL_HOSTS_SAY_WHERE_MACHINE_VAR_0} and does the project work there; only work that needs none of them (scratch computation, fetching docs) belongs here
