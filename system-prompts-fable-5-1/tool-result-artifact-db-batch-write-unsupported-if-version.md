<!--
name: 'Tool Result: Artifact DB Batch Write Unsupported if_version'
description: >-
  Suffix on an artifact_db_write batch invalid_argument error when the batch was
  pinned, telling the model the server may not accept if_version on batch writes
  and to resend without pins only if unconditional writes are acceptable.
ccVersion: 2.1.267
-->
. If this server does not yet accept `if_version` on batch writes, that alone explains the refusal — resend without the pins only if unconditional writes are acceptable here
