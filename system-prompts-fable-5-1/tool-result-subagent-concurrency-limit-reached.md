<!--
name: 'Tool Result: Concurrent Subagent Limit Reached'
description: >-
  AgentPreconditionError returned from the Task tool when the concurrent-
  subagent cap is hit, instructing the model not to retry and to ask the user
  to raise CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_SUBAGENT_CONCURRENCY_LIMIT_REACHED_VAR_0
-->
Concurrent subagent limit reached. You can run ${TOOL_RESULT_SUBAGENT_CONCURRENCY_LIMIT_REACHED_VAR_0} subagents at once — do not retry. Ask the user to raise CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS if more are needed.
