<!--
name: 'Tool Result: Artifact Db Batch Pinned Unsupported'
description: >-
  write_db batch error when the server cannot take batch writes or if_version
  pins, so nothing was applied.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_PINNED_UNSUPPORTED_VAR_0
-->
db batch write failed (${TOOL_RESULT_ARTIFACT_DB_BATCH_PINNED_UNSUPPORTED_VAR_0("invalid_argument")}): this server does not take batch writes yet (nor, most likely, \`if_version\`), and a batch with \`if_version\` pins is never applied one write at a time — nothing was written. Resend it without the pins only if unconditional writes are acceptable here
