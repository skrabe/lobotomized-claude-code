<!--
name: 'Tool Result: Artifact DB Documents Elided'
description: >-
  Row substituted into the read_db tool_result for documents dropped by the
  result size cap, telling the model an over-cap document can only be read on
  the artifact page.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_2
-->

[${TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_0} ${TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_1(TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_0,"document")} elided — size cap${TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_2===""?"":`; ${TOOL_RESULT_ARTIFACT_DB_DOCUMENTS_ELIDED_VAR_2}`}. A single document larger than this result cap cannot be rendered here — only the artifact page itself can read it.]
