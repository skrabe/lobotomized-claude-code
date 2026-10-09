<!--
name: 'Data: Permission callback — expected return shape'
description: >-
  States the exact object a permission callback must return, which is what the
  model is told when it returns something else.
ccVersion: 2.1.295
variables:
  - DATA_PERMISSION_CALLBACK_EXPECTED_RETURN_SHAPE_VAR_0
-->
Expected {behavior: 'allow', updatedInput?: object} or {behavior: 'deny', message: string}. updatedPermissions may hold at most ${DATA_PERMISSION_CALLBACK_EXPECTED_RETURN_SHAPE_VAR_0} updates, rules and directories in all.
