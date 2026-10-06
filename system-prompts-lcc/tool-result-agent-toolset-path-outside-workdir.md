<!--
name: 'Tool Result: agent toolset path outside working directory'
description: >-
  Error returned to the model when an agent-toolset file tool
  (read/write/edit/glob/grep) is given a path outside the session's working
  directory or permitted directories.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_0
  - TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_1
  - TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_2
-->
path ${TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_0.stringify(TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_1)} is outside ${TOOL_RESULT_AGENT_TOOLSET_PATH_OUTSIDE_WORKDIR_VAR_2}
