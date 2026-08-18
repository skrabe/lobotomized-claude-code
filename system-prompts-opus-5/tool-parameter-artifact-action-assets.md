<!--
name: 'Tool parameter: Artifact action — asset actions'
description: >-
  Action-parameter addendum describing upload_asset, list_assets, read_asset,
  and delete_asset and their required fields.
ccVersion: 2.1.234
-->
 'upload_asset' adds one local media, PDF, or font file to an existing artifact — pass `url` and `file_path`. 'list_assets' lists the files in an artifact's asset store (pass `url`; `after` continues a listing), 'read_asset' saves one of them to a local file named by its id (pass `url` and `asset_id`, optionally `out_dir`), and 'delete_asset' permanently removes one (pass `url` and `asset_id`). See **Artifact assets** above.
