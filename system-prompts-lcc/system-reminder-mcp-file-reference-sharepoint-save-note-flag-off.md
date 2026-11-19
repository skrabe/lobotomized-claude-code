<!--
name: 'System Reminder: SharePoint file reference save note (flag off)'
description: >-
  Flag-off variant telling Claude to save local files to SharePoint by sha256
  file reference instead of base64
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_MCP_FILE_REFERENCE_SHAREPOINT_SAVE_NOTE_FLAG_OFF_VAR_0
-->
${SYSTEM_REMINDER_MCP_FILE_REFERENCE_SHAREPOINT_SAVE_NOTE_FLAG_OFF_VAR_0} to save a local file with sharepoint_upload_file or sharepoint_update_file, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set contentBase64 to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs. If a reference is refused, do what the refusal says.
