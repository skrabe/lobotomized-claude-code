<!--
name: 'Tool result: design write_files would replace earlier upload'
description: >-
  DesignSync write_files refusal when a new file would replace another file
  uploaded earlier under the same stored name in this plan.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_0
  - TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_1
  - TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_2
-->
write_files: "${TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_0}" would replace "${TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_1.typed}", which an earlier call under this plan uploaded from another file: claude.ai/design stores both as "${TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_2}". If they are two files, give one of them another path in the project. If the new one takes the old one's place, delete "${TOOL_RESULT_DESIGN_WRITE_FILES_STORED_NAME_REPLACES_EARLIER_UPLOAD_VAR_2}" first, if this plan's deletes hold it, or call finalize_plan again.
