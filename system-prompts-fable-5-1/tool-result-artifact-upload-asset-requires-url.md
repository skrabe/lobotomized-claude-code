<!--
name: upload_asset requires url
description: >-
  Input-validation error returned to the model when upload_asset is called
  without the artifact's claude.ai URL.
ccVersion: 2.1.234
-->
action "upload_asset" requires `url` — the artifact's claude.ai URL (find it with action: "list").
