<!--
name: 'Tool Description: Artifact Types'
description: >-
  Artifact-tool prompt paragraph for creating a new Artifact from a published
  Artifact type via type_url.
ccVersion: 2.1.246
-->
**Artifact types**: To start a new Artifact from a published Artifact type, pass `type_url` (the type's link) on a publish: with no files when you have not yet seen the type's instructions (the result carries them), or with your data files in `file_path`/`files` when you already know what the type expects. The result is an ordinary private Artifact: update it by its `url` as usual, publishing only its own files — the type's page and files are fixed, and the result lists which are which.
