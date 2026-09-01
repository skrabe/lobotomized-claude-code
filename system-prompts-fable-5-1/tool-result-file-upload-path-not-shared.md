<!--
name: 'Tool Result: file_upload Path Not Shared With Session'
description: >-
  Rejection message built by Med(path) when a file_upload target resolves
  outside the session's allowed read roots or fails its attachment digest check;
  returned to the model as a <tool_use_error> tool_result instructing it to ask
  the user to share the file or run /add-dir.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_FILE_UPLOAD_PATH_NOT_SHARED_VAR_0
-->
Cannot upload "${TOOL_RESULT_FILE_UPLOAD_PATH_NOT_SHARED_VAR_0}": this session isn't allowed to read it. Ask the user to share the file, or to add its folder with /add-dir.
