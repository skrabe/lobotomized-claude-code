<!--
name: 'Tool result: uploaded .xlsx note'
description: >-
  Note appended to an asset upload result for .xlsx files about download-only
  serving and sharing limits.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_XLSX_NOTE_VAR_0
-->
 An .xlsx is only ever served as a download, and never to a link visitor or to a guest who can only view. The content scan can't read it: while a copy is stored, the artifact can't be made public or shared with anyone new outside the organization, so delete it once nothing needs it. A try that failed or was sent twice may have left another copy, which ${TOOL_RESULT_ARTIFACT_ASSET_UPLOADED_XLSX_NOTE_VAR_0('action "list_assets"',()=>'action "list" with `scope: "assets"`')} shows.
