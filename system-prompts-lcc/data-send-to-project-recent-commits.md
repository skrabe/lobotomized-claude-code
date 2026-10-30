<!--
name: 'Send to Project: Recent commits section'
description: >-
  Recent commits section (heading and list) in the /send-to-project folder
  facts.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_RECENT_COMMITS_VAR_0
  - DATA_SEND_TO_PROJECT_RECENT_COMMITS_VAR_1
-->
## Recent commits (newest first, up to ${DATA_SEND_TO_PROJECT_RECENT_COMMITS_VAR_0})
${DATA_SEND_TO_PROJECT_RECENT_COMMITS_VAR_1.commits.length>0?DATA_SEND_TO_PROJECT_RECENT_COMMITS_VAR_1.commits.join(`
`):"(none)"}
