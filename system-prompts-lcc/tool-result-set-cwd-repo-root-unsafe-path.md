<!--
name: 'Tool Result: set_cwd repository root unsafe path'
description: >-
  Rejects a set_cwd target whose repository root path has invisible characters,
  without echoing the path
ccVersion: 2.1.325
-->
The repository the target path belongs to has a root path with invisible or non-printing characters, so trust for it cannot be shown or recorded here. The path is deliberately not echoed back. To use the folder, trust it from a terminal session started there, or move the repository to a path without such characters.
