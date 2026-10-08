<!--
name: Chrome upload credential refusal
description: >-
  Refuses uploading credential-named files without explicit user sharing and
  asks Claude to tell the user.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_CHROME_FILE_UPLOAD_CREDENTIAL_VAR_0
-->
Cannot upload "${TOOL_RESULT_CHROME_FILE_UPLOAD_CREDENTIAL_VAR_0}": its name or folder is one that credentials are kept under (such as .env, a .pem or .key file, or .ssh), so it is not uploaded on Claude's word alone. Tell the user it was not uploaded.
