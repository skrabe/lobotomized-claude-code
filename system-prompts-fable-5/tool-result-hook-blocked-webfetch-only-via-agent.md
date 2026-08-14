<!--
name: "Hook blocked web fetch agent-only path"
description: >-
  Tells the model a hook blocked the session's only web-fetch route and how a hook could exempt it.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_HOOK_BLOCKED_WEBFETCH_ONLY_VIA_AGENT_VAR_0
  - TOOL_RESULT_HOOK_BLOCKED_WEBFETCH_ONLY_VIA_AGENT_VAR_1
-->


Web pages can only be fetched through the ${TOOL_RESULT_HOOK_BLOCKED_WEBFETCH_ONLY_VIA_AGENT_VAR_0} agent in this session (there is no direct ${TOOL_RESULT_HOOK_BLOCKED_WEBFETCH_ONLY_VIA_AGENT_VAR_1} tool). If the page is required, tell the user; a hook that means to allow web fetching can exempt tool_input.subagent_type == "${TOOL_RESULT_HOOK_BLOCKED_WEBFETCH_ONLY_VIA_AGENT_VAR_0}" — a name match, which a project, user, or plugin agent defined under that same name would also pass with whatever tools it declares, so it fits only where no such agent is defined.