<!--
name: ReadNotifications Origin Field
description: >-
  Output-schema description for the ReadNotifications origin source token,
  including open-set and normalization behavior.
ccVersion: 2.1.231
-->
Server-attested source token: "github_webhook" | "trigger_fire" | "mcp_send_message" (open set; unknown well-formed tokens pass through verbatim, off-grammar values coerce to "unknown").
