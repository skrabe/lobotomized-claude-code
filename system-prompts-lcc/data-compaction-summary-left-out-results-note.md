<!--
name: 'Data: Compaction summary left-out tool results note'
description: >-
  States how many tool results were too large to include in the summary and that
  those calls may have had effects
ccVersion: 2.1.314
variables:
  - DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_0
  - DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1
  - DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_2
-->
${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_0} tool ${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1?"result":"results"} (${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_2}) ${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1?"was":"were"} too large to include, and this summary was written without ${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1?"it":"them"}. ${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1?"That call was":"Those calls were"} made and may have had effects; the summary does not know what ${DATA_COMPACTION_SUMMARY_LEFT_OUT_RESULTS_NOTE_VAR_1?"it":"they"} returned.
