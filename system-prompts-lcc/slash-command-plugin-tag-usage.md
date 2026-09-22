<!--
name: 'Slash Command: /plugin tag — usage'
description: >-
  The /plugin tag usage text: creating a {name}--v{version} git tag for a
  plugin, and the flags it accepts.
ccVersion: 2.1.233
-->
Usage: /plugin tag [path] [--push] [--dry-run] [-f|--force]

Create a {name}--v{version} git tag for the plugin at <path> (default: .).
Validates plugin.json and any enclosing marketplace entry agree on the version.

For -m/--message and --remote, use the CLI: claude plugin tag --help
