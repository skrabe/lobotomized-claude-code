<!--
name: Asset list usage header
description: >-
  Header line of the list_assets tool result reporting file count and byte/file
  quota usage.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0
-->
Assets of ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.url}: ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.usage.files} ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.usage.files===1?"file":"files"}, ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.usage.bytes} of ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.usage.max_bytes} bytes used (limit ${TOOL_RESULT_ARTIFACT_ASSET_LIST_USAGE_HEADER_VAR_0.usage.max_files} files).
