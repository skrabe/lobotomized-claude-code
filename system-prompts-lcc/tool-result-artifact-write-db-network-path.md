<!--
name: 'Tool Result: Artifact write_db Network Path'
description: >-
  Error returned to the model when write_db's file_path is a network path (UNC
  share, /net automount or device-style), reaches one through a link, or has an
  unexaminable directory or link on the way.
ccVersion: 2.1.281
-->
write_db reads only local files — file_path names a network path (UNC share, /net automount, or device-style path), reaches one through a link on the way, or has a directory or link on the way that could not be examined; if the file is on a network location, copy it onto a local disk first
