<!--
name: 'Tool Result: Artifact Publish Unexamined Links User Approval Required'
description: >-
  safetyCheck decisionReason requiring the full consent dialog when
  publish-listed files are unexaminable, over-limit, from an unverified uploads
  folder, or ambiguously spelled.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_0?"Claude could not examine one of the files this publish lists for links":TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_1?"This publish lists more linked or redirected files than the automatic permission check can review":TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_2?"This publish reads a file from an uploads folder that is not a verified attachment of this conversation, and the automatic permission check cannot tell the difference":"This publish lists a file whose name does not say what it sends (a link, a hard link, or an ambiguous spelling), and the automatic permission check here is not shown that"} — approval must come from the user, in the full consent dialog${TOOL_RESULT_ARTIFACT_PUBLISH_UNEXAMINED_LINKS_USER_APPROVAL_REQUIRED_VAR_3}
