<!--
name: Artifact Database Write Source Symlink Restricted
description: >-
  Refuses a database write whose source symlink resolves outside permitted
  reads.
ccVersion: 2.1.294
-->
file_path reaches its file through a symbolic link that resolves somewhere this session may not read without asking — pass the resolved path, or copy the file under the working directory first
