<!--
name: >-
  Plugin hook error: …: $.tool.register: "…" refused: this session has no
  built-in tools…
description: >-
  Rejection of a plugin's $-API call; when the mod's hook does not catch it, the
  mod-under-development failure notice tells the model.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PLUGIN_TOOL_REGISTER_REFUSED_SESSION_HAS_NO_BUILT_TOOLS_VAR_0
  - TOOL_RESULT_PLUGIN_TOOL_REGISTER_REFUSED_SESSION_HAS_NO_BUILT_TOOLS_VAR_1
-->
${TOOL_RESULT_PLUGIN_TOOL_REGISTER_REFUSED_SESSION_HAS_NO_BUILT_TOOLS_VAR_0}: $.tool.register: "${TOOL_RESULT_PLUGIN_TOOL_REGISTER_REFUSED_SESSION_HAS_NO_BUILT_TOOLS_VAR_1.name}" refused: this session has no built-in tools (--tools ""), so it takes none from plugins
