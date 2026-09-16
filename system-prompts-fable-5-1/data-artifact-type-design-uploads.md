<!--
name: Artifact Type Design Uploads
description: >-
  Canvas-type uploads clause: unlinked images/fonts stay assets and a design
  system goes under project/ds/<folder>/.
ccVersion: 2.1.273
-->
 Images and font files that no artboard links to by a relative path stay uploaded assets, as the instructions say; a design system, where one is used, goes in as files under `project/ds/<folder>/` plus a record in the index's `designSystems` list, the way their reference on design-system components says for a canvas kept as files.
