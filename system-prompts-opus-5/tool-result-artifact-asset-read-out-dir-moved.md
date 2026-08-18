<!--
name: Artifact asset read — out_dir moved after approval
description: >-
  Artifact asset_read error telling the model the destination directory no
  longer resolves where it did at approval, so the fetched asset was not saved.
ccVersion: 2.1.234
-->
out_dir no longer resolves where it did when the save was approved — the asset was fetched but not saved; retry so it is checked again
