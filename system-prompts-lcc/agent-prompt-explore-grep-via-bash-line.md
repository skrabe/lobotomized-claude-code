<!--
name: 'Agent Prompt: Explore — content search tool line'
description: >-
  The Explore agent's instruction for searching file contents with regex, in the
  variant that routes `grep` through the Bash tool rather than naming a
  dedicated tool.
ccVersion: 2.1.233
variables:
  - AGENT_PROMPT_EXPLORE_GREP_VIA_BASH_LINE_VAR_0
-->
- Use \`grep\` via ${AGENT_PROMPT_EXPLORE_GREP_VIA_BASH_LINE_VAR_0} for searching file contents with regex
