<!--
name: 'Tool description: artifact publish update guidance'
description: >-
  Artifact tool prompt bullet on loading the design skill, reading an artifact
  before changing it, using url vs re-publishing file_path, and edits.
ccVersion: 2.1.332
variables:
  - TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_2
-->
${TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_0?`Before writing a new page, load the \`${TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_1}\` skill and read it. `:""}To change an artifact that this conversation didn't publish, read it in this conversation first, or the publish is refused. Build on what comes back, and publish from a later script with its link as \`url\`: without \`url\`, that publish creates a separate artifact. To change a page that you published in this conversation, publish the same \`file_path\` again with no \`url\`${TOOL_DESCRIPTION_ARTIFACT_PUBLISH_UPDATE_GUIDANCE_VAR_2?", and a small change as `edits`":""}.
