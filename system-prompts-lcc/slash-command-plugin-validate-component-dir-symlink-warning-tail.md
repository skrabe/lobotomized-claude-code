<!--
name: 'Plugin validate: component directory symlink warning tail'
description: >-
  Tail of the project-scope warning saying component directories are not
  followed through symlinks and must be validated at their real path.
ccVersion: 2.1.317
-->
component directories are read without following symlinks. A session loading this project does follow it, so validate the real directory separately.
