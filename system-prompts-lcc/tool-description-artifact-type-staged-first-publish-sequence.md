<!--
name: 'Tool Description: Artifact type staged first-publish sequence'
description: >-
  Explains the staged multi-call publish sequence for an Artifact type whose
  first publish needs an index file plus an initial content file published
  immediately, followed by the remaining files in later calls
ccVersion: 2.1.282
variables:
  - ARTIFACT_TYPE_FILE_STORAGE_CONFIG
  - ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG
  - ARTIFACT_FIRST_PUBLISH_CALL_PREFIX
-->
Write the files at those relative paths under one folder in your scratchpad directory (or the working directory), each written directly with your file-writing tool (it creates the folders: no shell step first, never a script that generates the files), in this order: \`${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.index}\` FIRST, complete, ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.indexHolds} (and its \`designSystems\` record where a design system is used), then ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.first}, and publish ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.written} right away, in one call: ${ARTIFACT_FIRST_PUBLISH_CALL_PREFIX} ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.firstSent}, plus any design-system files. Then, without pausing for the user, write ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.rest} and publish them with the same \`url\` and \`root\` — all in one more call, or a few files per call as you go (\`file_path\`: one new file's absolute path, \`files\`: the other new ones) — each call carrying only files no earlier call sent (each publish keeps the files earlier calls sent); ${ARTIFACT_TYPE_FIRST_PUBLISH_CONFIG.onlyOne} is done after the first call.
