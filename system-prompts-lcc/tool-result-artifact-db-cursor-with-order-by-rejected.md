<!--
name: 'Tool Result: Artifact DB Cursor With order_by Rejected'
description: >-
  Artifact tool validateInput rejection returned to the model when
  `query.cursor` is combined with `query.order_by` (an ordered query is a single
  page).
ccVersion: 2.1.224
-->
an ordered query is a single page — `query.cursor` is not accepted with `query.order_by`; drop one of the two (narrow with `query.where` if one ordered page is not enough).
