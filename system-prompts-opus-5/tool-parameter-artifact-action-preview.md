<!--
name: 'Tool Parameter: Artifact Action Preview'
description: >-
  Artifact action-enum addendum describing preview of a local page file with
  widths/themes and a layout checklist, with nothing uploaded.
ccVersion: 2.1.247
-->
 'preview' renders a local page file before you publish it — pass `file_path` (one .html file; files published beside it are not loaded), optionally `widths` (viewport widths in px, default 1280 and 390) and `themes` ('light', 'dark', default both) — and returns a screenshot per width and theme plus a checklist of layout and load problems (horizontal overflow, clipped content, theme-only color variables, blocked or local-only loads, diagram and console errors). Nothing is uploaded.
