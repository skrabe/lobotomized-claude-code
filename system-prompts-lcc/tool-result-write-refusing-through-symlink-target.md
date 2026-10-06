<!--
name: 'Tool Result: Write refused through symlink target'
description: >-
  Error returned when an atomic file write refuses a target path that is a
  symlink and asks for the real target path.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_REFUSING_THROUGH_SYMLINK_TARGET_VAR_0
-->
Refusing to write through symlink: ${TOOL_RESULT_WRITE_REFUSING_THROUGH_SYMLINK_TARGET_VAR_0}. Resolve the symlink and pass the real target path explicitly.
