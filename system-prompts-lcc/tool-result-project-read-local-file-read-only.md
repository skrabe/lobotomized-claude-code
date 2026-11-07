<!--
name: 'Projects: local_file is read-only'
description: 'local_file is for reading; copy it to change it, then project_write.'
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_PROJECT_READ_LOCAL_FILE_READ_ONLY_VAR_0
  - TOOL_RESULT_PROJECT_READ_LOCAL_FILE_READ_ONLY_VAR_1
-->
local_file is for reading only: read the parts you need with ${TOOL_RESULT_PROJECT_READ_LOCAL_FILE_READ_ONLY_VAR_0}'s offset and limit, or search it with ${TOOL_RESULT_PROJECT_READ_LOCAL_FILE_READ_ONLY_VAR_1}. Edits to it never reach the project, and project_write rejects it as local_path. To change the document or make a file from it, run \`cat /path/of/local_file > new-name\` in the working directory, where new-name is a name that no file there has, and work on that file. To save a change, call project_write with the document's path and that file as local_path. If the document is an upload such as a PDF, that saves a new text document and leaves the upload as it is.
