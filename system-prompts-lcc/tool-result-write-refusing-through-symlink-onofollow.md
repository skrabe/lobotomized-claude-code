<!--
name: 'Tool result: write refused through symlink (O_NOFOLLOW fallback)'
description: >-
  Error returned when the in-place fallback of an atomic write hits ELOOP
  opening the target with O_NOFOLLOW, i.e. the target is a symlink.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_REFUSING_THROUGH_SYMLINK_ONOFOLLOW_VAR_0
-->
Refusing to write through symlink: ${TOOL_RESULT_WRITE_REFUSING_THROUGH_SYMLINK_ONOFOLLOW_VAR_0} (O_NOFOLLOW)
