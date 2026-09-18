<!--
name: Artifact Upload Asset File Path Or Paths Not Both
description: >-
  Validation/deny error when upload_asset is called with both file_path and
  file_paths.
ccVersion: 2.1.276
-->
action "upload_asset" takes `file_path` (one file) or `file_paths` (several), not both.
