<!--
name: 'Git bundle: config includes in workdir'
description: >-
  Refusal reason when git configuration pulls in includes or lies where a
  session could write it
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_INCLUDES_WORKDIR_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_CONFIG_INCLUDES_WORKDIR_VAR_1
-->
its git configuration (${TOOL_RESULT_GIT_BUNDLE_CONFIG_INCLUDES_WORKDIR_VAR_0}) pulls in include files, lies inside this working tree, its repository or a directory your settings open to Claude Code sessions, or includes a file there — configuration this upload could not have git list here, where a file a session may write could say what that capture runs; ${TOOL_RESULT_GIT_BUNDLE_CONFIG_INCLUDES_WORKDIR_VAR_1}move what the includes hold into the configuration file itself, stop granting sessions the directory that holds it (permissions.additionalDirectories, sandbox.filesystem.allowWrite, an Edit rule or --add-dir), or start from an ordinary clone
