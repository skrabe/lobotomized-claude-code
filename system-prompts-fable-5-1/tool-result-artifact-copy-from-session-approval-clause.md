<!--
name: Artifact copy_from Session Approval Clause
description: >-
  Ask-message clause stating that approving covers further asset uploads and
  copies into this artifact for the rest of the session.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_SESSION_APPROVAL_CLAUSE_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_FROM_SESSION_APPROVAL_CLAUSE_VAR_1
-->
; approving covers further asset uploads and copies into this artifact${TOOL_RESULT_ARTIFACT_COPY_FROM_SESSION_APPROVAL_CLAUSE_VAR_0?"":", and reads of the source artifact's assets and published files,"} for the rest of this session${TOOL_RESULT_ARTIFACT_COPY_FROM_SESSION_APPROVAL_CLAUSE_VAR_1===null?"":" (a copy from this source asks again)"}.
