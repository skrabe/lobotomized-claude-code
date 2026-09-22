<!--
name: Artifact Publish Db Rules Reset Replaces Stored
description: >-
  Publish tool error explaining that a sent db block would reset stored access
  rules to the defaults and how to keep or reset them.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REPLACES_STORED_VAR_0
-->
a sent db block replaces the stored one, rules included, so this publish would have reset them to the defaults (anyone who can open the artifact can read its shared data, and anyone with more than view-only access can write it). To keep them, ${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REPLACES_STORED_VAR_0!==""?"resend db with those rules":"publish with capabilities omitted (the stored declaration stays as it is), or read it back and resend db with its rules"}; to reset them on purpose, send db: {"rules": []}.
