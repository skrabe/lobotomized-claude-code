<!--
name: 'Slash Command: Plugin validate plugin component dir symlink'
description: >-
  Plugin validate warning that a plugin component directory is a symlink and was
  not read, with when an installed plugin follows it and how to fix or validate
  it.
ccVersion: 2.1.317
-->
This directory is a symlink, so the validator read nothing in it. An installed plugin loads it only if it points inside the plugin's installed folder, or, for a plugin read in place from a local marketplace folder, inside that folder; a project's .claude/skills plugin, only if it points inside the folder holding that .claude. Otherwise replace the link with a copy of the folder. To check its files, validate the folder it points to.
