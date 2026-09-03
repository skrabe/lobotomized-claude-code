<!--
name: 'Data: Memory index listing cap note'
description: >-
  Trailing line appended to the assembled memory-directory index injected into
  context, stating how many memories were omitted by the recency cap.
ccVersion: 2.1.224
variables:
  - DATA_MEMORY_INDEX_LISTING_CAP_NOTE_VAR_0
  - DATA_MEMORY_INDEX_LISTING_CAP_NOTE_VAR_1
-->
... ${DATA_MEMORY_INDEX_LISTING_CAP_NOTE_VAR_0.length-DATA_MEMORY_INDEX_LISTING_CAP_NOTE_VAR_1.length} more memories not listed (showing the ${DATA_MEMORY_INDEX_LISTING_CAP_NOTE_VAR_1.length} most recently modified).
