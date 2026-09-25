<!--
name: 'Tool result: git bundle attribute source not uploading'
description: >-
  Upload refusal wrapper explaining the upload cannot follow an
  attribute-affecting git setting, with cause and remedy slots.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_NOT_UPLOADING_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_NOT_UPLOADING_VAR_1
-->
Not uploading this working tree: ${TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_NOT_UPLOADING_VAR_0}, and the upload cannot follow that setting, so a file git would change before storing it (to encrypt it, for example) could be uploaded as it is on disk. ${TOOL_RESULT_GIT_BUNDLE_ATTRIBUTE_SOURCE_NOT_UPLOADING_VAR_1}
