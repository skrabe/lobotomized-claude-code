<!--
name: Appifact Publish Sources Must Be In Folder
description: >-
  AppifactRepl invalid_args when publish file_path/files are not regular files
  the script wrote in its own publish folder, with size caps.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_PUBLISH_SOURCES_MUST_BE_IN_FOLDER_VAR_0
  - TOOL_RESULT_APPIFACT_PUBLISH_SOURCES_MUST_BE_IN_FOLDER_VAR_1
-->
file_path and every local source in files must be a regular file the script wrote inside its own publish folder (files.dir(); root must be that folder, and files cannot be sent without it), named by a relative path with no "..", at most ${TOOL_RESULT_APPIFACT_PUBLISH_SOURCES_MUST_BE_IN_FOLDER_VAR_0>>20} MiB each and ${TOOL_RESULT_APPIFACT_PUBLISH_SOURCES_MUST_BE_IN_FOLDER_VAR_1>>20} MiB together
