<!--
name: Artifact Publish Capabilities Omitted Would Revoke
description: >-
  Publish tool error refusing a capabilities declaration that would silently
  drop stored capabilities.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_3
-->
your capabilities declaration omits the stored ${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_1.length,"capability","capabilities")} ${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_2.join(", ")} while adding new ones — a sent declaration replaces the stored one, so this publish would have silently revoked ${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_1.length===1?"it":"them"}. To keep ${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_1.length===1?"it":"them"}, republish declaring the union${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_3.length<600?`: ${TOOL_RESULT_ARTIFACT_PUBLISH_CAPABILITIES_OMITTED_WOULD_REVOKE_VAR_3}`:" (republish with capabilities omitted to read the stored declaration back, then resend it plus your additions)"}. To revoke on purpose, publish that union first, then republish without the revoked names (a declaration that adds no new name goes out as sent); capabilities: {} clears everything.
