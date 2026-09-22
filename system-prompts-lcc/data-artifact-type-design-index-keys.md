<!--
name: Artifact Type Design Index Keys
description: >-
  Required keys of project/canvas.json (v, title, boards, order, plus
  notes/pages/launch).
ccVersion: 2.1.273
-->
`"v": 3`, `title`, `boards`: one entry per artboard, keyed by its file name, holding its frame on the canvas (`x`, `y`, `w`, `h` in CSS px) and its options, `order`: those names back to front, and `notes`, `pages` and `launch` when the canvas has them
