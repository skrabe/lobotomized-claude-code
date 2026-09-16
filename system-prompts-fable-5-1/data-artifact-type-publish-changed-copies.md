<!--
name: Artifact Type Publish Changed Copies
description: >-
  How to publish later file copies of a type-kept-as-files Artifact (url, root,
  absolute file_path, files by listed paths).
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_TYPE_PUBLISH_CHANGED_COPIES_VAR_0
  - DATA_ARTIFACT_TYPE_PUBLISH_CHANGED_COPIES_VAR_1
-->
save each changed copy at its listed path under one folder in the working directory or your scratchpad directory, then publish with \`url\`: ${DATA_ARTIFACT_TYPE_PUBLISH_CHANGED_COPIES_VAR_0(DATA_ARTIFACT_TYPE_PUBLISH_CHANGED_COPIES_VAR_1)}, \`root\`: that folder, \`file_path\`: the absolute path of one changed copy (not relative to \`root\`), and any other changed copies in \`files\` by their listed paths, so each is served at its listed path
