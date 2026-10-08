<!--
name: Project write session file read required
description: >-
  Requires reading or writing the whole session file before uploading it by
  local_path.
ccVersion: 2.1.294
-->
project_write: Read the whole file at local_path first, or pass its text as content. A file is uploaded by path only when this session has read or written all of it and it has not changed since.
