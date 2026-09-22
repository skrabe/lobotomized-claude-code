<!--
name: 'Tool Result: Write Refusing Symbolic Link Target'
description: >-
  Permission-deny tool result when a write target is a symlink, naming the
  resolved path the model should write instead.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_0
  - TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_1
  - TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_2
-->
Refusing to write ${TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_0(TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_1)}: it is a symbolic link. Write to the link's target path instead: ${TOOL_RESULT_WRITE_REFUSING_SYMBOLIC_LINK_TARGET_VAR_2}.
