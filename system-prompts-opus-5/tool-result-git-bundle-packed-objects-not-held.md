<!--
name: 'Tool Result: Git Bundle Packed Objects Not Held'
description: >-
  Bundle-failure result when the created bundle names commits this checkout's
  object store does not hold because another store stood in during the build.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_PACKED_OBJECTS_NOT_HELD_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PACKED_OBJECTS_NOT_HELD_VAR_1
-->
git bundle create packed ${TOOL_RESULT_GIT_BUNDLE_PACKED_OBJECTS_NOT_HELD_VAR_0(TOOL_RESULT_GIT_BUNDLE_PACKED_OBJECTS_NOT_HELD_VAR_1)} at commits this checkout's own object store does not hold: another object store stood in while the bundle was made. Make sure nothing else is writing to this checkout's git directory (objects/info in particular), then retry.
