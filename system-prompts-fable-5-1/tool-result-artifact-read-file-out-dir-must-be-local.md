<!--
name: Artifact read_file out_dir must be local
description: >-
  Validation error returned to the model when read_file's out_dir names a
  network path.
ccVersion: 2.1.239
-->
read_file saves only to local directories — out_dir names a network path.
