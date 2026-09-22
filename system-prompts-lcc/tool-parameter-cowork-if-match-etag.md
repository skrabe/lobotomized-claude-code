<!--
name: 'Tool parameter: Cowork output if_match CAS etag'
description: >-
  Model-facing describe() text for the if_match output-file CAS parameter in the
  Cowork staged-call mcp tool inputSchema.
ccVersion: 2.1.206
-->
Opaque lane etag the output row must still carry for the write to land (CAS). Omitted = unconditional last-writer-wins (an empty string is rejected, not treated as unconditional). A row that moved since fails that output with staging error_code=output_conflict and the requested bytes are not written. Redelivery of a completed CAS write re-runs and conflicts with its own prior write — treat output_conflict on a retry as possible-prior-success and reconcile by etag.
