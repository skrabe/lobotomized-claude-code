<!--
name: 'Data: Cloud move turn tail excerpt'
description: >-
  Marker heading the cut-off end of a single overlong turn when a conversation
  is handed to a cloud session
ccVersion: 2.1.318
variables:
  - DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_0
  - DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_1
  - DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_2
  - DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_3
-->
[${DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_0}] The end of a longer turn:
${DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_1.from(DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_2.at(-1)).subarray(-DATA_CLOUD_MOVE_TURN_TAIL_EXCERPT_VAR_3).toString()}
