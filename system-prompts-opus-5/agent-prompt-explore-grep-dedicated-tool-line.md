<!--
name: 'Agent Prompt: Explore — content search, dedicated tool'
description: >-
  The Explore agent's content-search instruction in the variant that names a
  dedicated tool, rather than routing `grep` through Bash.
ccVersion: 2.1.233
variables:
  - AGENT_PROMPT_EXPLORE_GREP_DEDICATED_TOOL_LINE_VAR_0
-->
- Use ${AGENT_PROMPT_EXPLORE_GREP_DEDICATED_TOOL_LINE_VAR_0} for searching file contents with regex
