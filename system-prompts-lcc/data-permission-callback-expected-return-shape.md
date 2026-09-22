<!--
name: 'Data: Permission callback — expected return shape'
description: >-
  States the exact object a permission callback must return, which is what the
  model is told when it returns something else.
ccVersion: 2.1.233
-->
Expected {behavior: 'allow', updatedInput?: object} or {behavior: 'deny', message: string}.
