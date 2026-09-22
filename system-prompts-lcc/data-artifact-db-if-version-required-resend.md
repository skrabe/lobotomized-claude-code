<!--
name: 'Data: Artifact DB If-Version Required Resend'
description: >-
  Shared resend sentence interpolated into write_db version_required tool
  results: re-read with read_db and retry with if_version set to that version.
ccVersion: 2.1.269
-->
Read it back with read_db, base the change on what it holds now, and resend with if_version set to the version that read returns
