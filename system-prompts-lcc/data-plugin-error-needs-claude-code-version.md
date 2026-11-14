<!--
name: 'Plugin error: needs Claude Code version'
description: Fragment naming the Claude Code range a plugin needs and the running version
ccVersion: 2.1.325
variables:
  - DATA_PLUGIN_ERROR_NEEDS_CLAUDE_CODE_VERSION_VAR_0
  - DATA_PLUGIN_ERROR_NEEDS_CLAUDE_CODE_VERSION_VAR_1
-->
needs Claude Code ${DATA_PLUGIN_ERROR_NEEDS_CLAUDE_CODE_VERSION_VAR_0(DATA_PLUGIN_ERROR_NEEDS_CLAUDE_CODE_VERSION_VAR_1.range)}, this is ${DATA_PLUGIN_ERROR_NEEDS_CLAUDE_CODE_VERSION_VAR_1.claudeCodeVersion}
