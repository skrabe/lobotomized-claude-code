<!--
name: TaskCreate Agent-params guidance
description: >-
  TaskCreate misuse error returned to the model when Agent-tool parameters were
  passed instead.
ccVersion: 2.1.206
-->
This call used Agent-tool parameters (`prompt`/`subagent_type`). TaskCreate adds an item to the task list and takes `subject` and `description` string parameters. To delegate work to a subagent, use the Agent tool instead.
