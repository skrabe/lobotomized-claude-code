<!--
name: 'Tool Result: Artifact files map cannot publish index.html'
description: >-
  Validation error returned to the model when a `files` map uses the reserved
  published path index.html.
ccVersion: 2.1.218
-->
files: "index.html" cannot be a published path — the `html` argument is always the index. Pass that file's content as `html` and remove the "index.html" mapping.
