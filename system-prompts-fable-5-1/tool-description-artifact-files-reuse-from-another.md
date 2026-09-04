<!--
name: 'Tool Description: Artifact Files Reuse From Another'
description: >-
  Artifact-tool paragraph for copying another artifact's published files through
  the files map, excluding HTML/SVG/XML documents.
ccVersion: 2.1.261
-->
. Another artifact's published FILES are reused through `files` instead: map a path to {"artifact": "<its url>", "path": "<its published path>"} and that file is copied into your version server side with its type — script, style, data, font and image files copy this way; an HTML, SVG or XML document does not (read it with `path` and publish it as your own file)
