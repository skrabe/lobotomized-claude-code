<!--
name: 'Tool Description: Artifact Copy Assets From Url'
description: >-
  Artifact-tool paragraph for server-side copying of up to ten assets from
  another artifact via copy_from, from_url, and asset_ids.
ccVersion: 2.1.269
-->
 To reuse assets another artifact already holds (a design system's fonts or images, say), pass `action: "copy_from"` with the destination's `url`, the source's `from_url`, and up to ten `asset_ids` from the source's list_assets — the server copies them (nothing is downloaded or re-uploaded) and the result gives each copy's new url in the destination (reference it verbatim); both artifacts must be ones you can open in your organization.
