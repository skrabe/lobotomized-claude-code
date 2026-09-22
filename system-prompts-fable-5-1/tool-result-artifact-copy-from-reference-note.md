<!--
name: Artifact copy_from Reference Note
description: >-
  copy_from tool_result trailer telling the model to reference copies by
  destination URL, never the source id, and that they persist until
  delete_asset.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_1
  - TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_2
-->

Reference a copy from the destination's page by its url verbatim — e.g. <img src=${TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_0(TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_1)}> — never by the source's id, which resolves only on the source artifact. Everyone who can open the destination can load these; they stay until deleted with ${TOOL_RESULT_ARTIFACT_COPY_FROM_REFERENCE_NOTE_VAR_2('action "delete_asset"',()=>'action "delete" and an id as `path`')}.
