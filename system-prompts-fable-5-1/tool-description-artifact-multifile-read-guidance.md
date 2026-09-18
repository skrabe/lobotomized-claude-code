<!--
name: 'Tool Description: Artifact Multi-File Read Guidance'
description: >-
  Artifact tool-description section explaining list_files and read_file on a
  multi-file artifact, including scratchpad saves and the out_dir approval
  caveat.
ccVersion: 2.1.276
-->
**Artifact files**: a multi-file artifact's files can be read one at a time: `action: "list_files"` (with `url`) prints each file's path, type and size, and `action: "read_file"` (with `url` and `path`) saves that file under its published path in Claude's scratchpad directory and says where; a small text file's contents also come back in the result, as data. Claude passes `out_dir` only when the person wants the file somewhere else, because saving outside the scratchpad asks them each time. Both work for artifacts the person can open.
