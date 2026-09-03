<!--
name: 'Tool Result: Artifact Publish HTML Base Element'
description: >-
  Publish warning that an author-written <base href> may be ignored or refused
  by the artifact host, so relative URLs must work without it.
ccVersion: 2.1.259
-->
This page contains a <base href> element. Artifact hosting controls the document base — an author-written <base> may be ignored, or refused if it points away from the artifact's own origin — so relative references must work without it: remove the tag and adjust any path that relied on it.
