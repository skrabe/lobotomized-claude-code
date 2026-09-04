<!--
name: Artifact save outside scratchpad requires user approval
description: >-
  safetyCheck decisionReason for a read_file save that writes a file outside the
  session scratchpad where the project's tools may act on it.
ccVersion: 2.1.261
variables:
  - >-
    TOOL_RESULT_ARTIFACT_READ_FILE_SAVE_OUTSIDE_SCRATCHPAD_USER_APPROVAL_REQUIRED_VAR_0
-->
Saving ${TOOL_RESULT_ARTIFACT_READ_FILE_SAVE_OUTSIDE_SCRATCHPAD_USER_APPROVAL_REQUIRED_VAR_0} writes a file outside the session scratchpad, where the project's tools may act on it, with a path and contents chosen by a writer of the artifact — approval must come from the user, not the auto-permission classifier${TOOL_RESULT_ARTIFACT_READ_FILE_SAVE_OUTSIDE_SCRATCHPAD_USER_APPROVAL_REQUIRED_VAR_1}
