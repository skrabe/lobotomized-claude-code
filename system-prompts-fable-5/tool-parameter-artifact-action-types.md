<!--
name: 'Tool Parameter: Artifact Action list_types / describe_type'
description: >-
  Action-enum addendum describing list_types and describe_type and the
  type_url/type_query fields they take.
ccVersion: 2.1.246
variables:
  - TOOL_PARAMETER_ARTIFACT_ACTION_TYPES_VAR_0
-->
 'list_types' lists the published Artifact types this account can start a new Artifact from — titles, descriptions and links (only \`type_query\` may accompany it); 'describe_type' shows one type's details — its files, whether it ships instructions, the capabilities it uses (pass the type's link as \`type_url\`, nothing else).${TOOL_PARAMETER_ARTIFACT_ACTION_TYPES_VAR_0?"":" Starting a new Artifact from a type is not available in this session."} See **Finding Artifact types** above.
