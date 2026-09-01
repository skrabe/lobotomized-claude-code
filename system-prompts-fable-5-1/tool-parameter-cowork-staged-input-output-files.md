<!--
name: 'Tool parameter: Cowork staged input/output files'
description: >-
  Model-facing inputSchema parameter description (zod .describe on the
  input_files/output_files array) explaining that declaring these makes a STAGED
  Cowork call with lane-row fetch and durable-at-ack output PUT
ccVersion: 2.1.206
-->
Declaring input_files or output_files makes this a STAGED call: rows are fetched from the synced-file lane into a private per-request temp dir the WORKER chooses (random, per-UID — the caller never sees or computes paths; it references files via tokens in arguments), the tool runs, and declared outputs are written back as lane rows (durable-at-ack PUT). The response then carries a `staging` result the caller switches on.
