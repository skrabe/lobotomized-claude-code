<!--
name: 'Tool Parameter: Artifact force supporting files preservation'
description: >-
  Clarifies that a forced Artifact publish preserves supporting files unless the
  publish replaces or explicitly removes them
ccVersion: 2.1.246
-->
 Its supporting files are not discarded: every published file stays unless this publish replaces it or removes it with a null `files` entry (action "list_files" shows what is published).
