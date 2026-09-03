<!--
name: 'Workshop Verifier: Island Open-Tag Byte Spelling'
description: >-
  Verifier violation hint returned when the ws-decisions island open tag does
  not end with the exact template bytes.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_ISLAND_OPEN_TAG_BYTE_SPELLING_VAR_0
-->
The ws-decisions island's open tag must END with the exact bytes ${TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_ISLAND_OPEN_TAG_BYTE_SPELLING_VAR_0} (double-quoted id attribute, last in the tag, as the template ships it; a page read back from the server may carry the server's own data-id after the id, nothing else) — the session's mechanical extraction scans for that sequence.
