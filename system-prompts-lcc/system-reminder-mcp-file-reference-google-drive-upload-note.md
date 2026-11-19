<!--
name: 'System Reminder: Google Drive file reference upload note'
description: >-
  Tells Claude to upload local files to Google Drive create_file by sha256 file
  reference instead of typing base64, noting only that tool reads references
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_MCP_FILE_REFERENCE_GOOGLE_DRIVE_UPLOAD_NOTE_VAR_0
-->
${SYSTEM_REMINDER_MCP_FILE_REFERENCE_GOOGLE_DRIVE_UPLOAD_NOTE_VAR_0} to upload a local file with Google Drive's create_file, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set base64Content to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs. This works only in that Google Drive tool: other connectors can't read a file reference. If a reference is refused, do what the refusal says.
