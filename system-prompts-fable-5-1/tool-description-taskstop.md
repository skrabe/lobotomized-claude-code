<!--
name: TaskStop tool description
description: >-
  Description of the TaskStop tool listing its behavior and the task_id
  parameter used to terminate a background task or teammate; sent to the model
  in the tool schema.
ccVersion: 2.1.206
-->

- Stops a running background task by its ID
- Takes a task_id parameter identifying the task to stop
- To stop an agent-team teammate, pass its agent ID ("name@team") or bare teammate name as task_id
- To stop a background agent spawned with a name, pass that name as task_id
- Returns a success or failure status
- Use this tool when you need to terminate a long-running task
