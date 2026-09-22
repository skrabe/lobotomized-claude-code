<!--
name: 'Tool Description: Artifact Quickstart'
description: >-
  quickstart action description: look up published Artifact types and design
  systems (and the default README) before making a new artifact.
ccVersion: 2.1.274
variables:
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_2
-->
Look up what is needed before making ${TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_0===void 0?"a new artifact":TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_1[s]}: the published Artifact types and the design systems the user can open${TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_0==="other"?"":", and the default one's README"} — titles${TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_0==="other"?" and descriptions":", descriptions and README text"} other people in the organization wrote will be read into the conversation (read-only).${TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_0==="other"||!TOOL_DESCRIPTION_ARTIFACT_QUICKSTART_VAR_2?"":" If possible, the default design system's files and the type's are saved to this session's scratchpad and listed instead of that README."}
