<!--
name: Workshop Sidecar History Contract Violation
description: >-
  Artifact publish refusal returned when a workshop redeploy omits
  refusedSidecarHistory, so the sidecar-ordering gate cannot run.
ccVersion: 2.1.219
-->
workshop publish contract violation: redeploys must pass refusedSidecarHistory (the AppState sidecar record for the target slug; [] when none) — refusing rather than skipping the sidecar-ordering gate
