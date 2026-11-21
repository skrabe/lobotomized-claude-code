<!--
name: 'Tool Result: Resumed agent cannot show permission prompt'
description: >-
  Deny message explaining the tool needs approval but this agent was resumed
  inside another tool call where no permission prompt can be shown
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PERMISSION_RESUMED_AGENT_CANNOT_PROMPT_VAR_0
-->
${TOOL_RESULT_PERMISSION_RESUMED_AGENT_CANNOT_PROMPT_VAR_0} did not run. It needs the user's approval, and the user was not asked: this agent was resumed inside another tool call, and no permission prompt can be shown from there. Asking again from this agent shows no prompt either. This agent's reply goes back to that tool call, not to the user. A call that the main conversation makes itself, or an agent that it resumes itself, can show a prompt.
