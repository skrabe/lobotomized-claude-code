<!--
name: 'Agent Prompt: Plugin Eval MCP Stop Conditions'
description: >-
  Tells the eval mock MCP stand-in to emit a STOP line only when the current
  call meets an author-listed off-the-rails condition.
ccVersion: 2.1.251
variables:
  - AGENT_PROMPT_PLUGIN_EVAL_MCP_STOP_CONDITIONS_VAR_0
  - AGENT_PROMPT_PLUGIN_EVAL_MCP_STOP_CONDITIONS_VAR_1
-->
The evaluation author listed conditions under which this run must be STOPPED because the agent has gone off the rails. If — and only if — the current call meets one of them, reply with a single line starting "${AGENT_PROMPT_PLUGIN_EVAL_MCP_STOP_CONDITIONS_VAR_0} " followed by a short reason naming the condition. The conditions:
${AGENT_PROMPT_PLUGIN_EVAL_MCP_STOP_CONDITIONS_VAR_1.trim()}
