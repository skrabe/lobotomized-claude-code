<!--
name: 'Tool result: plugin eval path link may resolve elsewhere refused'
description: >-
  Refuses a repo-authored plugin eval path that passes through a link the OS may
  resolve to a different folder, and says to point each link at a plain full
  path
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PLUGIN_EVAL_PATH_LINK_OS_MAY_RESOLVE_ELSEWHERE_REFUSED_VAR_0
  - TOOL_RESULT_PLUGIN_EVAL_PATH_LINK_OS_MAY_RESOLVE_ELSEWHERE_REFUSED_VAR_1
-->
${TOOL_RESULT_PLUGIN_EVAL_PATH_LINK_OS_MAY_RESOLVE_ELSEWHERE_REFUSED_VAR_0}: ${TOOL_RESULT_PLUGIN_EVAL_PATH_LINK_OS_MAY_RESOLVE_ELSEWHERE_REFUSED_VAR_1} passes through a link whose target the operating system may resolve to a different folder than the one Claude Code checked (for example, a target that is not valid UTF-8, or on Windows one with ".." after a folder name or too many links in a row) — refusing it. Point each link on the way straight at its folder with a plain full path
