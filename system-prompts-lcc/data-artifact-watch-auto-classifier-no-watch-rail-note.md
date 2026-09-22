<!--
name: Artifact watch classifier input — no watch rail
description: >-
  Rail label (g) used when watching for republishes is unavailable in this
  session, so the call only reports that.
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_WATCH_AUTO_CLASSIFIER_NO_WATCH_RAIL_NOTE_VAR_0
  - DATA_ARTIFACT_WATCH_AUTO_CLASSIFIER_NO_WATCH_RAIL_NOTE_VAR_1
-->
 (watching for republishes is not available in this session; the call only reports that${DATA_ARTIFACT_WATCH_AUTO_CLASSIFIER_NO_WATCH_RAIL_NOTE_VAR_0?.DATA_ARTIFACT_WATCH_AUTO_CLASSIFIER_NO_WATCH_RAIL_NOTE_VAR_1()===!0?DATA_ARTIFACT_WATCH_AUTO_CLASSIFIER_NO_WATCH_RAIL_NOTE_VAR_0.NO_WATCH_RAIL_COLLAB_CONSENT_CLAUSE:""})
