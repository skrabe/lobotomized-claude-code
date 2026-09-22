<!--
name: 'Tool Result: Read Write Deny Link Unresolved'
description: >-
  Permission-deny tool result when a read or write path's symlink chain cannot
  be examined or does not resolve.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_0
  - TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_1
  - TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_2
-->
Refusing to ${TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_0==="write to"?"write":"read"} ${TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_1(TOOL_RESULT_READ_WRITE_DENY_LINK_UNRESOLVED_VAR_2)}: where it leads on disk could not be determined (a link on the way could not be examined, or the links do not resolve).
