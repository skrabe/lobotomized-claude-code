<!--
name: 'Tool Description: app_drag'
description: app_drag tool description
ccVersion: 2.1.330
-->
Drag inside the specified app's window: either in a straight line from `coordinate` to `to_coordinate`, or along `path` through several points. Use for text selection, moving items in a list, or drawing. In a background Chromium or Electron app a drag selects by character only if it starts in an input or text area; over page text or in a rich editor it selects whole blocks. A drag is delivered as raw input, which in some apps makes the app active for a moment (its windows are not raised) before the previously active app is restored. All points are in the same window-local coordinate space as `app_click`.
