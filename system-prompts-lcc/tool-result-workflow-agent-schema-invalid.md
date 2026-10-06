<!--
name: 'Tool Result: workflow agent({schema}) invalid JSON Schema'
description: >-
  Thrown from a workflow script when agent({schema}) is handed a schema that
  does not parse; reaches the model as a task notification or a remote-workflow
  tool result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WORKFLOW_AGENT_SCHEMA_INVALID_VAR_0
-->
agent({schema}) received an invalid JSON Schema: ${TOOL_RESULT_WORKFLOW_AGENT_SCHEMA_INVALID_VAR_0.error}
