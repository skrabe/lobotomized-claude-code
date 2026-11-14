<!--
name: 'System Reminder: MCP file reference attach note'
description: >-
  Tells the model to attach local files in create_draft/send_message via a
  sha256 file reference instead of base64
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_MCP_FILE_REFERENCE_ATTACH_NOTE_VAR_0
-->
${SYSTEM_REMINDER_MCP_FILE_REFERENCE_ATTACH_NOTE_VAR_0} to attach a local file in a create_draft or send_message call, don't type its base64, even if the tool's description or earlier calls in this conversation show base64. Set the attachment's content to a file reference, sha256:<the file's SHA-256, as 64 lowercase hex>:<its absolute path, with / between folders>, and set filename to the file's name. The app fills in the file's content when the call runs. An update_draft call removes a draft's files, so to change a draft that has files, make a new draft with the same files. If a reference is refused, do what the refusal says.
