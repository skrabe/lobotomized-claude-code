<!--
name: Artifact Publish Base Href Outside With Files
description: >-
  Publish warning when the page <base href> points outside the artifact and
  supporting files can be published beside it.
ccVersion: 2.1.261
-->
This page's <base href> points outside the artifact — at another site, or at the site root. Artifact hosting serves only the artifact's own folder and refuses a base on another site, so relative references won't resolve through it — remove the tag and publish those files alongside the page (`files`), referenced by relative path.
