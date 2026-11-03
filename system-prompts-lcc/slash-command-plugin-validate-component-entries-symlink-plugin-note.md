<!--
name: 'Slash Command: Plugin validate component entries symlink plugin note'
description: >-
  Note appended to plugin component symlink warnings explaining when
  --plugin-dir, installed or .claude/skills plugins follow a symlink and to
  validate its target.
ccVersion: 2.1.317
-->
A session started with --plugin-dir on this plugin follows a symlink here. An installed plugin follows one only if it points inside the plugin's installed folder, or, for a plugin read in place from a local marketplace folder, inside that folder; a project's .claude/skills plugin, only if it points inside the folder holding that .claude. To check what a symlink points to, validate that path.
