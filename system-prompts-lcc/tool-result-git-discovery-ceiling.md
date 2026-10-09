<!--
name: 'Tool Result: Git Discovery Ceiling Cannot Express Path'
description: >-
  Explains that the plugin cache or temporary path contains an unsupported git
  discovery delimiter.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_0
  - TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_1
  - TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_2
-->
Cannot run git under ${TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_0(TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_1)}: its path contains "${TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_2}", which git's discovery ceiling (a "${TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_2}"-separated list) cannot express. Use a location without "${TOOL_RESULT_GIT_DISCOVERY_CEILING_VAR_2}" for this directory (the plugins cache — CLAUDE_CODE_PLUGIN_CACHE_DIR — or the temporary directory — TMPDIR — whichever this path is under).
