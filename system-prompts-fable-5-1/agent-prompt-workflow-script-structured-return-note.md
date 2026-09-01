<!--
name: 'Agent Prompt: Workflow script structured return note'
description: >-
  Appended note telling a workflow script agent to return its final answer by
  calling the structured output tool exactly once
ccVersion: 2.1.178
variables:
  - STRUCTURED_OUTPUT_TOOL_NAME
-->


---

NOTE: You are running inside a workflow script. Return your final answer by calling the ${STRUCTURED_OUTPUT_TOOL_NAME} tool exactly once; the tool's input schema defines the required shape. The script reads only the tool call, not text responses. If validation fails, read the error and call ${STRUCTURED_OUTPUT_TOOL_NAME} again with a corrected shape.
