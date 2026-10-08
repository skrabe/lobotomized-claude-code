<!--
name: Cloud PermissionRequest hook denied
description: >-
  Denies a permission request whose configured hook cannot run in the cloud
  session.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_0
  - TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_1
-->
The PermissionRequest ${TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_0[o.type]??TOOL_RESULT_PERMISSION_DENIED_CLOUD_HOOK_VAR_1.type} hook can't run in this cloud session, so this permission request is denied.
