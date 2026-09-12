<!--
name: 'Tool Parameter: Artifact Page Flag'
description: >-
  Person-schema Artifact tool page flag: return the rendered page when a read
  would otherwise return something else.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_0
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_1
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_2
  - TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_3
-->
read only: true returns the rendered page in cases where a read otherwise returns something else.${TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_0([TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_1.liveEditOn&&TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_2?TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_2.CORE_PAGE_LIVE_CLAUSE:"",TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_1.typeCatalogOn?"a typed Artifact's read leaves out the type's own page":""].filter(TOOL_PARAMETER_ARTIFACT_PAGE_2_VAR_3))}
