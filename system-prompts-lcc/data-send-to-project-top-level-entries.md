<!--
name: 'Send to Project: Top-level entries section'
description: >-
  Top-level entries section (heading and listing) in the /send-to-project folder
  facts.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_TOP_LEVEL_ENTRIES_VAR_0
-->
## Top-level entries
${DATA_SEND_TO_PROJECT_TOP_LEVEL_ENTRIES_VAR_0.topLevelEntries.join("  ")||"(empty folder)"}
