<!--
name: 'Data: Agent Import — Source Scan Failed Warning'
description: >-
  Warning emitted when a foreign agent's config can't be read; joined into BA_'s
  `value`, which the local-command dispatcher wraps as
  `Ur({content:'<local-command-stdout>…'})` — a real user message in the API
  request.
ccVersion: 2.1.214
variables:
  - DATA_AGENT_IMPORT_SCAN_FAILED_WARNING_VAR_0
-->
Couldn't read ${DATA_AGENT_IMPORT_SCAN_FAILED_WARNING_VAR_0.displayName} config — it may be malformed. Skipping.
