<!--
name: 'Tool Parameter: Computer app_drag path'
description: >-
  path parameter for multi-point drags: point count, ordering of button
  down/move/up, and exclusivity with coordinate/to_coordinate
ccVersion: 2.1.330
variables:
  - TOOL_PARAMETER_COMPUTER_APP_DRAG_PATH_VAR_0
-->
A drag through several points: [[x, y], ...] with 2 to ${TOOL_PARAMETER_COMPUTER_APP_DRAG_PATH_VAR_0} points, same coordinate space as \`coordinate\`. The button goes down at the first point, the pointer moves through each point in order, and the button comes up at the last. Use it instead of \`coordinate\` and \`to_coordinate\` (never together with them) for strokes that are 
