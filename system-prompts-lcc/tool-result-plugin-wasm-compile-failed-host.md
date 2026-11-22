<!--
name: 'Plugin hook error: …: $.wasm.compile: …'
description: >-
  Rejection of a plugin's $-API call; when the mod's hook does not catch it, the
  mod-under-development failure notice tells the model.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PLUGIN_WASM_COMPILE_FAILED_HOST_VAR_0
  - TOOL_RESULT_PLUGIN_WASM_COMPILE_FAILED_HOST_VAR_1
-->
${TOOL_RESULT_PLUGIN_WASM_COMPILE_FAILED_HOST_VAR_0.plugin}: $.wasm.compile: ${TOOL_RESULT_PLUGIN_WASM_COMPILE_FAILED_HOST_VAR_1}
