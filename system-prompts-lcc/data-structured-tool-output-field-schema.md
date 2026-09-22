<!--
name: 'Data: Structured tool output field schema'
description: >-
  Schema description of the tool_use_result Output object field surfaced in user
  messages, including per-tool shapes and the Agent/Task completed contract.
ccVersion: 2.1.218
-->
Structured tool output — the tool's full Output object, not the string content sent to the model. The shape is per-tool, keyed by the matching tool_use block's name (see the *Output types in toolTypes); MCP and dynamic tools carry their own shapes, so the field stays unknown-typed. For the Agent/Task tool the completed shape is the subagent's final report without the model-directed agentId/usage trailer, plus run totals — render from it instead of parsing the tool_result text.
