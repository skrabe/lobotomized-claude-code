<!--
name: 'Slash command /design: consent/revoke dispatch row'
description: >-
  Markdown dispatch-table row in the /design command prompt instructing the
  model to have the user run /design consent or /design revoke and to stop
  rather than treat the word as a brief.
ccVersion: 2.1.210
-->
| `consent` or `revoke` | Ask the user to run `/design consent` or `/design revoke` themselves — the dedicated commands manage the durable agent-access grant, and are available only with a first-party claude.ai login and a policy that permits Design access; if this session lacks those, say that instead. Do not treat the word as a design brief, and stop. |
