<!--
name: 'Data: Directory sync nested repo inside uncarried directory'
description: >-
  Advice tail interpolated into the nested-repository dir_sync_notice when the
  nested repos also sit under a path sync does not carry.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_NESTED_REPO_INSIDE_UNCARRIED_DIR_VAR_0
-->
; ${DATA_DIR_SYNC_NESTED_REPO_INSIDE_UNCARRIED_DIR_VAR_0?"it also sits":"they also sit"} in a directory sync does not carry (a dot or dependency directory), so only committed files there travel
