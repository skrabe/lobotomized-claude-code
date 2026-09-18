<!--
name: 'Tool Result: Artifact Publish Contract Rollout Retry'
description: >-
  Artifact publish deploy-422 tool result when the tool chose the server's
  newest contract before it reached every server: nothing was published, send
  the same call again in about a minute, and do not pin an older contract.
ccVersion: 2.1.277
-->
Nothing was published and nothing is wrong with the call: this tool chose that contract because it is the server's newest, and it has not reached every server yet. Send the same call again in about a minute; do not pin an older contract to get past this.
