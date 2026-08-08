<!--
name: 'Tool Result: Artifact DB Collection/Doc Id Format'
description: >-
  Artifact tool validateInput rejection returned to the model when `collection`
  or `doc_id` violate the segment grammar for a database path.
ccVersion: 2.1.224
-->
`collection` must be a "/"-separated path of 1-31 segments and `doc_id` one segment — letters, digits and _ - . ~ : @ + per segment, not "." or "..".
