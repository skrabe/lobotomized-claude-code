<!--
name: 'Data: Dir Sync — Nested .gitignore Files Too Large'
description: >-
  Directory-sync refusal detail when the .gitignore files in the folder's
  subdirectories together exceed what sync reads (rule-count or MiB cap).
ccVersion: 2.1.282
variables:
  - DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_0
  - DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_1
  - DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_2
-->
the .gitignore files in this folder's subdirectories together hold more than sync reads (over ${DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_0.toLocaleString("en-US")} rules or ${DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_1(DATA_DIR_SYNC_NESTED_GITIGNORES_TOO_LARGE_VAR_2/1048576)} MiB in all); trim or remove some of them to sync this folder
