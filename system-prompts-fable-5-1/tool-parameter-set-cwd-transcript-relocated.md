<!--
name: Set Cwd Transcript Relocated Field
description: >-
  Description of the transcript_relocated boolean field in the set_cwd tool's
  output/response schema (W_C), which the model receives as a tool result;
  model-facing.
ccVersion: 2.1.201
-->
True when the transcript lives in the project slot derived from cwd (the normal case, and the no-op case). False only on the documented edge where the move completed but the transcript move failed AND the rollback chdir failed — a cwd-derived resume lookup will then miss the session.
