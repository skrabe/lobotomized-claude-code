<!--
name: Project write outside-directory read required
description: >-
  Requires a full unchanged read record for a file outside the working
  directory.
ccVersion: 2.1.294
-->
project_write: Read the whole file at local_path first, or pass its text as content. Outside the working directory, a file is uploaded by path only when this session has read all of it and it has not changed since.
