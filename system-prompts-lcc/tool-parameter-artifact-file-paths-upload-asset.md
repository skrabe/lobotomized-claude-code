<!--
name: 'Tool Parameter: Artifact File Paths Upload Asset'
description: >-
  Artifact tool input-schema description for upload_asset file_paths: several
  local media files in one call, with types that must use file_path alone.
ccVersion: 2.1.276
variables:
  - TOOL_PARAMETER_ARTIFACT_FILE_PATHS_UPLOAD_ASSET_VAR_0
-->
upload_asset: several local image, video, PDF, font, stylesheet or script files in place of \`file_path\`, up to ${TOOL_PARAMETER_ARTIFACT_FILE_PATHS_UPLOAD_ASSET_VAR_0} in one call, all into the artifact that \`url\` names; one approval covers the call, and the result lists each file's id and url, or why it was not uploaded. A CSV, Markdown, JSON or plain-text file, a symbolic or hard link, and a file outside the working directory each go in a call of their own with \`file_path\`.
