<!--
name: 'Data: Command plugin source command field'
description: >-
  Describes the command field for command-based plugin sources, including its
  one-line directory output contract, cache-copy lifecycle, platform shell, and
  re-resolution behavior
ccVersion: 2.1.276
-->
Shell command that prints the absolute path of the plugin directory on stdout (exactly one line) and exits 0. It must leave a complete plugin in that directory before exiting; the directory is copied into the plugin cache, so the printed path may change between runs (it is re-resolved on every install and update, and once per session in the background). Runs through the platform shell (sh on macOS/Linux, cmd.exe on Windows) from the user's home directory with Claude Code's subprocess environment.
