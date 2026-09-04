<!--
name: Artifact read_file action description
description: >-
  Per-call description for action "read_file": saves one published file of a
  multi-file artifact at its published path, with the scratchpad-default and
  per-artifact approval rules.
ccVersion: 2.1.261
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_2
-->
Save one published file of a multi-file artifact${TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_0(TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_1)} at its published path — under the session scratchpad by default, anywhere else only with the user's approval each time; reads of the user's own artifacts need no separate approval, anyone else's ask once per artifact${TOOL_DESCRIPTION_ARTIFACT_READ_FILE_DYNAMIC_VAR_2()?" — an approval also covers server-side copies of them into other artifacts":""}.
