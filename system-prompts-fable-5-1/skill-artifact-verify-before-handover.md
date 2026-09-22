<!--
name: Verify Before Handover
description: >-
  Artifact-capabilities skill section telling the model to functionally check a
  page's declared capabilities once before sharing the link.
ccVersion: 2.1.280
variables:
  - SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_0
  - SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_1
  - SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_2
  - SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_3
  - SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_4
-->
## Verify before you hand over the link — this session

A page whose \`capabilities\` you declared in this session gets one functional pass, not a render loop: ${[SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_0.check&&SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_1.previewOn?`before publishing, one \`${SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_2}\` preview of the page (capabilities are unavailable in the preview, so that code does not run there)`:"",...SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_3].filter(SKILL_ARTIFACT_VERIFY_BEFORE_HANDOVER_VAR_4).join("; ")}. Then tell the user in one line what you exercised and what you could not. An Artifact made from an Artifact type is not such a page: its capabilities come from the type, and the type's instructions govern any checking.
