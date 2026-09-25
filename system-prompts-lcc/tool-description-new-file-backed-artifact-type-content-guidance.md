<!--
name: 'Tool Description: New file-backed Artifact type content guidance'
description: >-
  Explains how to create and later update a file-backed Artifact type instance
  while preserving its index metadata, reading changed files, and publishing
  only project content
ccVersion: 2.1.282
variables:
  - ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG
  - ARTIFACT_TYPE_FILE_STORAGE_CONFIG
  - ARTIFACT_CREATED_ON_FILES_MARKER
  - FORMAT_ARTIFACT_TYPE_STORE_OVERRIDE_NOTE_FN
  - FORMAT_ARTIFACT_FIRST_PUBLISH_INSTRUCTIONS_FN
  - ARTIFACT_URL
-->
This type keeps a new Artifact's content in the Artifact's own files under \`project/\`${ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG.storeDescribed?`, never in its store${ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG.storeCall===null?"":` (no ${ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG.storeCall} for its content)`}`:""}. The files: \`${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.index}\`, the index, a JSON object with ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.indexKeys}, plus ${ARTIFACT_CREATED_ON_FILES_MARKER}; and ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.files}.${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.uploads}${FORMAT_ARTIFACT_TYPE_STORE_OVERRIDE_NOTE_FN(ARTIFACT_TYPE_FILE_STORAGE_CONFIG,ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG.storeDescribed)} ${FORMAT_ARTIFACT_FIRST_PUBLISH_INSTRUCTIONS_FN(ARTIFACT_TYPE_FILE_STORAGE_CONFIG,ARTIFACT_URL)} Later changes: read each file you will change (${ARTIFACT_CONTENT_STORAGE_ACCESS_CONFIG.read}) and publish only those the same way (\`file_path\`: one changed file's absolute path); send the index only when you ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.indexEdits}, keeping every other key and its \`createdOnFiles\` object as read. Never publish index.html, SKILL.md or anything under \`artifact-type/\`.
