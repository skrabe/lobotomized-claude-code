<!--
name: 'Tool Result: db_read out_dir Moved Before Any Save'
description: >-
  ArtifactInputError when out_dir no longer resolves at the start of a db_read
  save, so nothing was written.
ccVersion: 2.1.251
-->
out_dir no longer resolves where it did when the save was approved — nothing was saved; retry so it is checked again.
