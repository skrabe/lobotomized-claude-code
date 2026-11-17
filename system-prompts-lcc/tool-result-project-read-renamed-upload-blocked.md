<!--
name: 'Tool Result: project_read renamed upload blocked'
description: >-
  Projects project_read error: a made-up name for a duplicate-named upload could
  not be checked by hooks and permission rules, so the file was not read; tells
  the model what to do
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_0
  - TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_1
  - TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_2
-->
"${TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_0(TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_1)}" was not read. That name was made up because another item is also called "${TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_0(TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_2.stored_name)}", and this session's hooks and permission rules go by stored names, so they could not check it. "${TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_0(TOOL_RESULT_PROJECT_READ_RENAMED_UPLOAD_BLOCKED_VAR_2.stored_name)}" is the other item, not this one. If a script made this call, call the tool directly. Otherwise tell the user that the file can be read once it is uploaded under a name of its own.
