<!--
name: 'Tool Result: Artifact DB List Rejects where/order_by'
description: >-
  Artifact tool validateInput rejection returned to the model when `query.where`
  or `query.order_by` are passed with db_op "list".
ccVersion: 2.1.224
-->
`query.where` and `query.order_by` are only accepted with db_op "query".
