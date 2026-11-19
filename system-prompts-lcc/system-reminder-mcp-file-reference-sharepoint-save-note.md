<!--
name: 'System Reminder: SharePoint file reference save note'
description: >-
  Tells Claude to save local files with sharepoint_upload_file or
  sharepoint_update_file by sha256 file reference, noting only those tools read
  references
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_MCP_FILE_REFERENCE_SHAREPOINT_SAVE_NOTE_VAR_0
-->
${SYSTEM_REMINDER_MCP_FILE_REFERENCE_SHAREPOINT_SAVE_NOTE_VAR_0} to save a local file with sharepoint_upload_file or sharepoint_update_file, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set contentBase64 to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs. This works only in sharepoint_upload_file and sharepoint_update_file: other connectors can't read a file reference. If a reference is refused, do what the refusal says.
