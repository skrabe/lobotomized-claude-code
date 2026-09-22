<!--
name: Artifact Read Owned Cowritten Html Consent
description: >-
  Ownership/consent paragraph for owned-but-cowritten or type-locked HTML in an
  artifact-read result.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_2
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_3
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_4
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_5
  - TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_6
-->
owned by you, but ${TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_0.typeLocked?"this file may be the Artifact type publisher's":TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_1?"it may hold content written outside your organization (your copy of someone else's artifact, or an outside editor published to it)":"a co-writer may have published to this artifact"}; its raw HTML comes back ${!TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_2?"only once the user has approved reading this artifact's files, which this session cannot ask":TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_3==="ask"?`once the user approves reading this artifact's files (the ${TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_4} tool's ${TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_5()} asks once)`:TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_3==="save"?`only on an approval that cannot be given from here; the ${TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_4} tool's ${TOOL_RESULT_ARTIFACT_READ_OWNED_COWRITTEN_HTML_CONSENT_VAR_6()} saves the published bytes instead`:"only on an approval no one in this session can give — raise it with the user"}
