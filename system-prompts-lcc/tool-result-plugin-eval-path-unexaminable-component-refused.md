<!--
name: 'Tool result: plugin eval path unexaminable component refused'
description: >-
  Plugin eval refusal for a path passing through an unreadable, dangling-link or
  over-long symlink component; surfaces in the eval mock tool result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_PLUGIN_EVAL_PATH_UNEXAMINABLE_COMPONENT_REFUSED_VAR_0
  - TOOL_RESULT_PLUGIN_EVAL_PATH_UNEXAMINABLE_COMPONENT_REFUSED_VAR_1
-->
${TOOL_RESULT_PLUGIN_EVAL_PATH_UNEXAMINABLE_COMPONENT_REFUSED_VAR_0}: ${TOOL_RESULT_PLUGIN_EVAL_PATH_UNEXAMINABLE_COMPONENT_REFUSED_VAR_1} passes through a component that cannot be examined (unreadable, a link or junction whose target does not exist, or a symlink chain too long to follow) — refusing it (it could not be vetted)
