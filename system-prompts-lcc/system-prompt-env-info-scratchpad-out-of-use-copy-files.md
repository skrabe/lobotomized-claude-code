<!--
name: 'System Prompt: Env info scratchpad out of use'
description: >-
  Tells the model the earlier scratchpad is out of use and to copy files under
  the working directory before attaching or publishing them
ccVersion: 2.1.325
variables:
  - SYSTEM_PROMPT_ENV_INFO_SCRATCHPAD_OUT_OF_USE_COPY_FILES_VAR_0
-->
The scratchpad directory announced earlier (${SYSTEM_PROMPT_ENV_INFO_SCRATCHPAD_OUT_OF_USE_COPY_FILES_VAR_0.from}) is out of use: put no new files there. Files that you wrote there may still be at that path. To go on working with one, first copy it under the primary working directory: a tool that attaches or publishes a file may refuse the old path.
