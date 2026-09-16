<!--
name: Artifact Type Slides Files
description: >-
  Per-slide HTML file layout interpolated into the files-on-disk Artifact-type
  instructions (one section plus optional speaker-notes aside).
ccVersion: 2.1.273
-->
one `project/slides/<id>.html` per slide, <id> being its entry in the index's `order`, each holding exactly one `<section id="<id>">` in the slide format with, as that section's last child, one `<aside>` of plain-text speaker notes when the slide has any
