<!--
name: 'Tool Result: project_write save unconfirmed'
description: >-
  project_write error when the new content could not be confirmed as saved;
  instructs the model to project_read before retrying.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_PROJECT_WRITE_SAVE_UNCONFIRMED_VAR_0
-->
project_write: could not confirm that the new content was saved. Nothing was removed, so the project may now list this path twice. ${TOOL_RESULT_PROJECT_WRITE_SAVE_UNCONFIRMED_VAR_0}
