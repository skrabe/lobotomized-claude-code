<!--
name: 'Tool Description: Artifact Asset True Upload'
description: >-
  Artifact tool-description clause for uploading a local file into the artifact
  asset store via url, file_path, and asset:true.
ccVersion: 2.1.276
variables:
  - TOOL_DESCRIPTION_ARTIFACT_ASSET_TRUE_UPLOAD_VAR_0
-->
. With \`url\`, \`file_path\` and \`asset: true\`, it instead uploads that local image, video, PDF, font or text file to the artifact's asset store; \`file_paths\` in place of \`file_path\` uploads up to ${TOOL_DESCRIPTION_ARTIFACT_ASSET_TRUE_UPLOAD_VAR_0} image, video, PDF, font, stylesheet or script files in one call under one approval (a text file goes in a call of its own), and the result gives each one's \`url\`. The page must declare the \`assets\` capability, and the \`artifact-capabilities\` skill has the limits. Claude references the uploaded file from the page by the \`url\` in the result, exactly as given
