<!--
name: Artifact Created-From-Type Fill Via Store Write
description: >-
  created_from_type tool_result telling the model this type is filled through
  its own store via data/write_db, not by publishing page files.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_1
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_2
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_3
-->
This type's instructions fill it through its own store, not with its page or data files: write it ${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_0(TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_1)}, passing \`url\`: ${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_2(TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_FILL_VIA_STORE_WRITE_VAR_3)}, as those instructions below describe (they cover only this Artifact's own content). Do not publish \`file_path\`/\`files\` to it as its content — a file only where those instructions call for one (an uploaded image or font, a support file) — and never index.html or any of the type's files.
