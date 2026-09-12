<!--
name: 'Tool Description: Artifact Asset True Upload'
description: >-
  Artifact tool-description clause for uploading a local file into the artifact
  asset store via url, file_path, and asset:true.
ccVersion: 2.1.269
-->
. With `url`, `file_path` and `asset: true`, it instead uploads that local image, video, PDF, font or text file to the artifact's asset store. The page must declare the `assets` capability, and the `artifact-capabilities` skill has the limits. Claude references the uploaded file from the page by the `url` in the result, exactly as given
