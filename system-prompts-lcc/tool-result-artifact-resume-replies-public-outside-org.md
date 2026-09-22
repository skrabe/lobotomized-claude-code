<!--
name: 'Tool Result: Artifact Resume Replies Public Outside Org'
description: >-
  resume_replies tool_result when auto-replies cannot be re-armed because no
  account signed in outside its organization can do so.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_0
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_1
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_2
-->
Auto-replies were NOT resumed on ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_0(TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_1.url)}: ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_PUBLIC_OUTSIDE_ORG_VAR_2}. No account signed in outside its organization can re-arm them; tell the user, and do not retry.
