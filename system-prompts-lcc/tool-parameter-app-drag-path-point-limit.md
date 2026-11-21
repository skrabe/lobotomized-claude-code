<!--
name: 'Tool Parameter: app_drag path point limit'
description: >-
  app_drag/app_batch path parameter: path delivered quickly; strokes over the
  point limit must be split into several drags.
ccVersion: 2.1.330
variables:
  - TOOL_PARAMETER_APP_DRAG_PATH_POINT_LIMIT_VAR_0
-->
whole path is delivered in well under a second. A stroke that needs more than ${TOOL_PARAMETER_APP_DRAG_PATH_POINT_LIMIT_VAR_0} points has to be split into several drags, and the button comes up between them.
