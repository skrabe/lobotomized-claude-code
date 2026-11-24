<!--
name: 'Tool Result: DesignSync inline data refused'
description: write_files error when inline data is not accepted and localPath must be used.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_INLINE_DATA_REFUSED_VAR_0
-->
write_files: inline data for ${TOOL_RESULT_DESIGN_WRITE_FILES_INLINE_DATA_REFUSED_VAR_0} is not accepted, since the plan uploads files from the folder approved at finalize_plan. Nothing in this call was uploaded. Write the content to a file at ${TOOL_RESULT_DESIGN_WRITE_FILES_INLINE_DATA_REFUSED_VAR_0} under that folder and pass that path as localPath, or stop and ask the user how to proceed.
