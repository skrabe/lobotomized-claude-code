<!--
name: 'Tool Description: Artifact type file-backed content update guidance'
description: >-
  Explains how to detect file-backed Artifact type content, read every changed
  file, republish it to the same URL, and preserve the type's index metadata
ccVersion: 2.1.273
variables:
  - ARTIFACT_ACTION_NAMES
  - FORMAT_ARTIFACT_INDEX_FILENAMES_FN
  - ARTIFACT_TYPE_FILE_STORAGE_CONFIG
  - ARTIFACT_FILE_STORAGE_MARKER
  - FORMAT_ARTIFACT_FILE_UPDATE_PUBLISH_INSTRUCTIONS_FN
  - ARTIFACT_URL
  - FORMAT_ARTIFACT_STORE_WRITE_PROHIBITION_FN
  - ARTIFACT_CREATED_ON_FILES_MARKER
  - FORMAT_ARTIFACT_URL_FN
-->
List its files first, before any other call (${ARTIFACT_ACTION_NAMES.list}). This Artifact's content lives in its own files under \`project/\`${ARTIFACT_ACTION_NAMES.storeDescribed?", never in its store":""}: ${FORMAT_ARTIFACT_INDEX_FILENAMES_FN(ARTIFACT_TYPE_FILE_STORAGE_CONFIG)} is the index, a JSON object with ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.indexKeys}, plus a \`createdOnFiles\` or \`convertedFrom\` object; and ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.files}.${ARTIFACT_FILE_STORAGE_MARKER(ARTIFACT_TYPE_FILE_STORAGE_CONFIG,ARTIFACT_ACTION_NAMES.storeDescribed)} Read each file you will change (${ARTIFACT_ACTION_NAMES.read}) and ${FORMAT_ARTIFACT_FILE_UPDATE_PUBLISH_INSTRUCTIONS_FN(ARTIFACT_URL)}. Send the index only when you ${ARTIFACT_TYPE_FILE_STORAGE_CONFIG.indexEdits}, keeping every other key and that object as read${ARTIFACT_ACTION_NAMES.storeDescribed?`; ${FORMAT_ARTIFACT_STORE_WRITE_PROHIBITION_FN(ARTIFACT_ACTION_NAMES.storeCall)}${ARTIFACT_ACTION_NAMES.storeCall===null?"":" — reading what its old store holds, to see what was there, is fine"}. If no ${FORMAT_ARTIFACT_INDEX_FILENAMES_FN(ARTIFACT_TYPE_FILE_STORAGE_CONFIG)} is listed, this Artifact has not been started on files: start it on files now as you would a new one, writing the index, with ${ARTIFACT_CREATED_ON_FILES_MARKER}, and every content file under one folder and publishing them to it in ONE call (\`url\`: ${FORMAT_ARTIFACT_URL_FN(ARTIFACT_URL)}, \`root\`: that folder, \`file_path\`: the index's absolute path, \`files\`: the rest by their \`project/…\` paths), and tell the user whether its earlier content was carried over; from then on its page shows only those files, nothing from its old store`:`. If no ${FORMAT_ARTIFACT_INDEX_FILENAMES_FN(ARTIFACT_TYPE_FILE_STORAGE_CONFIG)} is listed, this Artifact has no files content yet: write the index, with ${ARTIFACT_CREATED_ON_FILES_MARKER}, and every content file as for a new one, under one folder, and publish them to it in ONE call (\`url\`: ${FORMAT_ARTIFACT_URL_FN(ARTIFACT_URL)}, \`root\`: that folder, \`file_path\`: the index's absolute path, \`files\`: the rest by their \`project/…\` paths)`}
