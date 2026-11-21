<!--
name: 'Tool Parameter: app target focused (macOS AXFocusedUIElement)'
description: >-
  target 'focused' parameter macOS arm: AXFocusedUIElement dispatch for
  canvas-heavy apps like Pages/Keynote.
ccVersion: 2.1.330
-->
(AXFocusedUIElement) instead of hit-testing at a coordinate. Use for canvas-heavy apps (Pages, Keynote) where the document body has no positional accessibility elements but the app's own text cursor is somewhere editable. 
