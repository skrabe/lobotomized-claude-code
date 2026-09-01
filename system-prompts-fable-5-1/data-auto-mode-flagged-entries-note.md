<!--
name: 'Data: Auto-mode uncleanable flagged-entries note'
description: >-
  Runtime note that N additional flagged permissions.allow entries can't be
  auto-removed, appended to the auto-mode setup skill prompt context.
ccVersion: 2.1.207
variables:
  - DATA_AUTO_MODE_FLAGGED_ENTRIES_NOTE_VAR_0
-->

${DATA_AUTO_MODE_FLAGGED_ENTRIES_NOTE_VAR_0} additional flagged ${DATA_AUTO_MODE_FLAGGED_ENTRIES_NOTE_VAR_0===1?"entry":"entries"} can't be shown or auto-removed (unusual characters or length) — the user should review permissions.allow by hand.
