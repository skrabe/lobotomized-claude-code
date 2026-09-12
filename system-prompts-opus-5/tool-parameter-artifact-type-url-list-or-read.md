<!--
name: 'Tool Parameter: Artifact Type URL List Or Read'
description: >-
  type_url schema description when the type catalog is on: read describes a
  type, list lists its Artifacts, with a create-unavailable caveat.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_TYPE_URL_LIST_OR_READ_VAR_0
-->
 read (no \`url\`): the type to describe. list: the type whose Artifacts to list, or Claude names the type with \`type\` instead.${TOOL_PARAMETER_ARTIFACT_TYPE_URL_LIST_OR_READ_VAR_0.typeCreateOn?"":" Creating an Artifact from a type is not available in this session, so it is accepted only with those two actions."}
