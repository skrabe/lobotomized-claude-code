<!--
name: 'Tool Parameter: app_* element_index'
description: >-
  inputSchema description of the shared app_* element_index, targeting an AX
  summary [N] instead of a coordinate.
ccVersion: 2.1.246
-->
Index into the AX summary returned by the last app_screenshot (the [N] prefix on each line). Targets that element's center directly instead of by coordinate. Use when coordinate-based clicking returns unsupported(canvas). Mutually exclusive with coordinate and target.
