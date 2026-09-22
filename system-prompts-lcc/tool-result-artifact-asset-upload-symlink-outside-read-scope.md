<!--
name: 'Tool Result: Artifact asset upload via unapproved symlink'
description: >-
  Preflight error (Myf) telling the model file_path resolves through a symlink
  into a path this session may not read, and to upload the resolved path or copy
  the file first.
ccVersion: 2.1.234
-->
file_path reaches its file through a symbolic link that resolves somewhere this session may not read without asking — upload the file by its resolved path, or copy it under the working directory first
