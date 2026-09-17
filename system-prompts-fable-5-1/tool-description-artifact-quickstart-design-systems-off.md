<!--
name: 'Tool Description: Artifact Quickstart (Design Systems Off)'
description: >-
  quickstart action description when design systems are left out: types will be
  read into the conversation, with optional scratchpad files.
ccVersion: 2.1.274
variables:
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_2
-->
Look up what is needed before making ${TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_0===void 0?"a new artifact":TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_1[s]}: the published Artifact types — titles and descriptions their publishers wrote will be read into the conversation (read-only; design systems left out).${!TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_2||TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_0!=="slides"&&TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_DESIGN_SYSTEMS_OFF_VAR_0!=="design"?"":" If possible, the type's published files are also saved to this session's scratchpad and listed."}
