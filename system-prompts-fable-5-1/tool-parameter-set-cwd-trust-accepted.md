<!--
name: Set Cwd Trust Accepted
description: >-
  Input-schema field description for the set_cwd tool's `trust_accepted` boolean
  instructing the model to only send true after showing a trust dialog;
  model-facing.
ccVersion: 2.1.201
-->
Host attestation that the user explicitly accepted a trust dialog for this directory. Only send true after showing one — the CLI records the directory as trusted (the same latch /cd's own prompt writes) before relocating. Requires trusted_directory.
