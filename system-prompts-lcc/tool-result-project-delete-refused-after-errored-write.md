<!--
name: 'Tool result: project_delete refused after errored write'
description: >-
  project_delete validation refusal when an earlier project_write in the same
  response failed, since the doc may hold unsaved text.
ccVersion: 2.1.330
-->
This call deleted nothing. A project_write earlier in this response was refused or returned an error, and this call was sent before that result was known, so this doc may hold text that is saved nowhere else. This refusal applies to this response only.
