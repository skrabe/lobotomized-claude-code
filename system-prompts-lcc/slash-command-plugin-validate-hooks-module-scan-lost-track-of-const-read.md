<!--
name: 'Slash Command: Plugin validate hooks module scan lost track of const read'
description: >-
  Hooks-module validation refusal when the scan lost track of a read of a state
  const and cannot show every use is a plain read
ccVersion: 2.1.292
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_SCAN_LOST_TRACK_OF_CONST_READ_VAR_0
-->
the scan lost track of this read of "${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_SCAN_LOST_TRACK_OF_CONST_READ_VAR_0}" and cannot show that every use of the const is a plain read. This is a fault of the scan, not of the module, which is refused rather than passed
