<!--
name: 'Data: Settings sandbox filesystem allowWriteWithinDeny description'
description: >-
  Settings-schema description of sandbox.filesystem.allowWriteWithinDeny:
  directories kept writable under a denyWrite parent
ccVersion: 2.1.328
-->
Directories that stay writable although denyWrite names the directory that holds them: canonical absolute paths, each lifting the entry for its own parent directory and no other. Grants nothing that allowWrite does not. On Windows, applied only by the mxc backend, where the holding directory is one that git reads.
