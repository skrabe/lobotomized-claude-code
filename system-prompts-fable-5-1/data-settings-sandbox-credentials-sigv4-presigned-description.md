<!--
name: 'Data: sandbox.credentials.sigv4.presigned setting description'
description: >-
  Description of the `sandbox.credentials.sigv4.presigned` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Policy for presigned URLs (X-Amz-Algorithm/X-Amz-Signature in the query, no Authorization header): the signature lives in the URL itself. `deny` (default) or `passthrough`.
