<!--
name: 'Tool Description: SharePoint file reference save hint'
description: >-
  Tool description prefix telling Claude to save files to SharePoint/OneDrive by
  sha256 file reference instead of typing base64
ccVersion: 2.1.328
-->
FILE REFERENCES: to save a file you can read here, don't type its base64; set contentBase64 to a file reference, sha256:<64 lowercase hex>:<its absolute path, with / between folders>. The app fills in the file's content when the call runs.
