<!--
name: Artifact watch — no linked originator
description: >-
  Explains that the session has no linked human originator, so it cannot hold
  durable wake subscriptions, and when a retry will re-check.
ccVersion: 2.1.232
-->
This session currently has no linked human originator, so it cannot hold wake subscriptions. Common causes: the session was started by a background event, or the connection between the chat platform and the Claude account needs re-linking. After the user addresses that (re-link and/or restart the session) — or if the server-side policy changes — a deliberate watch retry will re-check; automatic retries while the session stays originator-less are answered locally without contacting the server.
