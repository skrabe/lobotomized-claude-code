<!--
name: '/plugin validate: path not read for hooks'
description: >-
  /plugin validate warning that a path through a link or unopenable was not read
  for hooks files; asks to validate the real directory separately.
ccVersion: 2.1.326
-->
This path was not read for hooks files: it is or goes through a link (a symlink or a Windows junction), or could not be opened. The plugin loader can still take it as a plugin, so a hooks module there loads without being listed here. Validate the real directory separately.
