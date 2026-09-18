<!--
name: 'Tool Parameter: Artifact Publish Asset Flag With Copy-From'
description: >-
  asset-flag schema description when copy_from is on: url-true uploads
  file_path(s) to the asset store, or copies another artifact's assets via
  from_url and asset_ids.
ccVersion: 2.1.276
-->
publish with `url`: true uploads `file_path` (or each of `file_paths`) to that artifact's asset store instead of publishing it as the page — or, with `from_url` and `asset_ids` in place of `file_path`, copies those assets of another artifact into it server side (see **Calls**).
