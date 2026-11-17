<!--
name: 'MCP upload tool: file references note'
description: >-
  Tells the model to upload a readable file by setting base64Content to a sha256
  file reference instead of typing base64.
ccVersion: 2.1.326
-->
FILE REFERENCES: to upload a file you can read here, don't type its base64; set base64Content to a file reference, sha256:<64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs.
