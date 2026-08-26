<!--
name: 'Tool Result: Artifact Publish HTML Base Element'
description: >-
  Publish warning that a <base> tag will not apply on the artifact host so
  relative URLs must be fixed.
ccVersion: 2.1.246
-->
This page contains a <base> element. Published artifacts don't apply an author-written <base href> (the artifact host controls the document base), so relative references must work without it — remove the tag and adjust any path that relied on it.
