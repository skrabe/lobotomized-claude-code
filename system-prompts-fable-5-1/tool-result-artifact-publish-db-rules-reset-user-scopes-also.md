<!--
name: Artifact Publish Db Rules Reset User Scopes Also
description: >-
  Clause added to the db-rules publish error when the sent user block also omits
  stored scopes, telling the model to resend them or send an empty scopes list.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_USER_SCOPES_ALSO_VAR_0
-->
 The sent user block likewise omits its stored scopes${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_USER_SCOPES_ALSO_VAR_0()!==""?` (${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_USER_SCOPES_ALSO_VAR_0()})`:""}: resend user with them as well, or user: {"scopes": []} to drop them.
