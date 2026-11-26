<!--
name: 'Tool result: read_db out_dir leading dash'
description: >-
  Validation error when read_db cannot save a collection under out_dir because a
  path part starts with '-'.
ccVersion: 2.1.332
-->
read_db does not save this collection under out_dir: a part of its path starts with "-", and shell commands would read a folder with that name as an option. Read it without out_dir.
