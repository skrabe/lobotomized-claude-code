<!--
name: 'Slash command /design: sync/login dispatch row'
description: >-
  Markdown dispatch-table row in the /design command prompt instructing the
  model to have the user run /design sync or /design login themselves and to
  stop.
ccVersion: 2.1.210
-->
| `sync` / `login` | Ask the user to run `/design sync` or `/design login` themselves — when this session offers them, typing the command directly routes to the dedicated `/design-sync` / `/design-login` surfaces, which this prompt cannot reach; if the session does not offer them, say that instead. Do not guess at their availability, and stop. |
