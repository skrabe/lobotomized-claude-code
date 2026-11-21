<!--
name: 'Tool Parameter: app_* element_index'
description: >-
  inputSchema description of the shared app_* element_index, targeting an AX
  summary [N] instead of a coordinate.
ccVersion: 2.1.330
-->
The [N] prefix of a line in the last app_screenshot's AX summary or an app_ax_find result; any other number is refused. Targets that element's center directly instead of by coordinate. Use when coordinate-based clicking returns unsupported(canvas). Refused if something from another page inside the window (an embedded page, or the page around one) is at that position now, or if the action would go to something else of the same page than that element. Mutually exclusive with coordinate and target.
