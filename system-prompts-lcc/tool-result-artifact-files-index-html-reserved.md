<!--
name: 'Tool Result: Artifact files map cannot publish index.html'
description: >-
  Validation error returned to the model when a `files` map uses the reserved
  published path index.html, which is the page itself (the file_path file, or
  the type-supplied page).
ccVersion: 2.1.328
-->
files: "index.html" cannot be a published path: that name is the page itself, the file sent as `file_path`, so `files` takes no entry for it. On an artifact made from a type, the type supplies the page and it cannot be replaced.
