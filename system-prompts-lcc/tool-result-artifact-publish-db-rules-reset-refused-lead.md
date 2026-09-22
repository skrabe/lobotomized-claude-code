<!--
name: Artifact Publish Db Rules Reset Refused Lead
description: >-
  Opening of the publish tool error when a capabilities declaration re-sends db
  without the artifact's stored access rules.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_2
-->
your capabilities declaration re-sends db without its rules while the artifact stores ${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_0.length} ${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_1(TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_0.length,"access rule")}${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_2!==""?`: ${TOOL_RESULT_ARTIFACT_PUBLISH_DB_RULES_RESET_REFUSED_LEAD_VAR_2}`:' (not listed here; read the artifact with action "read" to see them)'} — 
