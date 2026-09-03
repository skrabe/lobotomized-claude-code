<!--
name: 'Tool Parameter: Artifact Type URL'
description: >-
  Artifact tool type_url parameter for creating a new Artifact as a private copy
  of an Artifact type's current release.
ccVersion: 2.1.237
-->
URL of an Artifact type to create this Artifact from (people may call a type a template or a starter). The new Artifact starts as a private copy of the type's current release, and `file_path`/`files` become its own files alongside the type's (omit them to create it without files of its own). Always creates a new Artifact — omit `url`; update it afterwards by its `url` like any other. The type's files, its page included, can't be replaced on it.
