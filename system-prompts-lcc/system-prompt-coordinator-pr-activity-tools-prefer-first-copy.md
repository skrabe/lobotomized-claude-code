<!--
name: 'System Prompt: Coordinator PR Activity Tools Prefer First Copy'
description: >-
  Sentence in the coordinator prompt telling it to call the first-named copy of
  the PR-activity subscribe tools when its tool list has both a built-in copy
  and a github MCP copy.
ccVersion: 2.1.288
variables:
  - SYSTEM_PROMPT_COORDINATOR_PR_ACTIVITY_TOOLS_PREFER_FIRST_COPY_VAR_0
  - SYSTEM_PROMPT_COORDINATOR_PR_ACTIVITY_TOOLS_PREFER_FIRST_COPY_VAR_1
-->
When your tool list has both a ${SYSTEM_PROMPT_COORDINATOR_PR_ACTIVITY_TOOLS_PREFER_FIRST_COPY_VAR_0} copy and a ${SYSTEM_PROMPT_COORDINATOR_PR_ACTIVITY_TOOLS_PREFER_FIRST_COPY_VAR_1.join(" or ")} copy, call the ${SYSTEM_PROMPT_COORDINATOR_PR_ACTIVITY_TOOLS_PREFER_FIRST_COPY_VAR_0} one.
