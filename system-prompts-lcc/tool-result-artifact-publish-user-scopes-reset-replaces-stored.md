<!--
name: Artifact Publish User Scopes Reset Replaces Stored
description: >-
  Publish tool error explaining that a sent user block would drop stored scopes,
  including profile name and avatar, and how to keep or drop them.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_1
-->
a sent user block replaces the stored one, scopes included, so this publish would have dropped ${TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_0.length===1?"it":"them"} (for profile, the page would no longer receive the viewer's name and avatar). To keep ${TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_0.length===1?"it":"them"}, ${TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_1!==""?`resend user with scopes: ${TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_1}`:"publish with capabilities omitted (the stored declaration stays as it is), or read it back and resend user with its scopes"}; to drop ${TOOL_RESULT_ARTIFACT_PUBLISH_USER_SCOPES_RESET_REPLACES_STORED_VAR_0.length===1?"it":"them"} on purpose, send user: {"scopes": []}.
