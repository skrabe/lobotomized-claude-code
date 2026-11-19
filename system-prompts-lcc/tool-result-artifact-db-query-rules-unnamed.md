<!--
name: 'Tool Result: Artifact db query rules unnamed'
description: >-
  Artifact db query error suffix when the server did not name the rule, listing
  all query rules
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_ARTIFACT_DB_QUERY_RULES_UNNAMED_VAR_0
-->
. The server did not name the rule. The rules for \`query\` are: ${[...TOOL_RESULT_ARTIFACT_DB_QUERY_RULES_UNNAMED_VAR_0.values()].join("; ")}
