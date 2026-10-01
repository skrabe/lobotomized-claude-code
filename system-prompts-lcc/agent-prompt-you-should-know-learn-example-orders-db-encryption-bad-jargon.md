<!--
name: 'You should know: jargon encryption learn example'
description: >-
  Bad jargon-dense learn: example about envelope encryption and KMS in the You
  should know side-agent prompt.
ccVersion: 2.1.286
-->
learn: Your Orders DB at-rest encryption uses envelope encryption with per-table data keys wrapped by a KMS master key, so every cold read pays a KMS decrypt round-trip plus AES-GCM overhead on the hot path
