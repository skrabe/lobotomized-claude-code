<!--
name: 'Tool Result: Artifact upload asset path contains URL scheme'
description: >-
  Upload validation message that a path cannot contain ://, to give a disk path,
  and to write one slash after a colon.
ccVersion: 2.1.325
-->
a path cannot hold "://", even with invisible characters in between. Give the file's path on disk, not a link. If that path has a colon in it, write one slash after the colon.
