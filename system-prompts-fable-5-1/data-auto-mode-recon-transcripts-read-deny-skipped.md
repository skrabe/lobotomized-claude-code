<!--
name: 'Recon: transcripts skipped by read-deny gate'
description: >-
  Note in the auto-mode recon recent-usage section that some transcripts were
  not read due to permissions.deny / untrusted / out-of-scope paths.
ccVersion: 2.1.210
variables:
  - DATA_AUTO_MODE_RECON_TRANSCRIPTS_READ_DENY_SKIPPED_VAR_0
  - DATA_AUTO_MODE_RECON_TRANSCRIPTS_READ_DENY_SKIPPED_VAR_1
-->

_Skipped by the read-deny gate: ${DATA_AUTO_MODE_RECON_TRANSCRIPTS_READ_DENY_SKIPPED_VAR_0} ${DATA_AUTO_MODE_RECON_TRANSCRIPTS_READ_DENY_SKIPPED_VAR_1(DATA_AUTO_MODE_RECON_TRANSCRIPTS_READ_DENY_SKIPPED_VAR_0,"transcript")} not read — a permissions.deny rule covers the path, it is an untrusted network path, or it resolved outside the projects directory._
