<!--
name: 'Tool Result: Design Project Grant Mint Refused (404)'
description: >-
  ClaudeDesign error message returned to the model when POST /v1/design/grants
  404s, telling it the project cannot hold a durable write grant and to fall
  back to finalize_plan with a plan_token.
ccVersion: 2.1.211
-->
This project cannot hold a durable write grant for this account (it may be shared from another organization, or not viewable) — use finalize_plan with writes/deletes and pass the returned plan_token for writes to this project.
