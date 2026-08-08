<!--
name: 'Artifact Comments: Egress Proxy Blocked'
description: >-
  `err` returned by a9o() on a 403/blocked-by-allowlist; the Artifact tool's
  `comments` action rethrows it as `new Sp(nt.err, …)`, so the text lands in the
  model's is_error tool_result.
ccVersion: 2.1.221
-->

the network egress proxy in this environment blocks the artifact content host — comments cannot be read here (not a transient failure)
