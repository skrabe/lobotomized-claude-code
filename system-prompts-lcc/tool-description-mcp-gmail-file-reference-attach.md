<!--
name: 'Tool Description: MCP Gmail file reference attachments'
description: >-
  Prefix added to Gmail create_draft/send_message tool descriptions telling the
  model to attach readable files via sha256 file references instead of base64,
  and how drafts with files must be updated
ccVersion: 2.1.317
-->
FILE REFERENCES: to attach a file you can read here, don't type its base64; set the attachment's content to a file reference, sha256:<64 lowercase hex>:<its absolute path, with / between folders>, and set filename to the file's name. The app fills in the file's content once the user approves the call. An update_draft call removes a draft's files, so to change a draft that has files, make a new draft with the same files.
