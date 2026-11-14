<!--
name: 'System Reminder: MCP file reference upload note'
description: >-
  Tells the model to upload local files to the Drive connector's create_file via
  a sha256 file reference instead of base64
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_MCP_FILE_REFERENCE_UPLOAD_NOTE_VAR_0
-->
${SYSTEM_REMINDER_MCP_FILE_REFERENCE_UPLOAD_NOTE_VAR_0} to upload a local file with create_file, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set base64Content to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs. If a reference is refused, do what the refusal says.
