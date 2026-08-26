<!--
name: 'Tool Description: Artifact Assets Guidance'
description: >-
  Explains Artifact upload_asset, list_assets, read_asset, and delete_asset and
  when to use each.
ccVersion: 2.1.246
-->


**Artifact assets**: to put a local image, video, PDF, font, or text file (CSV, Markdown, JSON, plain text) into an existing artifact whose page declares the `assets` capability, pass `action: "upload_asset"` with the artifact's `url` and the `file_path`, then reference the file from the page by the `url` in the result, verbatim. `action: "list_assets"` (with `url`) lists what the store holds — ids, types, sizes — including files people added through the page; `action: "read_asset"` (with `url` and `asset_id`, optionally `out_dir`) saves one to a local file named by its id; `action: "delete_asset"` (with `url` and `asset_id`) removes one permanently — delete only a file nothing references any more, and only when the user asks or when replacing one you uploaded. The results and the `artifact-capabilities` skill carry the limits and details.
