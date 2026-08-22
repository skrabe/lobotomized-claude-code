<!--
name: 'Tool Description: Artifact multi-file read guidance'
description: >-
  Artifact tool-description section explaining the list_files and read_file
  actions on a multi-file artifact, where read_file saves the file, and the
  out_dir approval caveat
ccVersion: 2.1.239
-->


**Artifact files**: a multi-file artifact's individual files can be read without fetching the whole page — `action: "list_files"` (with `url`) prints each file's path, type, and size; `action: "read_file"` (with `url` and `path`) saves that file under its published path in a folder of your scratchpad directory and tells you where — Read it from there; pass `out_dir` only when the user wants the file somewhere else, since saving outside the scratchpad asks them each time. Works for artifacts you can open in your organization.