<!--
name: 'Data: Compaction summary refused or stopped calls note'
description: >-
  Notes refused or stopped calls whose text was too large to include and that
  stopped calls may have run
ccVersion: 2.1.314
variables:
  - DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_0
  - DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_1
-->
${DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_0>0?`${DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_1} more ${DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_1===1?"was a refused or stopped call":"were refused or stopped calls"}`:`The text of ${DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_1} refused or stopped ${DATA_COMPACTION_SUMMARY_LEFT_OUT_REFUSED_CALLS_NOTE_VAR_1===1?"call":"calls"} was too large to include`}; a stopped call may have run, in part or in full.
