<!--
name: 'Tool Result: Artifact Root Is A Scratchpad/Workdir Symlink'
description: >-
  Validation error returned to the model when publish root is a symlink crossing
  between the working directory and the scratchpad.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_1
  - TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_2
  - TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_3
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_1)} is a link from ${TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_2===TOOL_RESULT_ARTIFACT_ROOT_SCRATCHPAD_WORKDIR_LINK_VAR_3[0]?"the working directory into your scratchpad directory":"your scratchpad directory into the working directory"} — pass the directory it points to instead
