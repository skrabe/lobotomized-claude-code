<!--
name: 'Tool Description: Artifact nested runtime cleanup error'
description: >-
  Formats the Artifact publish error for irreducibly nested runtime markers,
  base tags, or repeated page skeletons and directs publishing the innermost
  clean document
ccVersion: 2.1.251
-->
This page carries runtime-marker comment blocks (`<!-- frame-runtime -->…<!-- /frame-runtime -->`, `<!-- chart-runtime -->…<!-- /chart-runtime -->`, `<!--claude-mermaid-runtime-begin…`, `<!--claude-hljs-runtime-begin…`), `data-frame-runtime` attributes, `<base href="/_f/…">` tags, or repeated artifact skeletons (`<!doctype html><html><head>…` wrapped around the page again and again) nested so that removing one keeps exposing another — nothing a genuine page or a fetched artifact contains. Delete every such comment block, attribute, tag, and repeated outer skeleton from the source, keep the innermost document, and publish again.
