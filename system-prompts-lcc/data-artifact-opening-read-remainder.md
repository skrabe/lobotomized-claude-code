<!--
name: 'Data: Artifact Opening Read Remainder'
description: >-
  Opening-context note listing files left on disk for a later Read because they
  would not fit the Bash tails.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_OPENING_READ_REMAINDER_VAR_0
-->
Also on disk, not printed by the above because of their size; read one with the Read tool only if you need it: ${DATA_ARTIFACT_OPENING_READ_REMAINDER_VAR_0.join(", ")}
