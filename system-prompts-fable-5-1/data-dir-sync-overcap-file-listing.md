<!--
name: 'Data: Directory sync overcap file listing'
description: >-
  Per-file size/commit listing interpolated into the overcap dir_sync_notice
  reminder so the model can name the blobs blocking sync.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_0
  - DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_1
  - DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_2
-->
${DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_0(DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_1.path)} (${DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_2(DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_1.size)} MiB, ${DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_1.commit===null?"uncommitted — in the working tree or staged":`brought in by commit ${DATA_DIR_SYNC_OVERCAP_FILE_LISTING_VAR_1.commit.slice(0,12)}`})
