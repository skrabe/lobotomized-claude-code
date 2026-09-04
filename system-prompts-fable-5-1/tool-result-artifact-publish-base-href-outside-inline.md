<!--
name: Artifact Publish Base Href Outside Inline
description: >-
  Publish warning when the page <base href> points outside the artifact and
  references must work without supporting files.
ccVersion: 2.1.261
-->
This page's <base href> points outside the artifact — at another site, or at the site root. Artifact hosting serves only the artifact's own folder and refuses a base on another site, so relative references won't resolve through it — remove the tag and make those references work without it (inline what the page needs).
