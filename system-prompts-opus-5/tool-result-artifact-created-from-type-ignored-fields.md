<!--
name: 'Tool Result: Create-From-Type Ignored Fields'
description: >-
  Warning list passed through Ntl into created_from_type tool data, then
  rendered in the create tool_result.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_IGNORED_FIELDS_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_IGNORED_FIELDS_VAR_1
-->
${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_IGNORED_FIELDS_VAR_0.map((TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_IGNORED_FIELDS_VAR_1)=>`\`${TOOL_RESULT_ARTIFACT_CREATED_FROM_TYPE_IGNORED_FIELDS_VAR_1}\``).join(", ")} ignored on create — a create takes only the type and an optional title (the icon and description start as the type's); pass them when you publish files to it.
