<!--
name: 'Tool Parameter: app_* target focused'
description: >-
  inputSchema description of the app_* `target: "focused"` enum, telling the
  model to dispatch against AXFocusedUIElement instead of a coordinate.
ccVersion: 2.1.246
-->
Dispatch against the application's currently-focused UI element (AXFocusedUIElement) instead of hit-testing at a coordinate. Use for canvas-heavy apps (Pages, Keynote) where the document body has no positional accessibility elements but the app's own text cursor is somewhere editable. Mutually exclusive with coordinate and element_index.

If you omit ALL of coordinate, element_index, and target, the action defaults to the same point as your most recent app_* action 
