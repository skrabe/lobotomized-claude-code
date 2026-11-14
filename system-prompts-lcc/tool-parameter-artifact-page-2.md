<!--
name: 'Tool Parameter: Artifact Page Flag'
description: >-
  Person-schema Artifact tool page flag: return the rendered page when a read
  would otherwise return something else.
ccVersion: 2.1.325
variables:
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_0
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_1
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_3
-->
read only: true returns the rendered page in cases where a read otherwise returns something else.${TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_0([TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_1.typeCatalogOn?"a typed Artifact's read leaves out the type's own page":""].filter(TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_3))}
