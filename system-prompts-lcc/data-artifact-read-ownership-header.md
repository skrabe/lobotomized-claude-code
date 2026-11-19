<!--
name: 'Data: artifact read ownership header'
description: >-
  Ownership clause of the artifact read header for the user's own artifact, with
  audience, type-publisher and co-writer provenance notes
ccVersion: 2.1.328
variables:
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_2
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_3
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_4
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_5
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_6
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_7
-->
owned by you${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience===void 0?"":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience==="owner"?`, ${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.folderMayLetOthersIn?"open to people with access to the folder it's in":"private"}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1(DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0)}`:`, shared with ${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_2(DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience)}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audienceView===void 0?"":` (${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_3(DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audienceView)})`}`}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.typeLocked?DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_4?"; the page comes from its Artifact type and was written by the type's publisher":"; created from an Artifact type, so this file may be the type publisher's":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_5||DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_6?"; may include content from a writer outside your organization":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.cowritten||DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.authoredByOthers===!0?"; may include contributions from other writers":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_7?"; may include content not published from this session":""}
