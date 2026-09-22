<!--
name: 'Tool Result: Artifact write_db Network Path'
description: >-
  Error returned to the model when write_db's file_path is a
  network/UNC/automount path that cannot be sent.
ccVersion: 2.1.237
-->
write_db reads only local files — a network path (UNC share, /net automount, or device-style path) cannot be sent; copy the file onto a local disk first
