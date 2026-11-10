<!--
name: Set Cwd Transcript Relocated Field
description: >-
  Description of the transcript_relocated boolean field in the set_cwd tool's
  output/response schema (W_C), which the model receives as a tool result;
  model-facing.
ccVersion: 2.1.322
-->
True when the transcript lives in the project slot derived from cwd (the normal case, and the no-op case). False only when the transcript move failed and the directory change could not be undone, so the move was kept — a cwd-derived resume lookup will then miss the session.
