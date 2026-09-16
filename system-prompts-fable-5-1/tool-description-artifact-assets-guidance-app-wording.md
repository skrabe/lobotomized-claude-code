<!--
name: 'Tool Description: Artifact assets guidance (app wording)'
description: >-
  App-worded guidance for uploading, listing, reading, copying, referencing, and
  deleting files in an Artifact asset store
ccVersion: 2.1.273
variables:
  - ARTIFACT_CAPABILITIES_SKILL_NAME
  - CAN_COPY_ARTIFACT_ASSETS
  - CAN_COPY_PUBLISHED_ARTIFACT_FILES
-->
**Artifact assets**: \`action: "upload_asset"\` with an artifact's \`url\` and a \`file_path\` adds that local image, video, PDF, font, stylesheet, script or text file to the asset store of an existing artifact whose page declares the \`assets\` capability, and Claude references it from the page by the \`url\` in the result, exactly as given. \`action: "list_assets"\` (with \`url\`) lists the store, including files people added through the page; \`action: "read_asset"\` (with \`url\` and \`asset_id\`) saves one to a local file; \`action: "delete_asset"\` (with \`url\` and \`asset_id\`) removes one permanently, only for a file nothing references any more, and only when the person asks or when replacing one it uploaded. The \`${ARTIFACT_CAPABILITIES_SKILL_NAME}\` skill has the limits.${CAN_COPY_ARTIFACT_ASSETS?` \`action: "copy_from"\` with the destination's \`url\`, the source artifact's \`from_url\` and up to ten \`asset_ids\` from the source's list_assets reuses assets another artifact already holds, such as a design system's fonts: the server copies them and the result gives each copy's new url, to reference exactly as given; both artifacts must be ones the person can open in their organization.${CAN_COPY_PUBLISHED_ARTIFACT_FILES?' Another artifact\'s published files are reused through a publish instead: in `files`, Claude maps a path to `{"artifact": "<its url>", "path": "<its published path>"}` and the server copies that file into the new version with its type. Script, style, data, font and image files copy this way; an HTML, SVG or XML document does not, so Claude reads it with `read_file` and publishes it as its own file.':""}`:""}
