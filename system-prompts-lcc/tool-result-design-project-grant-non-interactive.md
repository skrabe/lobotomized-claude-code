<!--
name: 'Tool Result: Design project write grant inactive (non-interactive)'
description: >-
  Claude Design error in a non-interactive session when writing needs an
  inactive project write grant.
ccVersion: 2.1.291
-->
Writing to this project needs a project write grant that is not currently active (it may have been revoked) — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token. A durable project write grant can be approved from an interactive Claude Code session.
