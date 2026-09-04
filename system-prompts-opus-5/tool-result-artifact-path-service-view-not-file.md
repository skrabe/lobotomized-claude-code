<!--
name: Artifact path names a service view not a file
description: >-
  read_file rejection when the requested path is one of the artifact service's
  own views rather than a published file.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PATH_SERVICE_VIEW_NOT_FILE_VAR_0
  - TOOL_RESULT_ARTIFACT_PATH_SERVICE_VIEW_NOT_FILE_VAR_1
-->
path ${TOOL_RESULT_ARTIFACT_PATH_SERVICE_VIEW_NOT_FILE_VAR_0(TOOL_RESULT_ARTIFACT_PATH_SERVICE_VIEW_NOT_FILE_VAR_1)} names one of the artifact service's own views, not a published file; list_files shows the readable paths
