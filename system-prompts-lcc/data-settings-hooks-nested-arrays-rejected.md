<!--
name: 'Data: Settings hooks nested arrays rejected'
description: >-
  Error rejecting a settings write whose hooks are written as deeply nested
  arrays that may hide a PreToolUse/PermissionRequest hook
ccVersion: 2.1.326
variables:
  - DATA_SETTINGS_HOOKS_NESTED_ARRAYS_REJECTED_VAR_0
  - DATA_SETTINGS_HOOKS_NESTED_ARRAYS_REJECTED_VAR_1
-->
${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_REJECTED_VAR_0} rejected: hooks: written as nested arrays with values more than ${DATA_SETTINGS_HOOKS_NESTED_ARRAYS_REJECTED_VAR_1} levels deep, which may hold a PreToolUse/PermissionRequest hook that cannot be loaded; write "hooks" as an object of event names
