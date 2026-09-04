<!--
name: 'Tool Description: Artifact Copy Assets From Url'
description: >-
  Artifact-tool paragraph for server-side copying of up to ten assets from
  another artifact via from_url and asset_ids.
ccVersion: 2.1.261
-->
. To reuse assets another artifact already holds (a design system's fonts or images, say), pass `from_url` (that artifact) and up to ten `asset_ids` from a `scope: "assets"` listing of it in place of `file_path`: the server copies them — nothing is downloaded or re-uploaded — and the result gives each copy's new url in this artifact, to reference verbatim; both artifacts must be ones you can open in your organization
