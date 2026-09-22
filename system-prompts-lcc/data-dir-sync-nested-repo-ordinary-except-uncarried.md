<!--
name: 'Data: Directory sync nested repo ordinary except uncarried'
description: >-
  Advice tail interpolated into the nested-repository dir_sync_notice when some
  nested repos would sync as ordinary files except those under an uncarried
  directory.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_0
  - DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_1
  - DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_2
  - DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_3
-->
 — content kept as ordinary files (no .git of its own) syncs, except under a directory sync does not carry (a dot or dependency directory: ${DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_0.filter(DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_1).slice(0,DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_2).map(DATA_DIR_SYNC_NESTED_REPO_ORDINARY_EXCEPT_UNCARRIED_VAR_3).join(", ")})
