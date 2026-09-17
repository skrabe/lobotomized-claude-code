<!--
name: Artifact Type No Own File Yet Older Store Note
description: >-
  Guidance that the Artifact has no file of its own yet and older content may
  live in a prior store.
ccVersion: 2.1.274
variables:
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_0
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_1
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_2
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_3
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_4
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_5
  - DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_6
-->
It has no file of its own yet — ${DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_0}, so there is no file of its own to list or read before writing. ${DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_1(DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_2,DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_3,DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_4)} If the user says this Artifact already has content, it may be in its older store, as ${DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_5.storeDocs}: ${DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_6===null?"this session has no call that reads that store, so ask them what it held":`read those first (${DATA_ARTIFACT_TYPE_NO_OWN_FILE_YET_OLDER_STORE_NOTE_VAR_6})`} and carry that into these files.
