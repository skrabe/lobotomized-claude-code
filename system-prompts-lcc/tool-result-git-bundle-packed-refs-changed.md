<!--
name: 'Tool Result: Git Bundle Packed Refs Changed'
description: >-
  Bundle-failure result when git bundle create packed refs this checkout did not
  show, so refs changed or were redirected while the bundle was made.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_PACKED_REFS_CHANGED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PACKED_REFS_CHANGED_VAR_1
-->
git bundle create packed ${TOOL_RESULT_GIT_BUNDLE_PACKED_REFS_CHANGED_VAR_0(TOOL_RESULT_GIT_BUNDLE_PACKED_REFS_CHANGED_VAR_1)}, which this checkout did not show when the upload read its refs: its refs changed, or were redirected elsewhere, while the bundle was made. Make sure nothing else is writing to this checkout, inspect its git directory (a commondir file there was not written by git), then retry.
