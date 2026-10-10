<!--
name: 'Tool Result: permission denied, cloud hook cannot run'
description: >-
  Permission deny message when a PermissionRequest hook type cannot run in a
  cloud session.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_0
  - TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_1
-->
The PermissionRequest ${TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_0[t.type]??TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_1.type} hook can't run in this cloud session, so this permission request is denied.
