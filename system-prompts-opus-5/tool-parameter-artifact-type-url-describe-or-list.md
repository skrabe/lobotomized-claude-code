<!--
name: 'Tool Parameter: Artifact type_url Describe Or List'
description: >-
  type_url .describe() addendum covering describe_type and list (and that
  create-from-type may be unavailable).
ccVersion: 2.1.257
variables:
  - TOOL_PARAMETER_ARTIFACT_TYPE_URL_DESCRIBE_OR_LIST_VAR_0
-->
 With action "describe_type": the type to describe (a link from a list_types result); with action "list": the type whose Artifacts to list (or name it with \`type\` instead).${TOOL_PARAMETER_ARTIFACT_TYPE_URL_DESCRIBE_OR_LIST_VAR_0?"":" Creating an Artifact from a type is not available in this session, so it is accepted only with those two actions."}
